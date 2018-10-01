from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


# 创建数据库对象
db = SQLAlchemy()


def create_app(config_name):
    # 初始化app对象
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 注册蓝图
    from blog.modules.index import index_blu
    app.register_blueprint(index_blu)

    # 初始化数据库对象
    db.init_app(app)

    # 返回app对象
    return app
