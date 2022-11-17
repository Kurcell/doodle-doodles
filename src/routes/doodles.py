from flask import Blueprint, jsonify
from ..models.models import Doodle

doodle_bp = Blueprint('doodles', __name__)

@doodle_bp.route("/doodles", methods=['GET'])
def read():
    return jsonify(Doodle.query.all())
