from flask import Blueprint, jsonify, request
from repositories.collectorCountry_repository import getCollectorCountry

# Create blueprint (route)
bp = Blueprint('collectorCountryNoPool', __name__, url_prefix='/collectorCountryNoPool')

@bp.route('/', methods=['POST'])
def getCollectorByCountryNoPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = getCollectorCountry(False, country)
    return jsonify([dict(row) for row in result])