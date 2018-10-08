from flask import render_template, current_app

from blog import db
from blog.models import Article, Category, Tag
from . import page_blu
from sqlalchemy import extract


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

    archives = db.session.query(extract('year', Article.create_time).label('year')).group_by('year').all()

    articles = []
    for a in archives:
        articles.append(
            (a[0], db.session.query(Article).filter(extract('year', Article.create_time) == a[0]).all()))

    name = "归档"
    return render_template("blog/archives.html", articles=articles, name=name)
