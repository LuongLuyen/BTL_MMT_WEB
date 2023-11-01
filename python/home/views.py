from django.shortcuts import render
from .models import User, Card
from django.contrib.auth import logout
import socket
def sendSocket(data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))  
    client.send(data)
    client.close()

def getHome(request):
    if request.method == 'POST':
        stkn = request.POST.get('stkn') 
        ck = request.POST.get('ck') 
        ndck = request.POST.get('ndck') 
        bank = request.POST.get('bank')
        idUser =  request.session['user_id']
        name =  request.session['name']

        if(stkn!=None and ck!=None and ndck!=None ):
            card = Card.objects.get(userid=idUser)
            card.sd = '{:,}'.format(int(card.sd)).replace(',', '.')
            try:
                tkNhan = Card.objects.get(stk=stkn) 
                tkChuyen = Card.objects.get(userid=idUser)
                tkChuyen.sd = tkChuyen.sd - int(ck)
                tkNhan.sd = tkNhan.sd +int(ck)
                tkChuyen.save()
                tkNhan.save()
                card = Card.objects.get(userid=idUser)
                card.sd = '{:,}'.format(int(card.sd)).replace(',', '.')
                text = stkn+" + "+ck+" + "+ndck
                encoded_text = text.encode("utf-8")
                data = bytes(encoded_text)
                sendSocket(data)
                return render(request, 'pages/home.html', {'card': card, 'name': name})
            except:
                return render(request, 'pages/home.html', {'card': card, 'name': name})
            
    return render(request, 'pages/home.html')

def getLogin(request):
    if request.method == 'POST':
        userName = request.POST.get('userName') 
        password = request.POST.get('password') 
        lo = request.POST.get('logout') 
        try:
            userDB = User.objects.get(userName=userName)
            passDB = User.objects.get(password=password)
            if(userDB!=None and passDB!=None):
                request.session['user_id'] = userDB.id
                request.session['name'] = str(userDB.name)
                name =  request.session['name']
                idUser =  request.session['user_id']
                card = Card.objects.get(userid=idUser)
                card.sd = '{:,}'.format(int(card.sd)).replace(',', '.')
                return render(request, 'pages/home.html', {'card': card, 'name': name})
        except:
            return render(request, 'pages/Login.html')
        if(lo=="logout"):
            if 'user_id' in request.session:
                del request.session['user_id']
                request.session.pop('name', None)
            logout(request)
        
            return render(request, 'pages/Login.html')
    else:
        return render(request, 'pages/Login.html')

