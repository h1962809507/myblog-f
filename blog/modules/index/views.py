from flask import render_template
from blog.models import Article, Category, Tag
from . import index_blu


@index_blu.route('/')
def index():
    articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    name = "首页"
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).all()[:5],
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@index_blu.route("/article/all")
def all_articles():
    articles = Article.query.order_by(Article.create_time.desc()).all()
    name = "全部文章"
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).all()[:5],
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@index_blu.route("/category/<int:code>")
def category(code):
    articles = Category.query.get(code).article
    name = Category.query.get(code).name
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).all()[:5],
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@index_blu.route("/tag/<int:code>")
def tag(code):
    articles = Tag.query.get(code).article
    name = Tag.query.get(code).name
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).all()[:5],
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return render_template("blog/index.html", articles=articles, name=name, context=context)
