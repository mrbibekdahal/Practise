import socket

target = input("Enter target IP: ")

for port in range(20,101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,port))

    if result == 0:
     print(f"port {port} is open")
    s.close()