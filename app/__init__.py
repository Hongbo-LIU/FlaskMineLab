from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
pagedown = PageDown()


def create_app(config_name):    # 创建设置信息
    app = Flask(__name__)
    # app的config方法是通过Flask类里面获得的,也就是说从对象中加载（比较常用的方式）app.config.from_object()
    # 其中 app.config = app.make_config(instance_relative_config)
    # make_config(instance_relative_config)函数返回的是config_class这样的方法，
    # config_name 来自于 flasky.py中config的类而来。
    # 比较详细的讲解可以参考：https://blog.csdn.net/bestallen/article/details/52225577
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_profix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_profix='/api/v1')

    from .MineCOG import MineCOG as MineCOG_blueprint
    app.register_blueprint(api_blueprint, url_profix='/MineCOG/v1')

    return app


