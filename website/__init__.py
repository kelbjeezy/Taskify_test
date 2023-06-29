from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisgoingtobeataskapp123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from jinja2 import Environment
    from .views import views
    from .auth import auth
    from datetime import datetime

    env = Environment()

    @app.template_filter('enumerate')
    def jinja2_enumerate(iterable):
        return enumerate(iterable)

    @app.template_filter('format_datetime')
    def jinja2_format_datetime(date):
        return datetime.strptime(date, "%Y-%m-%d").date()
    
    
    @app.template_filter('get_datetime')
    def jinja2_get_datetime(placeholder):
        return datetime.now().date()

    env.filters['enumerate'] = jinja2_enumerate
    env.filters['format_datetime'] = jinja2_format_datetime
    env.filters['get_datetime'] = jinja2_get_datetime




    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Tasks

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database')


