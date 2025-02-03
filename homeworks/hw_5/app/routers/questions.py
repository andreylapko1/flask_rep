from flask import Blueprint

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_list_questions():
    return "Список вопросов"


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return f"Вопрос: {question_id}"
