..repositories import collector_repository

def getCollectorsByCountryORM(countryName): 
    collectors = collector_repository.get_collectors_by_country(countryName)
    result = [collector.name for collector in collectors]
    return result
