from flask import Blueprint, request, jsonify
from utils.context_manager import ContextManager 
from models.db_init import db
from models.models import Chat, Branch  
from utils.openai_helper import query_openai_api  
import os

chat_bp = Blueprint('chat_bp', __name__)
context_manager = ContextManager()

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    
    
    reply = query_openai_api([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ])
    
    return jsonify({"reply": reply}), 200

@chat_bp.route('/chats', methods=['POST'])
def create_chat():
    data = request.json
    new_chat = Chat(user_id=data.get('user_id', 1), message=data.get('message'))
    db.session.add(new_chat)
    db.session.commit()
    return jsonify({
        "id": new_chat.id,
        "user_id": new_chat.user_id,
        "message": new_chat.message,
        "created_at": new_chat.created_at
    }), 201

@chat_bp.route('/chats', methods=['GET'])
def get_chats():
    chats = Chat.query.all()
    return jsonify([{
        "id": chat.id,
        "user_id": chat.user_id,
        "message": chat.message,
        "created_at": chat.created_at
    } for chat in chats]), 200

@chat_bp.route('/chats/<int:chat_id>', methods=['GET'])
def get_chat(chat_id):
    chat = db.session.get(Chat, chat_id)
    if chat:
        return jsonify({
            "id": chat.id,
            "user_id": chat.user_id,
            "message": chat.message,
            "created_at": chat.created_at
        }), 200
    return jsonify({"error": "Chat not found"}), 404

@chat_bp.route('/chats/<int:chat_id>', methods=['PUT'])
def update_chat(chat_id):
    chat = db.session.get(Chat, chat_id)
    if chat:
        data = request.json
        chat.message = data.get('message')
        db.session.commit()
        return jsonify({
            "id": chat.id,
            "user_id": chat.user_id,
            "message": chat.message,
            "created_at": chat.created_at
        }), 200
    return jsonify({"error": "Chat not found"}), 404

@chat_bp.route('/chats/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    chat = db.session.get(Chat, chat_id)
    if chat:
        db.session.delete(chat)
        db.session.commit()
        return jsonify({"message": "Chat deleted"}), 200
    return jsonify({"error": "Chat not found"}), 404

@chat_bp.route('/branches/create', methods=['POST'])
def create_branch():
    data = request.json
    chat_id = data.get('chat_id')
    message = data.get('message')

    # get the context 
    context = context_manager.get_context(chat_id)

   # Insert  message into  context
    context_manager.add_message(chat_id, user_message=message)

    # Check if the context is empty before sending
    if not context:
        context = [{"role": "system", "content": "You are a helpful assistant."}]

    # Request to the OpenAI API with the entire context
    reply = query_openai_api(context)

   # Add the assistance system's response to the context
    context_manager.add_message(chat_id, assistant_message=reply)

   # Create the new branch with the answer
    new_branch = Branch(chat_id=chat_id, branch_content=reply)
    db.session.add(new_branch)
    db.session.commit()

    return jsonify({
        "id": new_branch.id,
        "branch_id": new_branch.id,
        "chat_id": new_branch.chat_id,
        "branch_content": new_branch.branch_content,
        "created_at": new_branch.created_at
    }), 201



@chat_bp.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    branch = db.session.get(Branch, branch_id)
    if branch:
        return jsonify({
            "branch_id": branch.id,  
            "chat_id": branch.chat_id,
            "branch_content": branch.branch_content,
            "created_at": branch.created_at
        }), 200
    return jsonify({"error": "Branch not found"}), 404
