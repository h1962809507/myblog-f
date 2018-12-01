import markdown
from flask import render_template, current_app, abort, request, jsonify

from blog import db
from blog.models import Article, Comment
from . import article_blu


@article_blu.route("/article/<int:code>")
def detail(code):
    article = ""
    try:
        article = Article.query.get(code)
        article.click += 1
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        abort(500)

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.toc',
        'markdown.extensions.tables',
        'markdown.extensions.codehilite',
    ])

    article.content = md.convert(article.content)
    article.toc = md.toc
    return render_template("blog/single.html", article=article)


@article_blu.route("/comment", methods=["POST"])
def comment_view():
    """保存评论"""
    # article_id 文章id
    # parent_id 父评论id
    # name 回复者名字
    # email 邮箱
    # url 网址
    # content 评论内容
    data = request.json
    article_id = data.get("article_id")
    parent_id = data.get("parent_id")
    name = data.get("name")
    email = data.get("email")
    url = data.get("url")
    content = data.get("content")
    reply_name = data.get("reply_name")

    # 验证参数
    if not all([article_id, name, email, url, content]):
        return jsonify(state="参数不足")
    try:
        article_id = int(article_id)
        if parent_id:
            parent_id = int(parent_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(state="参数错误")

    # 保存数据
    comment = Comment()
    comment.article_id = article_id
    comment.parent_id = parent_id
    comment.nick_name = name
    comment.email = email
    comment.url = url
    comment.content = content
    comment.reply_name = reply_name

    db.session.add(comment)

    # 提交数据
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(state="数据保存失败")
    comment_id = comment.id
    print(comment.create_time)
    comment_time = str(comment.create_time)
    return jsonify(state="ok", comment_id=comment_id, comment_time=comment_time)
