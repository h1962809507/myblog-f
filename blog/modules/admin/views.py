from flask import flash, request, redirect
from blog.models import User
from . import admin_blu


admin = False


def is_admin(*args):
    if args:
        global admin
        admin = True
    return admin


@admin_blu.route('/login', methods=["POST"])
def login():
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

    is_admin(True)

    return redirect("/admin/post")
