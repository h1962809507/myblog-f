import logging
from redis import StrictRedis


class Config:
    """flask配置"""
    DEBUG = True
    SECRET_KEY = "myblog"
    # 数据库配置
    SQL = "mysql"
    DRIVER = "mysqlclient"
    USERNAME = "root"
    PASSWORD = "aaa"
    HOST = "127.0.0.1"
    PORT = "3306"
    DATABASE = "myblog"
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s" % (SQL, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BABEL_DEFAULT_LOCALE = 'zh_CN'

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session配置
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 10

    # 默认的配置等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False
    LOG_LEVEL = logging.ERROR


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
