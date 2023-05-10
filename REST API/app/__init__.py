from flask import Flask
from .routes import registerBlueprints

def createApp():
    app = Flask(__name__)
    # Register blueprints (routes)
    registerBlueprints(app)
    return app