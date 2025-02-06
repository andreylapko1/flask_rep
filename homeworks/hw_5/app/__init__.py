from flask import Flask
from app.routers.questions import questions_bp
from app.routers.responses import responses_bp
from app.routers.categories import categories_bp
from config import DevelopmentConfig
from app.models import db
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(questions_bp)
    app.register_blueprint(responses_bp)
    app.register_blueprint(categories_bp)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    return app

