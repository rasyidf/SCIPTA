# -*- encoding: utf-8 -*-


from flask import Flask, url_for, g, request
from flask_babel import Babel
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

db = SQLAlchemy()
login_manager = LoginManager() 
babel = Babel()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)
    @babel.localeselector
    def get_locale():

        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale

        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return g.lang_code
        
    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone

def register_blueprints(app):
    for module_name in ('admin','base', 'home', 'api'):
        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config) 
    with app.app_context():
        register_extensions(app)
        register_blueprints(app)
        configure_database(app)
        
    return app
