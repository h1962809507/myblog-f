from flask_admin.contrib.sqla import ModelView
from blog import blog_admin, db
from blog.models import User
from blog.models import Post
from blog.models import Category
from blog.models import Tag


blog_admin.add_view(ModelView(User, db.session, name="用户管理"))
blog_admin.add_view(ModelView(Post, db.session, name="文章管理"))
blog_admin.add_view(ModelView(Category, db.session, name="分类管理"))
blog_admin.add_view(ModelView(Tag, db.session, name="标签管理"))
