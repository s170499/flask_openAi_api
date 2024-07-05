from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from models import models
        db.create_all()

    return app