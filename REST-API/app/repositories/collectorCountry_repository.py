from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool

# Crear la conexion con el servidor de base de datos
username = "user"
password = "123456"
server = "localhost"
port = "1433"
db = "esenVerde"
driver = "ODBC Driver 17 for SQL Server"

# Crear 2 engines, uno con pool y otro sin pool
poolEngine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}:{port}/{db}?driver={driver}", pool_size=5, max_overflow=5)
noPoolEngine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}:{port}/{db}?driver={driver}", poolclass=NullPool)


# Ejecutar un query (SP) en la base de datos con parametros
def getCollectorCountry(pool, country):
    # Si pool es True, usar el engine con pool, sino usar el engine sin pool
    if pool:
        engine = poolEngine
    else:
        engine = noPoolEngine

    param = country
    query = text("EXEC CollectorsByCountryFiltered :param")
    with engine.connect() as connection:
        result = connection.execute(query, {"param": param})
        # Convertir el resultado a una lista con diccionarios
        keys = result.keys()
        resultDict = [dict(zip(keys, row)) for row in result.fetchall()]
        connection.close()
        return resultDict