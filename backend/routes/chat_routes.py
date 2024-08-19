from flask import Blueprint, request, jsonify
from models.db_init import db
from models.models import Chat
from models.branch import Branch
from utils.openai_helper import query_openai_api  # Import der OpenAI-Hilfsfunktion
import os

chat_bp = Blueprint('chat_bp', __name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

chats = []
branches = [] 

@chat_bp.route('/chats', methods=['POST'])
def create_chat():
    data = request.json
    chat_id = len(chats) + 1
    chat = {"id": chat_id, "message": data.get('message')}
    chats.append(chat)
    return jsonify(chat), 201

@chat_bp.route('/chats', methods=['GET'])
def get_chats():
    return jsonify(chats), 200

@chat_bp.route('/chats/<int:chat_id>', methods=['GET'])
def get_chat(chat_id):
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if chat:
        return jsonify(chat), 200
    return jsonify({"error": "Chat not found"}), 404

@chat_bp.route('/chats/<int:chat_id>', methods=['PUT'])
def update_chat(chat_id):
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if chat:
        data = request.json
        chat['message'] = data.get('message')
        return jsonify(chat), 200
    return jsonify({"error": "Chat not found"}), 404

@chat_bp.route('/chats/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    global chats
    chats = [chat for chat in chats if chat['id'] != chat_id]
    return jsonify({"message": "Chat deleted"}), 200

@chat_bp.route('/branches/create', methods=['POST'])
def create_branch():
    data = request.json
    parent_id = data.get('parent_id')
    chat_id = data.get('chat_id')
    message = data.get('message')
    
    # Verwenden der ausgelagerten OpenAI-Funktion
    reply = query_openai_api([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ])
    
    # Create new branch
    branch_id = len(branches) + 1  # Einfache in-memory ID
    new_branch = Branch(branch_id=branch_id, chat_id=chat_id, parent_id=parent_id, content=reply)
    branches.append(new_branch)
    
    return jsonify({
        "branch_id": new_branch.branch_id,
        "chat_id": new_branch.chat_id,
        "parent_id": new_branch.parent_id,
        "content": new_branch.content,
        "created_at": new_branch.created_at
    }), 201

@chat_bp.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    branch = next((b for b in branches if b.branch_id == branch_id), None)
    if branch:
        return jsonify({
            "branch_id": branch.branch_id,
            "chat_id": branch.chat_id,
            "parent_id": branch.parent_id,
            "content": branch.content,
            "created_at": branch.created_at
        }), 200
    return jsonify({"error": "Branch not found"}), 404
