from app.repositories import ORMQuery_repository
# Controller se encarga de la logica de los datos
# Llama a la funcion de repository que se encarga de la conexion con la base de datos y la consulta
def getCollectorsByCountryORM(countryName): 
    return ORMQuery_repository.getCollectorsByCountryORM(countryName)

