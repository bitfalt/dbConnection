from flask import Blueprint, jsonify, request
from repositories import collectorCountry_repository

# Create blueprint (route)
bp = Blueprint('collectorCountryPool', __name__, url_prefix='/collectorCountryPool')

@bp.route('/', methods=['POST'])

def getCollectorByCountryPool():
    # Get country from request
    country = request.json['country']
    # Get result from request
    result = collectorCountry_repository.getCollectorCountry(True, country)
    return jsonify([dict(row) for row in result])
