from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify({"status": "Nero Hub is running", "mode": "Dev"})
