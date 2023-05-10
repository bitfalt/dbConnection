from flask import Blueprint, jsonify, request
from repositories.collectorCountry_repository import getCollectorCountry

# Create blueprint (route)
bp = Blueprint('collectorCountryPool', __name__, url_prefix='/collectorCountryPool')

@bp.route('/', methods=['POST'])

def getCollectorByCountryPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = getCollectorCountry(True, country)
    return jsonify([dict(row) for row in result])
