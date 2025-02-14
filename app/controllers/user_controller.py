from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_service.get_all_users())

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user) if user else jsonify({'error': 'User not found'}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = user_service.create_user(data)
    return jsonify(new_user), 201

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404