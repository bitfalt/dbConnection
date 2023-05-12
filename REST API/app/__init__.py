from flask import Flask
from app.routes import registerBlueprints
# from app.repositories.models import db

def createApp():
    app = Flask(__name__)
    # Register blueprints (routes)
    registerBlueprints(app)
    return app