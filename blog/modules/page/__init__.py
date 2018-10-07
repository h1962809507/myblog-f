"""首页视图相关"""
from flask import Blueprint


page_blu = Blueprint("page_blu", __name__)


from .views import *
