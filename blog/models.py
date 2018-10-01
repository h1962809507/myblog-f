from blog import db
from datetime import datetime


class Post(db.Model):
    """文章模型"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
