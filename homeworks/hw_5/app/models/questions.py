from app.models import db
from sqlalchemy import Column


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    category_id = Column(db.Integer, db.ForeignKey('category.id'))
    text = db.Column(db.Text, nullable=False)
    responses = db.relationship("Response", backref="question", lazy='joined')



class Statistics(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    agree_count = db.Column(db.Integer, default=0)
    disagree_count = db.Column(db.Integer, default=0)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)