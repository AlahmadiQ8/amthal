from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.pymongo import PyMongo
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from config import config
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

bootstrap = Bootstrap()
mongo = PyMongo()
mail = Mail()
moment = Moment()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.jinja_env.trim_blocks = True
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mongo.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
