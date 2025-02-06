from app.models import db



class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    text = db.Column(db.Text, nullable=False)
    responses = db.relationship("Response", backref="question", lazy='joined')


class Statistic(db.Model):
    __tablename__ = 'statistic'
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    agree_count = db.Column(db.Integer, nullable=False, default=0)
    disagree_count = db.Column(db.Integer, nullable=False, default=0)



class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)