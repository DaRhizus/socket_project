import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

while True:
    input_string = input("Göndermek istediğiniz veriyi girin -> ")
    s.sendall(bytes(input_string, 'utf-8'))

    if input_string.lower() == 'exit':
        break

    received_data = s.recv(1024).decode()
    print("Sunucudan gelen cevap:", received_data)

s.close()
