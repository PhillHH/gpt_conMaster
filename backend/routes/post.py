from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.models.post import Post
from backend.app import db

post_bp = Blueprint('post', __name__)

@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200

@post_bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict()), 200

@post_bp.route('/', methods=['POST'])
@login_required
def create_post():
    data = request.json
    title = data.get('title')  # 'your_post_title'
    content = data.get('content')  # 'your_post_content'
    
    new_post = Post(
        title=title,
        content=content,
        user_id=current_user.id
    )
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify(new_post.to_dict()), 201

@post_bp.route('/<int:id>', methods=['PUT'])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.json
    post.title = data.get('title', post.title)  # 'updated_title'
    post.content = data.get('content', post.content)  # 'updated_content'
    
    db.session.commit()
    
    return jsonify(post.to_dict()), 200

@post_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    
    db.session.delete(post)
    db.session.commit()
    
    return jsonify({"message": "Post deleted"}), 200