from flask import render_template, redirect, session
from flask_admin import AdminIndexView, expose
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    num = StringField("输入昵称", validators=[DataRequired()], render_kw={"placeholder": "请输入帐号"})
    password = PasswordField("输入密码", validators=[DataRequired()], render_kw={"placeholder": "请输入密码"})
    submit = SubmitField("登录")


class IndexView(AdminIndexView):
    @expose()
    def index(self):
        # 后台登录验证
        if session.get("num", None):
            return redirect("/admin/article")

        # 重写AdminIndexView类中index方法，在访问后台首页页面时，执行重写的方法
        login_form = LoginForm()
        return render_template("admin/index.html", form=login_form)
