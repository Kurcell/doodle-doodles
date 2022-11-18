from flask import Blueprint, jsonify, request
from ..models.models import Doodle
from ..__init__ import db

doodle_bp = Blueprint('doodles', __name__)

@doodle_bp.route("/", methods=['GET'])
def hello():
    return "Welcome to Just a Doodle's Doodle API!"

@doodle_bp.route("/doodle/<int:id>", methods=['GET'])
def readOne(id):
    return jsonify(Doodle.query.filter_by(id = id).one())

@doodle_bp.route("/doodles", methods=['GET'])
def readMany():
    return jsonify(Doodle.query.all())

@doodle_bp.route("/doodle", methods=['POST'])
def create():
    req = request.get_json()
    return jsonify(Doodle.create(req['instructions']))

@doodle_bp.route("/doodle/<int:id>", methods=['PUT'])
def update(id):
    req = request.get_json()
    return jsonify(Doodle.update(id, req['instructions']))

@doodle_bp.route("/doodle/<int:id>", methods=['DELETE'])
def delete(id):
    return jsonify(Doodle.delete(id))
