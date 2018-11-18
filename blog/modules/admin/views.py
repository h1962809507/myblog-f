import time
from flask import flash, request, redirect, session, current_app
from blog import db
from blog.admin.admin import is_admin
from blog.admin.upload_image import storage
from blog.models import User, Article
from . import admin_blu


@admin_blu.route('/login', methods=["POST"])
def login():
    num = request.form.get("num")
    password = request.form.get("password")
    user = None
    try:
        user = User.query.filter(User.num == num).first()
    except Exception as e:
        flash(e)
        return redirect("/admin")

    if not user:
        flash("帐号不存在！")
        return redirect("/admin")

    # 判断密码是否正确，models封装好的方法，调用即可
    if not user.check_password(password):
        flash("密码错误！")
        return redirect("/admin")

    # 写入session
    session["num"] = num

    return redirect("/admin/article")


@admin_blu.route("/add_article", methods=["POST"])
def add_article():
    # 获取数据
    try:
        title = request.form.get("title")
        digest = request.form.get("digest")
        author_id = request.form.get("author")
        category_id = request.form.get("category")
        tag_id = request.form.get("tag")
        content = request.form.get("content")
    except Exception as e:
        current_app.logger.error(e)
        return "数据获取失败"

    date = int(time.time())
    key = "blog/cover/" + str(date)

    cover_url = "http://image.mxuanli.cn/" + key

    # 验证数据
    if not all([title, digest, author_id, category_id, tag_id, content, cover_url]):
        return "参数不全"
    try:
        author_id = int(author_id)
        category_id = int(category_id)
        tag_id = int(tag_id)
    except Exception as e:
        current_app.logger.error(e)
        return "参数错误"

    try:
        img = request.files.get("cover").read()
    except Exception as e:
        current_app.logger.error(e)
        return "图片获取失败"

    # 保存数据
    article = Article()
    article.title = title
    article.digest = digest
    article.author = author_id
    article.category_id = category_id
    article.tag_id = tag_id
    article.content = content
    article.cover_url = cover_url

    # 插入数据
    db.session.add(article)

    # 图片到七牛
    try:
        url = storage(img, key)
    except Exception as e:
        current_app.logger.error(e)
        return "上传图片错误"

    # 保存数据到数据库
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return "数据保存失败"

    return "ok"
