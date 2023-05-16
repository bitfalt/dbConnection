from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

# Replace with your SQL Server connection details
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=esenVerde;'
    r'UID=user;'
    r'PWD=123456'
)

containerList = []
wasteList = []

def getMovementTypeID():
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT movementtype FROM dbo.MovementTypes WHERE name = 'Exchange'")
        row = cursor.fetchone()
        
        if row is not None:
            return row.movementtype
        else:
            return None

def addContainersTVP():

    global containerList

    with pyodbc.connect(conn_str) as conn:
    # Preparar el TVP y crear el cursor
        containerTVP = []
        cursor = conn.cursor()

        # Iterar sobre la lista de contenedores y agregarlos al TVP
        for container in containerList:
            containerName = container[0]
            containerNumber = container[1]
            # Obtener el id del contenedor
            cursor.execute("SELECT containerid FROM dbo.Containers WHERE name = ?", containerName)
            row = cursor.fetchone()
            # Insertarlo en el TVP
            if row is not None:
                containerID = row.containerid
                containerTVP.append((containerID, containerNumber))
    
    return containerTVP

def addWasteTypeTVP():

    global wasteList

    with pyodbc.connect(conn_str) as conn:
    # Preparar el TVP y crear el cursor
        wasteTVP = []
        cursor = conn.cursor()

        # Iterar sobre la lista de desechos y agregarlos al TVP
        for waste in wasteList:
            wasteName = waste[0]
            wasteNumber = waste[1]
            # Obtener el id del desecho
            cursor.execute("SELECT wastetypeid FROM dbo.WasteTypes WHERE name = ?", wasteName)
            row = cursor.fetchone()
            # Insertarlo en el TVP
            if row is not None:
                wasteID = row.wastetypeid
                wasteTVP.append((wasteID, wasteNumber))
    
    return wasteTVP

@app.route('/waste-types', methods=['GET'])
def getWasteTypes():
    WOPTIONS = []
    data = []
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM dbo.WasteTypes")
        rows = cursor.fetchall()
        for row in rows:
            WOPTIONS.append(row.name.strip())
    
    for waste in WOPTIONS:
        data.append({"name": waste})
    
    return jsonify(data)


@app.route('/container-names', methods=['GET'])
def getContainerNames():
    COPTIONS = []
    data = []
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM dbo.Containers")
        rows = cursor.fetchall()
        for row in rows:
            COPTIONS.append(row.name.strip())
    
    for container in COPTIONS:
        data.append({"name": container})

    return jsonify(data)


@app.route('/submit-containers', methods=['POST'])
def postContainers():
    global containerList
    try:
        data = request.json

        for container in data:
            result = []
            result.append(container["name"])
            result.append(container["number"])
            containerList.append(result)

        return jsonify({"Status": "Success", "Message": "Containers added successfully"}), 200
    
    except Exception as e:
        return jsonify({"Status": "Error", "Message": str(e)}), 400

@app.route('/submit-waste-types', methods=['POST'])
def postWasteTypes():
    global wasteList
    try:
        data = request.json

        for waste in data:
            result = []
            result.append(waste["type"])
            result.append(waste["number"])
            wasteList.append(result)

        return jsonify({"Status": "Success", "Message": "Waste types added successfully"}), 200
    
    except Exception as e:
        return jsonify({"Status": "Error", "Message": str(e)}), 400

@app.route('/test-lists', methods=['GET'])
def testLists():
    global containerList
    global wasteList
    return jsonify({"Status": "Success", "Message": "Lists created successfully", "Containers": containerList, "WasteTypes": wasteList}), 200

@app.route('/test-tvp', methods=['GET'])
def testTVP():
    containerTVP = addContainersTVP()
    wasteTVP = addWasteTypeTVP()
    return jsonify({"Status": "Success", "Message": "TVPs created successfully", "Containers": containerTVP, "WasteTypes": wasteTVP}), 200

@app.route('/execute-sp', methods=['GET'])
def executeStoredProcedure():
    with pyodbc.connect(conn_str) as conn:
        try:
            cursor = conn.cursor()
            containerTVP = (addContainersTVP())
            wastetypeTVP = (addWasteTypeTVP())
            movtypeid = getMovementTypeID()
            cursor.execute("EXECUTE dbo.exchangeContainer @containersTVP = ?, @wastetypeTVP = ?, @movtypeid = ?", containerTVP, wastetypeTVP ,movtypeid)
            conn.commit()
            return jsonify({"Status": "Success", "Message": "Stored Procedure executed successfully"}), 200
        
        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            return jsonify({"Status": "Error", "Message": str(ex), "SQLState": sqlstate}), 400
        
if __name__ == '__main__':
    app.run(debug=True)
