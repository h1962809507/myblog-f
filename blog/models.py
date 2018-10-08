from werkzeug.security import generate_password_hash, check_password_hash
from blog import db
from datetime import datetime


class User(db.Model):
    """用户（管理员）"""
    __tablename__ = "user"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 用户id，主键
    num = db.Column(db.String(24), unique=True, nullable=False)  # 帐号
    nick_name = db.Column(db.String(64), unique=True, nullable=False)  # 用户名
    password_hash = db.Column(db.String(128), nullable=False)  # 加密后的密码
    avatar_url = db.Column(db.String(256))  # 头像的url地址

    article = db.relationship("Article", backref='user', lazy="dynamic")

    @property
    def password(self):
        # 密码
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        # 设置（加密）密码
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        # 验证密码
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return self.nick_name


class Category(db.Model):
    """分类"""
    __tablename__ = "category"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(64), unique=True, nullable=False)  # 名称

    article = db.relationship("Article", backref='category', lazy="dynamic")

    def __repr__(self):
        return self.name


class Tag(db.Model):
    """标签"""
    __tablename__ = "tag"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(64), unique=True, nullable=False)  # 名称

    article = db.relationship("Article", backref='tag', lazy="dynamic")

    def __repr__(self):
        return self.name


class Article(db.Model):
    """文章模型"""
    __tablename__ = "article"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id
    title = db.Column(db.String(256), nullable=False)  # 标题
    digest = db.Column(db.String(512), nullable=False)  # 摘要
    cover_url = db.Column(db.String(256), nullable=False)  # 封面图
    content = db.Column(db.Text, nullable=False)  # 内容
    author = db.Column(db.Integer, db.ForeignKey("user.id"))  # 作者
    click = db.Column(db.Integer, default=0)  # 阅读量
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))  # 分类
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 标签
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    comment = db.relationship("Comment", backref='article', lazy="dynamic")

    def __repr__(self):
        return self.title


class Comment(db.Model):
    """评论"""
    __tablename__ = "comment"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 评论id 主键
    content = db.Column(db.Text, nullable=False)  # 评论内容 不允许为空
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))  # 评论文章的id 外键
    parent_id = db.Column(db.Integer, db.ForeignKey("comment.id"))  # 父评论id 自关联外键
    nick_name = db.Column(db.String(64), unique=True, nullable=False)  # 用户名，不允许重复为空
    email = db.Column(db.String(48), nullable=True)  # 邮箱
    url = db.Column(db.String(48), nullable=True, default="#")  # 网址
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间

    def __repr__(self):
        return self.content
