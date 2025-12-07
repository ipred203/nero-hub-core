from config import Config
from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify({
        "status": f"{Config.APP_NAME} is running",
        "mode": "Dev"
    })
