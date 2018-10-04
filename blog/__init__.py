from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


# 创建数据库对象
db = SQLAlchemy()

# admin对象
blog_admin = Admin(name="博客后台")


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

    # 初始化admin对象
    blog_admin.init_app(app)

    # 导入admin配置
    from blog import admin

    # 返回app对象
    return app
