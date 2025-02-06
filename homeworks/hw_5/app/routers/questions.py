from flask import Blueprint, jsonify, request
from app.models.questions import Question
import pandas as pd
from app.models import db
from app.schemas.questions import CreateQuestion, ResponseQuestion, MessageResponse


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    questions_data = [ResponseQuestion.model_validate(q).model_dump() for q in questions]
    return pd.DataFrame(questions_data).to_html()
    # return jsonify(questions_data)


@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'message': 'No text provided'}), 400
    question = Question(text=data['text'])
    db.session.add(question)
    db.session.commit()
    return jsonify({'message': 'Answer create', 'id': question.id}), 201

@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = Question.query.get(question_id)
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    return jsonify({'message': f'Question found: {question.text}'}), 200


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    question = Question.query.get(question_id)
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    data = request.get_json()
    question.text = data['question_text']
    db.session.commit()
    return jsonify({'message': f'Question with id {question.id} was update: {question.text}'}), 200

@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question = Question.query.get(question_id)
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': f'Answer with id: {question.id} deleted'}), 200

