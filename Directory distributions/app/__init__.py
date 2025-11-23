from flask import Flask
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'
    # Register blueprints
    app.register_blueprint(auth_bp)
    
    return app