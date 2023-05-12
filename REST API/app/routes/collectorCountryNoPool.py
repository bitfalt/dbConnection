from flask import Blueprint, jsonify, request
from app.controllers import collectorCountry_controller

# Create blueprint (route)
bp = Blueprint('collectorCountryNoPool', __name__, url_prefix='/collectorCountryNoPool')

# Definir ruta y metodos de la misma
# bp.route define la ruta dada en Blueprint()
@bp.route('/', methods=['POST'])
def getCollectorByCountryNoPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = collectorCountry_controller.getCollectorByCountry(False, country)
    
    return jsonify(result)