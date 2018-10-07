"""关于，联系页视图相关"""
from flask import Blueprint


about_blu = Blueprint("about_blu", __name__)


from .views import *
