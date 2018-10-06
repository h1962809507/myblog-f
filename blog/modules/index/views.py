from flask import render_template
from blog.models import Article, Category
from . import index_blu


@index_blu.route('/')
def index():
    articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    categories = Category.query.order_by(Category.id.asc()).all()
    name = "首页"
    return render_template("blog/index.html", articles=articles, categories=categories, name=name)
