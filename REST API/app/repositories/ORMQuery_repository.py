from app.repositories.models import db, Collector, Office, Address, Country
from app.repositories.collectorCountry_repository import createConnection
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

# Obtener los colectores de un pais usando ORM
def getCollectorsByCountryORM(countryName):

    engine = createConnection(False)
    Session = sessionmaker(bind=engine)
    session = Session()
 
    query = select(Collector.name).select_from(Collector).join(Office).join(Address).join(Country).where(Country.name == countryName)
    result = session.execute(query)

    # Crear lista vacia
    resultDict = []

    # Recorrer el resultado y agregarlo a la lista como diccionario para JSON
    for res in result:
        # Se crea el diccionario con el nombre. 
        # "name" es el nombre de la columna en la tabla y res[0] el valor
        resultDict.append({"name": res[0]})

    return resultDict
