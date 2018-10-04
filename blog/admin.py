from flask_admin.contrib.sqla import ModelView
from blog import blog_admin, db
from blog.models import User
from blog.models import Post
from blog.models import Category
from blog.models import Tag

is_true = True


class UserView(ModelView):

    column_list = ('num', 'nick_name')

    column_labels = {
            "num": u"帐号",
            "nick_name": u"昵称",
            "password_hash": u"密码",
            "avatar_url": u"头像"
    }

    def is_accessible(self):
        return is_true

    def __init__(self, session, **kwargs):
        super().__init__(User, session, **kwargs)


class PostView(ModelView):
    column_labels = {
        "title": u"标题",
        "digest": u"摘要",
        "content": u"内容",
        "user": u"作者",
        "click": u"点击",
        "category": u"分类",
        "tag": u"标签",
        "create_time": u"创建时间",
        "update_time": u"修改时间"
    }

    def is_accessible(self):
        return is_true

    def __init__(self, session, **kwargs):
        super().__init__(Post, session, **kwargs)


class CategoryView(ModelView):
    column_labels = {
            "name": u"名称"
    }

    def is_accessible(self):
        return is_true

    def __init__(self, session, **kwargs):
        super().__init__(Category, session, **kwargs)


class TagView(ModelView):
    column_labels = {
            "name": u"名称"
    }

    def is_accessible(self):
        return is_true

    def __init__(self, session, **kwargs):
        super().__init__(Tag, session, **kwargs)


blog_admin.add_view(PostView(db.session, name="文章管理"))
blog_admin.add_view(UserView(db.session, name="用户管理"))
blog_admin.add_view(CategoryView(db.session, name="分类管理"))
blog_admin.add_view(TagView(db.session, name="标签管理"))
