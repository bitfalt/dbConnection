import socket
import json
import struct

def receiveData(sock):
    # First receive the size of the data
    sizeData = sock.recv(4)
    size = struct.unpack('!I', sizeData)[0]
    # Now receive the data
    data = b''
    while len(data) < size:
        chunk = sock.recv(1024)
        if not chunk:
            break
        data += chunk
    # Decode the data
    return json.loads(data.decode())

# Create and connect the socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 12345))

try:
    while True:
        # Send the query
        # Initialize query as "", if query != "" send query else continue loop
        query = "SELECT * FROM dbo.ProcessXCountryPrices ORDER BY id"
        clientSocket.send(query.encode())

        # Receive and process the data
        data = receiveData(clientSocket)
        print(f"Result from server: {data}")
except KeyboardInterrupt:
    print("Closing client socket...")
    clientSocket.close()
except Exception as e:
    print(f"An error occurred: {e}")
    clientSocket.close()
