import markdown
from flask import render_template, current_app, abort
from blog.models import Article
from . import article_blu


@article_blu.route("/article/<int:code>")
def detail(code):
    article = Article.query.get(code)
    articles = list()
    try:
        articles = Article.query.order_by(Article.create_time.desc()).all()[:4]
    except Exception as e:
        current_app.logger.error(e)
        abort(500)
    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render_template("blog/single.html", article=article, articles=articles)
