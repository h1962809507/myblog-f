from flask import render_template

from blog.models import Article
from . import article_blu


@article_blu.route("/article/<int:code>")
def detail(code):
    article = Article.query.get(code)
    return render_template("blog/single.html", article=article)
