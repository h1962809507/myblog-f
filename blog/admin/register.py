from flask_script import Command

from blog import db
from blog.models import User


class Register (Command):
    # 注册管理员账号，加入到flask-script命令中，使用命令创建，不在页面显示
    def run(self):
        num = input("输入帐号：")
        user_num = None
        try:
            user_num = User.query.filter(User.num == num).first()
        except Exception as e:
            print(e)
            print("获取失败!")
            return

        if user_num:
            print("帐号已注册！")
            return

        nick_name = input("输入昵称：")
        avatar_url = input("输入头像地址：")
        password = input("输入密码：")

        user = User()
        user.nick_name = nick_name
        user.num = num
        user.avatar_url = avatar_url
        # 这里使用了@property，会自动加密密码，并赋值给password_hash
        user.password = password

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            print("注册失败！")
            return
        print("注册成功！")
