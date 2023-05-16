from flask import Flask
from app.routes import collectorCountryPool, collectorCountryNoPool, ORMQuery

# Registra las rutas en la aplicacion, definidas en los blueprints
def registerBlueprints(app: Flask):
    app.register_blueprint(collectorCountryPool.bp)
    app.register_blueprint(collectorCountryNoPool.bp)
    app.register_blueprint(ORMQuery.bp)
