from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello():
    return 'Hello from python!'

@bp.route('/')
def index():
    return 'python index'