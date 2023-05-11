from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create engine and session
engine = create_engine('mysql+pymysql://user:123456@localhost/esenVerde')
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Collector(Base): 
    __tablename__ = "Collectors"
    collectorid  = Column(Integer, primary_key=True)
    name = Column(String(30))

class Office(Base):
    __tablename__ = "Offices"
    officeid = Column(Integer, primary_key=True)
    name = Column(String(30))
    addressid = Column(Integer, ForeignKey("Addresses.addressid"))
    collectorid = Column(Integer, ForeignKey("Collectors.collectorid"))

class Address(Base):
    __tablename__ = "Addresses"
    addressid = Column(Integer, primary_key=True)
    city = Column(String(30))
    street = Column(String(80))
    postalCode = Column(String(20))
    countryid = Column(Integer, ForeignKey("Countries.countryid"))

class Country(Base):
    __tablename__ = "Countries"
    countryid = Column(Integer, primary_key=True)
    name = Column(String(30))


# create tables
Base.metadata.create_all(engine)

