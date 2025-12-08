from flask import Blueprint
from config import Config

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return f"{Config.APP_NAME} API is running!"
