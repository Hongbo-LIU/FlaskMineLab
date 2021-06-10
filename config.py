import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:   # 创建了一个Config的类。 类中的变量如下：
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.qq.com'     # os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = 465                 # os.environ.get('MAIL_PORT', '465')
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = False              # os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', 'on', 1]
    MAIL_USERNAME = '41120763@qq.com'   # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'wzpzjcrgjqhubhia'  # os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <41120763@qq.com>'
    FLASKY_ADMIN = os.environ.get('FLAKSY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_COMMENTS_PER_PAGE = 10
    BOOTSTRAP_BTN_SIZE = 'sm'
    # BOOTSTRAP_BOOTSWATCH_THEME = 'Lumen'

    @staticmethod
    def init_app(app):  # 创建类中的函数，进行初始化
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
