from flask import render_template
from blog.models import Article
from . import index_blu


@index_blu.route('/')
def index():
    articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    return render_template("blog/index.html", articles=articles)
