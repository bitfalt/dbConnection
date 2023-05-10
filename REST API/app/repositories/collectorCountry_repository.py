from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool

def createConnection(pool):
    username = "user"
    password = "123456"
    server = "localhost"
    database = "esenVerde"
    driver = "ODBC Driver 17 for SQL Server"
    if pool:
        engine = create_engine(f"mssql+pyodbc://user:123456@localhost:1433/esenVerde?driver={driver}", pool_size=10, max_overflow=0)
    else:
        engine = create_engine(f"mssql+pyodbc://user:123456@localhost:1433/esenVerde?driver={driver}", poolclass=NullPool)
    return engine

def getCollectorCountry(pool, country):
    engine = createConnection(pool)
    param = country
    query = text("EXEC CollectorsByCountryFiltered :param")
    with engine.connect() as connection:
        result = connection.execute(query, {"param": param})

        keys = result.keys()
        resultDict = [dict(zip(keys, row)) for row in result.fetchall()]

        return resultDict