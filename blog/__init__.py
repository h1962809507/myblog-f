from flask import Flask
from flask_wtf import CSRFProtect
from blog.modules.admin import IndexView
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel


# 创建数据库对象
db = SQLAlchemy()

# admin对象endpoint=endpoint, url=url
blog_admin = Admin(name="博客后台", index_view=IndexView(name='登录'))


def create_app(config_name):
    # 初始化app对象
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 注册蓝图
    from blog.modules.index import index_blu
    app.register_blueprint(index_blu)

    # 汉化
    babel = Babel(app)

    CSRFProtect(app)

    # 初始化数据库对象
    db.init_app(app)

    # 初始化admin对象
    blog_admin.init_app(app)

    # 导入admin配置
    from blog import admin

    # 返回app对象
    return app
