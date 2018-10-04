"""后台相关"""

# 登录
from .admin import *

# 注册视图

from flask import Blueprint


admin_blu = Blueprint("admin_blu", __name__)


from .views import *