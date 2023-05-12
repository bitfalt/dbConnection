from flask import Blueprint, jsonify, request
from app.controllers import collectorCountry_controller

# Create blueprint (route)
bp = Blueprint('collectorCountryPool', __name__, url_prefix='/collectorCountryPool')

@bp.route('/', methods=['POST', "GET"])

def getCollectorByCountryPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = collectorCountry_controller.getCollectorCountry(True, country)
    return jsonify(result)
