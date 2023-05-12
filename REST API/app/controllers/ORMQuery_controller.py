from app.repositories import ORMQuery_repository

def getCollectorsByCountryORM(countryName): 
    return ORMQuery_repository.getCollectorsByCountryORM(countryName)

