import pyodbc

def connect():
    server = 'localhost'
    database = 'esenVerde'

    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=yes;')
    
    return conn

def executeQuery(query):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close() 

query = "SELECT * FROM dbo.ProcessXCountryPrices ORDER BY id"
data = executeQuery(query)

# print("ID: " + str(data[0][0]))
# print("Name: " + data[0][1])
# print("Description: " + data[0][2])
# print("Country: " + data[0][3])
# print("Price: " + str(data[0][4]))
# print("Type: " + data[0][5])

