"""后台相关"""

# 蓝图
from flask import Blueprint


admin_blu = Blueprint("admin_blu", __name__)


from .views import *
