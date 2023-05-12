from sqlalchemy import Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy

# Declaracion de las tablas como objetos para el ORM y realizar las consultas
db = SQLAlchemy()

class Collector(db.Model): 
    __tablename__ = "Collectors"
    collectorid  = Column(Integer, primary_key=True)
    name = Column(String(30))

class Office(db.Model):
    __tablename__ = "Offices"
    officeid = Column(Integer, primary_key=True)
    name = Column(String(30))
    addressid = Column(Integer, ForeignKey("Addresses.addressid"))
    collectorid = Column(Integer, ForeignKey("Collectors.collectorid"))

class Address(db.Model):
    __tablename__ = "Addresses"
    addressid = Column(Integer, primary_key=True)
    city = Column(String(30))
    street = Column(String(80))
    postalCode = Column(String(20))
    countryid = Column(Integer, ForeignKey("Country.countryid"))

class Country(db.Model):
    __tablename__ = "Country"
    countryid = Column(Integer, primary_key=True)
    name = Column(String(30))
