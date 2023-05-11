from models import db 
from models import Collectors, Offices, Addresses, Country 
from sqlalchemy.orm import joinedload

def getCollectorsByCountryORM(countryName): 
    collectors = db.session.query(Collectors).\
        join(Offices, Collectors.collectorid == Offices.collectorid).\
        join(Addresses, Offices.addressid == Addresses.addressid).\
        join(Country, Addresses.countryid == Country.countryid).\
        options(joinedload(Collectors.offices).joinedload(Offices.addresses).joinedload(Addresses.country)).\
        filter(Country.name == countryName).\
        all()
    return collectors
