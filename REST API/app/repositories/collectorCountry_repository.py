from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool

def createConnection(pool):
    if pool:
        engine = create_engine("mysql+pymysql://user:123456@localhost:3306/esenVerde", pool_size=10, max_overflow=0)
    else:
        engine = create_engine("mysql+pymysql://user:123456@localhost:3306/esenVerde", poolclass=NullPool)

    return engine

def getCollectorCountry(pool, country):
    engine = createConnection(pool)
    param = country
    query = text("EXEC CollectorsByCountryFiltered :param")
    with engine.connect() as connection:
        result = connection.execute(query, params={"param": param})
        return result.fetchall()