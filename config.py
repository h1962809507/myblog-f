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


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
