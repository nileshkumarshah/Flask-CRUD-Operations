from flask import Flask
from apps.app1 import app1_blueprint

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Register blueprints for modular apps
    app.register_blueprint(app1_blueprint, url_prefix='/app1')

    # Application configurations can go here
    app.config.from_object('config.Config')
    
    # Initialize SQLAlchemy
    db = SQLAlchemy(app)

    # Import models
    from apps.app1.models import User

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    return app
