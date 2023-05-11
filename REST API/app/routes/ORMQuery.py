from flask import Blueprint, jsonify
from ..controllers import collector_controller

bp = Blueprint('ORMQuery', _name_, url_prefix="/ORMQuery")

@bp.route("/", methods=["POST"])
def getCollectorsByCountryORM():
    countryName = request.json["country"]
    result = collector_controller.get_collectors_by_country(countryName)
    return jsonify(result)
