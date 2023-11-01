import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tạo server từ socket
server.bind(('127.0.0.1', 12345)) # ip là 127.0.0.1 port là: 12345
server.listen(1) # cho nó lắng nghe việc gửi dữ liệu từ client
print("Server is listening on port 12345...")
try:
    while True: # cho nó luôn luôn chạy
        conn, addr = server.accept() # Chấp nhận kết nối từ máy khách và lưu đối tượng kết nối trong biến conn và địa chỉ của máy khách trong biến addr.
        data = conn.recv(1024) # Đọc dữ liệu từ máy khách thông qua đối tượng kết nối conn và lưu vào biến data với dung lượng tối đa là 1024 byte
        print(f"Data: {data.decode()}") # ban đầu là kiểu byte cho nó sang string
        conn.close() # đóng nó
except KeyboardInterrupt: # bắt ngoại lệ in ra dòng dưới
    print("Ctrl+C Out")

