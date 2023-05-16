from flask import Blueprint, jsonify, request
from app.controllers import ORMQuery_controller

# Create blueprint (route)
bp = Blueprint('ORMQuery', __name__, url_prefix="/ORMQuery")

# Definir ruta y metodos de la misma
# bp.route define la ruta dada en Blueprint()
@bp.route("/", methods=["POST"])
def getCollectorsByCountryORM():
    # Get country from request
    countryName = request.json["country"]
    # Get result from request
    result = ORMQuery_controller.getCollectorsByCountryORM(countryName)
    
    return jsonify(result)
