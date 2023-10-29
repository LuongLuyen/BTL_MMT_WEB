import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345)) 
server.listen(1)
print("Server is listening on port 12345...")
try:
    while True:
        conn, addr = server.accept()
        data = conn.recv(1024)
        print(f"Data: {data.decode()}")
        datas = "Hello, Client!"
        conn.send(datas.encode())
        conn.close()
except KeyboardInterrupt:
    print("Ctrl+C detected. Server terminated.")

