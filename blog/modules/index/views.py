from flask import render_template
from blog.models import Article, User
from . import index_blu


@index_blu.route('/')
def index():
    # post = Post.query.order_by(Post.id.asc()).paginate(2, 3)
    user = User.query.all()
    # print(post)
    return render_template("blog/index.html")
