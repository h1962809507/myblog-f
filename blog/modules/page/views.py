from flask import render_template
from blog.models import Article, Category, Tag
from . import page_blu


def blog_tag():
    # 获取侧边栏数据
    context = {
        "new_articles": Article.query.order_by(Article.create_time.desc()).all()[:5],
        "categories": Category.query.order_by(Category.id.asc()).all(),
        "tags": Tag.query.order_by(Tag.id.asc()).all()
    }
    return context


@page_blu.route('/')
def index():
    # 首页视图
    articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    name = "首页"
    context = blog_tag()
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@page_blu.route("/article/all")
def all_articles():
    # 全部文章页视图
    articles = Article.query.order_by(Article.create_time.desc()).all()
    name = "全部文章"
    context = blog_tag()
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@page_blu.route("/category/<int:code>")
def category(code):
    # 分类页视图
    articles = Category.query.get(code).article
    name = Category.query.get(code).name
    context = blog_tag()
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@page_blu.route("/tag/<int:code>")
def tag(code):
    # 标签页视图
    articles = Tag.query.get(code).article
    name = Tag.query.get(code).name
    context = blog_tag()
    return render_template("blog/index.html", articles=articles, name=name, context=context)


@page_blu.route("/about")
def about():
    name = "关于"
    context = blog_tag()
    return render_template("blog/about.html", name=name, context=context)


@page_blu.route("/contact")
def contact():
    name = "联系"
    context = blog_tag()
    return render_template("blog/contact.html", name=name, context=context)
