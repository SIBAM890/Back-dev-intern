from app.routes import auth_bp
from app.controllers.auth_controller import register, login

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)