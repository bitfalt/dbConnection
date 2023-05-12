from app.repositories.collectorCountry_repository import getCollectorCountry
# Controller se encarga de la logica de los datos
# Llama a la funcion de repository que se encarga de la conexion con la base de datos y la consulta
def getCollectorByCountry(pool, country):
    return getCollectorCountry(pool, country)
