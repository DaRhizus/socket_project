import socket
import threading

def handle_client(client_socket, addr):
    print('Bağlantı alındı:', addr)

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Alınan veri:", data)

        reply = input("Cevap vermek istediğiniz mesajı girin -> ")
        client_socket.sendall(bytes(reply, 'utf-8'))

    print('Bağlantı kapatıldı:', addr)
    client_socket.close()

def start_server():
    s = socket.socket()
    port = 12345
    s.bind(('', port))
    s.listen(5)
    print("Soket dinleme modunda")

    while True:
        c, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(c, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
