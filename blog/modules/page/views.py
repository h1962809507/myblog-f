import collections
from flask import render_template, current_app
from flask.json import jsonify

from blog import db
from blog.models import Article, Category, Tag
from . import page_blu
from sqlalchemy import extract, and_


def blog_tag():
    # 获取侧边栏数据
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).limit(5),
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return context


@page_blu.route('/')
def index():
    # 首页视图
    articles = Article.query.order_by(Article.create_time.desc()).limit(4)
    name = "首页"
    return render_template("blog/index.html", articles=articles, name=name)


@page_blu.route("/article/all")
def all_articles():
    # 全部文章页视图
    articles = Article.query.order_by(Article.create_time.desc()).all()
    name = "全部文章"
    return render_template("blog/index.html", articles=articles, name=name)


@page_blu.route("/category/<int:code>")
def category(code):
    # 分类页视图
    articles = Category.query.get(code).article
    name = Category.query.get(code).name
    return render_template("blog/index.html", articles=articles, name=name)


@page_blu.route("/tag/<int:code>")
def tag(code):
    # 标签页视图
    articles = Tag.query.get(code).article
    name = Tag.query.get(code).name
    return render_template("blog/index.html", articles=articles, name=name)


@page_blu.route("/about")
def about():
    # 关于页面
    name = "关于"
    return render_template("blog/about.html", name=name)


@page_blu.route("/contact")
def contact():
    # 联系页面
    name = "联系"
    return render_template("blog/contact.html", name=name)


@page_blu.route("/archives")
def archive():
    # 归档页面

    articles = Article.query.order_by(Article.create_time.desc()).all()
    articles_list = collections.OrderedDict()
    for article in articles:
        year = article.create_time.year
        month = article.create_time.month
        time = str(year) + str(month)
        articles_list[time] = db.session.query(Article).filter(
            and_(extract('year', Article.create_time) == year,
                 extract('month', Article.create_time) == month)).all()
    name = "归档"
    return render_template("blog/archives.html", articles=articles_list, name=name)
