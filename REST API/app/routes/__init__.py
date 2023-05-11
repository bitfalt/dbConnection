from flask import Flask
from . import collectorCountryPool, collectorCountryNoPool, ORMQuery

def registerBlueprints(app: Flask):
    app.register_blueprint(collectorCountryPool.bp)
    app.register_blueprint(collectorCountryNoPool.bp)
    app.register_blueprint(ORMQuery.bp)
