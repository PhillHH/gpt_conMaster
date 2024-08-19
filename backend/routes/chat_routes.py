from flask import Blueprint, request, jsonify
from models.db_init import db
from models.models import Chat, Branch  # Importiere das Branch-Modell aus models
from utils.openai_helper import query_openai_api  # Import der OpenAI-Hilfsfunktion
import os

chat_bp = Blueprint('chat_bp', __name__)

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

    # Verwenden der ausgelagerten OpenAI-Funktion
    reply = query_openai_api([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ])
    
    # Create new branch
    new_branch = Branch(chat_id=chat_id, branch_content=reply)
    db.session.add(new_branch)
    db.session.commit()

    return jsonify({
        "id": new_branch.id,
        "branch_id": new_branch.id,  # Hier korrigiert: branch_id sollte new_branch.id sein
        "chat_id": new_branch.chat_id,
        "branch_content": new_branch.branch_content,
        "created_at": new_branch.created_at
    }), 201


@chat_bp.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    branch = db.session.get(Branch, branch_id)
    if branch:
        return jsonify({
            "branch_id": branch.id,  # Hier muss branch.id stehen, um den richtigen Wert zurückzugeben
            "chat_id": branch.chat_id,
            "branch_content": branch.branch_content,
            "created_at": branch.created_at
        }), 200
    return jsonify({"error": "Branch not found"}), 404
