from flask import flash, request, redirect, session
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
    data = request.form
    print(data)
    return "xixi"
