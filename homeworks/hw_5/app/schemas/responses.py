from app.models import db

class Response(db.Model):
    __tablename__ = 'response'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    # text = db.Column(db.Text, nullable=False)
    questions = db.relationship("Question", backref="response", lazy='joined')
    is_agree = db.Column(db.Boolean, nullable=False)


