import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Listening...")

while True:

    client, addr = server.accept()

    print(addr)

    request = client.recv(1024)

    print(request.decode())

    response = """HTTP/1.1 200 OK

Hello World there
"""

    client.send(response.encode())

    client.close()