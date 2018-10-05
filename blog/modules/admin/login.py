from flask import render_template
from flask_admin import AdminIndexView, expose
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("输入昵称", validators=[DataRequired()], render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("输入密码", validators=[DataRequired()], render_kw={"placeholder": "请输入密码"})
    submit = SubmitField("登录")


class IndexView(AdminIndexView):
    @expose()
    def index(self):
        login_form = LoginForm()
        return render_template("admin/index.html", form=login_form)
