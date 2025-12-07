from flask import Blueprint, jsonify
from config import Config

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify({
        "status": f"{Config.APP_NAME} is running",
        "mode": "Dev"
    })
