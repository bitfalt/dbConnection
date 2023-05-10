from repositories.collectorCountry_repository import getCollectorCountry

def getCollectorByCountry(pool, country):
    return getCollectorCountry(pool, country)
