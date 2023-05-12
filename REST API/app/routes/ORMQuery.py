from flask import Blueprint, jsonify, request
from app.controllers import ORMQuery_controller

bp = Blueprint('ORMQuery', __name__, url_prefix="/ORMQuery")

@bp.route("/", methods=["POST"])
def getCollectorsByCountryORM():
    countryName = request.json["country"]
    result = ORMQuery_controller.getCollectorsByCountryORM(countryName)
    return jsonify(result)
