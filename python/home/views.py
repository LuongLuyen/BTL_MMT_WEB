from django.shortcuts import render
import socket
def sendSocket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))  
    data = b"Hello, Server!"
    client.send(data)
    data = client.recv(1024)
    print("Data", data.decode())
    client.close()

def getHome(request):
    return render(request, 'pages/home.html')
def getLogin(request):
    # sendSocket()
    return render(request, 'pages/Login.html')
