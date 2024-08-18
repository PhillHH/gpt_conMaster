# routes/chat_routes.py
from flask import Blueprint, request, jsonify
from models.db_init import db
from models.models import Chat

chat_bp = Blueprint('chat_bp', __name__)

chats = []

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
