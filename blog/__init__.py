from flask import Flask
from config import config


def create_app(config_name):
    # 初始化app对象
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 返回app对象
    return app
