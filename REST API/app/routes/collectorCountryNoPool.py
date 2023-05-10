from flask import Blueprint, jsonify, request
from ..controllers import collectorCountry_controller

# Create blueprint (route)
bp = Blueprint('collectorCountryNoPool', __name__, url_prefix='/collectorCountryNoPool')

@bp.route('/', methods=['POST'])
def getCollectorByCountryNoPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = collectorCountry_controller.getCollectorByCountry(False, country)
    return jsonify([dict(row) for row in result])