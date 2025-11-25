# app/__init__.py
from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, bcrypt 
# Removed 'ma'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    # Removed ma.init_app(app)

    # Register Blueprints
    from app.routes import auth_bp, job_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(job_bp)
    
    with app.app_context():
        db.create_all()

    return app