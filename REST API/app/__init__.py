from flask import Flask
from .routes import registerBlueprints
from .repositories import db

def createApp():
    app = Flask(__name__)
    driver = "ODBC Driver 17 for SQL Server"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mssql+pyodbc://user:123456@localhost:1433/esenVerde?driver={driver}"
    db.init_app(app)
    # Register blueprints (routes)
    registerBlueprints(app)
    return app