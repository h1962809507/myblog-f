import markdown
from flask import render_template, current_app, abort, request

from blog import db
from blog.models import Article
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

    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render_template("blog/single.html", article=article)


@article_blu.route("/comment", methods=["POST"])
def comment():
    print(request.json)
    return "ok"