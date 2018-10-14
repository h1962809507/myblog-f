import time

from flask import flash, request, redirect, session, current_app

from blog.admin.upload_image import storage
from blog.models import User
from . import admin_blu


def is_admin():
    #  访问后台权限验证
    num = session.get("num", None)
    if num:
        return True
    return False


@admin_blu.route('/login', methods=["POST"])
def login():
    # 后台登录验证
    num = request.form.get("num")
    password = request.form.get("password")
    user = None
    try:
        user = User.query.filter(User.num == num).first()
    except Exception as e:
        flash(e)
        return redirect("/admin")

    if not user:
        flash("帐号不存在！")
        return redirect("/admin")

    # 判断密码是否正确，models封装好的方法，调用即可
    if not user.check_password(password):
        flash("密码错误！")
        return redirect("/admin")

    # 写入session
    session["num"] = num

    return redirect("/admin/article")


@admin_blu.route("/add_article", methods=["POST"])
def add_article():
    print(request.form)
    try:
        img = request.files.get("cover").read()
    except Exception as e:
        current_app.logger.error(e)
        return "图片获取失败"

    date = int(time.time())
    key = "blog/cover/" + str(date)

    # 图片到七牛
    try:
        url = storage(img, key)
    except Exception as e:
        current_app.logger.error(e)
        return "上传图片错误"
    print("http://image.mxuanli.cn/"+url)
    return "xixi"
