"""文章页视图相关"""
from flask import Blueprint


article_blu = Blueprint("article_blu", __name__)


from .views import *
