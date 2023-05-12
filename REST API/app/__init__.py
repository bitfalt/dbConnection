from flask import Flask
from app.routes import registerBlueprints

# Crea la app de Flask
def createApp():
    app = Flask(__name__)
    # Register blueprints (routes)
    registerBlueprints(app)
    return app