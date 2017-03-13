from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models
    # @app.route('/')
    # def index():
    #     return '<h1>Hello World</h1>'    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    return app
