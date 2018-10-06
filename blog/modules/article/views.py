import markdown
from flask import render_template
from blog.models import Article
from . import article_blu


@article_blu.route("/article/<int:code>")
def detail(code):
    article = Article.query.get(code)
    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render_template("blog/single.html", article=article)


@article_blu.route("/article/all")
def index():
    articles = Article.query.order_by(Article.create_time.desc()).all()
    return render_template("blog/index.html", articles=articles)
