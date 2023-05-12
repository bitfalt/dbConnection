from ..repositories import ORMQuery_repository

def getCollectorsByCountryORM(countryName): 
    collectors = ORMQuery_repository.getCollectorsByCountryORM(countryName)
    result = [collector.name for collector in collectors]
    return result
