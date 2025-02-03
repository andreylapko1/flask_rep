from flask import Blueprint
responses_bp = Blueprint('responses', __name__, url_prefix='/responses')



@responses_bp.route('/', methods=['POST'])
def add_response():
    return 'Response added'