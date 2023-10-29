import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))  

data = b"Hello, Server!"
md5_hash = hashlib.md5(data).hexdigest()

print(f"Sending data: {data}")
print(f"MD5 hash: {md5_hash}")
client.send(data)

client.close()
