import markdown
from flask import render_template
from blog.models import Article, Category
from . import article_blu


@article_blu.route("/article/<int:code>")
def detail(code):
    article = Article.query.get(code)
    articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render_template("blog/single.html", article=article, articles=articles)


@article_blu.route("/article/all")
def index():
    articles = Article.query.order_by(Article.create_time.desc()).all()
    categories = Category.query.order_by(Category.id.asc()).all()
    name = "全部文章"
    return render_template("blog/index.html", articles=articles, categories=categories, name=name)
