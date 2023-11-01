from django.shortcuts import render
from .models import User, Card
from django.contrib.auth import logout
import socket
def sendSocket(data): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tạo kết nối bên client
    client.connect(('127.0.0.1', 12345))  # kết nối vào đúng ip và port bên server lưy ý:(máy chủ web chạy port 8000)
    client.send(data) # gửi thông tin chuyển khoản lên server
    client.close() # đóng

def getHome(request): 
    if request.method == 'POST':  # nếu là submit form
        stkn = request.POST.get('stkn')  # số tài khoản người nhận (nhập vào từ giao diện)
        ck = request.POST.get('ck')  # số tiền chuyển (nhập vào từ giao diện)
        ndck = request.POST.get('ndck') # nội dung chuyển khoản (nhập vào từ giao diện)
        bank = request.POST.get('bank') # các loại ngân hàng (ddinh làm nhưng khó quá bỏ qua)
        idUser =  request.session['user_id'] # lấy id người dùng đăng nhập ra
        name =  request.session['name'] # tương tự

        if(stkn!=None and ck!=None and ndck!=None ): # nếu như đủ thông tin
            card = Card.objects.get(userid=idUser) # lấy ra thẻ của người đang đăng nhập (sài cho thằng dòng 38)
            card.sd = '{:,}'.format(int(card.sd)).replace(',', '.') # format số dư thêm đấu . vào trước 3 số 0 ví dụ 10000 bằng 100.000
            try:
                tkNhan = Card.objects.get(stk=stkn) # lấy ra tài khoản nhận tiền
                tkChuyen = Card.objects.get(userid=idUser) # lấy ra tài khoản chuyển tiền
                tkChuyen.sd = tkChuyen.sd - int(ck) # số dư người chuyển sẽ bằng số dư ban đầu - số tiền chuyển
                tkNhan.sd = tkNhan.sd +int(ck) # ngược lại thì sẽ cộng vào
                tkChuyen.save() # lưu lại
                tkNhan.save() # lưu lại
                card = Card.objects.get(userid=idUser) # lấy ra thẻ của người đang đăng nhập (sài cho thằng dòng 336)
                card.sd = '{:,}'.format(int(card.sd)).replace(',', '.') # # format số dư thêm đấu . vào trước 3 số 0 ví dụ 10000 bằng 100.000
                text = " Tk huong thu: "+stkn+" + So tien: "+ck+" + noi dung: "+ndck # nội dung giao dịch chuyển sang 1 string
                encoded_text = text.encode("utf-8") # ép nó sang utf-8
                data = bytes(encoded_text) # ép nó sang kiểu byte
                sendSocket(data) # gọi đến hàm gửi thông tin giao dịch  lên server
                return render(request, 'pages/home.html', {'card': card, 'name': name}) # trar về trang home và data cần thiết để hiển thị
            except:
                return render(request, 'pages/home.html', {'card': card, 'name': name}) # trar về trang home và data cần thiết để hiển thị (nhập thiếu dữ liệu ở giao giện người dùng nó sẽ không sendSocket và ko thay đổi giao dịch)
            
    return render(request, 'pages/home.html') # mặc định trả vwf trang home

def getLogin(request):
    if request.method == 'POST': # nếu là submit form
        userName = request.POST.get('userName') #lấy tên đăng nhập từ form
        password = request.POST.get('password') #lấy mật khẩu nhập từ form
        lo = request.POST.get('logout')  # thoát
        try:
            userDB = User.objects.get(userName=userName) # so sánh nhập vào == nguoi dùng DB hay không
            passDB = User.objects.get(password=password) # tương tự
            if(userDB!=None and passDB!=None):
                request.session['user_id'] = userDB.id # đăng nhập thành công lưu id vào session
                request.session['name'] = str(userDB.name) # tương tự
                name =  request.session['name'] # lấy tên trong session ra dùng
                idUser =  request.session['user_id'] # tương tự
                card = Card.objects.get(userid=idUser) # lấy thẻ ngân hàng theo id người dùng lúc nãy đăng nhập
                card.sd = '{:,}'.format(int(card.sd)).replace(',', '.') # format số dư thêm đấu . vào trước 3 số 0 ví dụ 10000 bằng 100.000
                return render(request, 'pages/home.html', {'card': card, 'name': name}) # trả về giao diện home và có các data gồm (thẻ ngân hàng và tên chủ thẻ)
        except:
            return render(request, 'pages/Login.html') # nhập tk mk sai không đúng trả về trang login
        if(lo=="logout"): # nếu là thoát
            if 'user_id' in request.session:
                del request.session['user_id'] # xóa id người dùng
                request.session.pop('name', None) # xóa tên người dùng
            logout(request) # trả cái request đó về giao giiện để thông báo cho trình duyệt là đã đăng xuất
        
            return render(request, 'pages/Login.html') # trả về trang login
    else: # get giao diện login
        return render(request, 'pages/Login.html') # trả về giao diện login

