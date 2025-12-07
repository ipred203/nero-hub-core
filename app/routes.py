from fkask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({
        "status": "nero hub is running",
        "mode": "development"
    })