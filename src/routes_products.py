from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src.models import db, User
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register():
    data = request.json
    hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
    user = User(username=data['username'], password=hashed)
    db.session.add(user)
    db.session.commit()
    return {'message':'registered'}

@auth_bp.post('/login')
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.checkpw(data['password'].encode(), user.password.encode()):
        token = create_access_token(identity=user.username)
        return {'token': token}
    return {'message':'invalid credentials'}, 401