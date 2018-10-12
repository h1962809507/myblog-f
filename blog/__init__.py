from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_wtf import CSRFProtect
from blog.admin.index import IndexView
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel
import logging

# 创建数据库对象
db = SQLAlchemy()

# 创建admin对象，首页视图使用重写的IndexView类
blog_admin = Admin(name="博客后台", index_view=IndexView(name='登录'))


def set_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 获取配置
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/logs", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    # 初始化app对象
    set_log(config_name)
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 汉化
    babel = Babel(app)

    CSRFProtect(app)

    # 初始化数据库对象
    db.init_app(app)

    # 初始化admin对象
    blog_admin.init_app(app)

    # 导入admin配置
    from blog.admin import admin

    # 注册蓝图
    from blog.modules.page import page_blu
    app.register_blueprint(page_blu)

    from blog.modules.admin import admin_blu
    app.register_blueprint(admin_blu)

    from blog.modules.article import article_blu
    app.register_blueprint(article_blu)

    # 注册函数
    from blog.modules.page import blog_tag
    app.add_template_global(blog_tag)

    # 返回app对象
    return app

