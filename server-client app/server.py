import socket
import json
import struct

from dbtest import executeQuery


def parseData(data):

    parsedData = []

    for row in data:
        row = [row[1].strip(), row[3].strip(), str(row[4]), row[5].strip()]
        parsedData.append(row)

    return parsedData



def sendData(data):
    jsonData = json.dumps(data)
    print(jsonData)
    # Send the size of the data first
    size = struct.pack('!I', len(jsonData))
    clientSocket.send(size)
    # Now send the data
    clientSocket.send(jsonData.encode())



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 12345))
print("Server is listening")
serverSocket.listen(1)

while True:
    clientSocket, clientAddress = serverSocket.accept()
    print(f"Client connected: {clientAddress}")
    
    request = clientSocket.recv(1024).decode()
    print(f"Received query: {request}")
    # Use the executeQuery function to get the result
    result = executeQuery(request)
    # Parse the result
    parsedData = parseData(result)
    print("Now sending data")
    # Send the parsed result to the client
    sendData(parsedData)
    print("Finished sending data")

    




serverSocket.close()