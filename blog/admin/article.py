from flask import current_app, abort, request
from flask_admin import expose, BaseView
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from blog.models import Category, Tag, User


class AddArticleForm(FlaskForm):
    title = TextAreaField("标题", validators=[DataRequired("请输入标题")])
    digest = TextAreaField("摘要", validators=[DataRequired("请输入摘要")])
    author = SelectField('作者', validators=[DataRequired("请选择")],
                         choices=[])
    category = SelectField('分类', validators=[DataRequired("请选择")],
                         choices=[])
    tag = SelectField('标签', validators=[DataRequired("请选择")],
                           choices=[])

    cover = FileField("封面", validators=[FileRequired("没有选择文件"), FileAllowed(['jpg', 'png'])])

    context = TextAreaField("内容", validators=[DataRequired("请输入内容")])


class AddArticleView(BaseView):

    @expose('/', methods=["POST", "GET"])
    def index(self):
        form = AddArticleForm()
        categories = list()
        tags = list()
        users = list()
        try:
            categories = Category.query.order_by(Category.id.asc()).all()
            tags = Tag.query.order_by(Tag.id.asc()).all()
            users = User.query.all()
        except Exception as e:
            current_app.logger.error(e)
            abort(500)

        user_list = list()
        for user in users:
            user_list.append((user.id, user.nick_name))

        form.author.choices += user_list

        category_list = list()
        for category in categories:
            category_list.append((category.id, category.name))

        form.category.choices += category_list

        tag_list = list()
        for tag in tags:
            tag_list.append((tag.id, tag.name))

        form.tag.choices += tag_list

        form.author.choices += user_list

        return self.render('/admin/article.html', form=form)
