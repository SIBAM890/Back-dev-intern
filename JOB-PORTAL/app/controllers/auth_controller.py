from flask import request, jsonify
from app.extensions.db import db
from app.models.user import User
from flask_jwt_extended import create_access_token

def register():
    data = request.get_json()
    
    # Check if user already exists
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'message': 'User already exists'}), 400

    # Create new user
    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        is_admin=data.get('is_admin', False)
    )
    
    # Hash password
    new_user.set_password(data.get('password'))
    
    # Save to DB
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    
    if user and user.check_password(data.get('password')):
        # --- THE FIX IS HERE ---
        # We must convert user.id to a string using str()
        access_token = create_access_token(identity=str(user.id))
        
        return jsonify({'access_token': access_token}), 200
        
    return jsonify({'message': 'Invalid credentials'}), 401