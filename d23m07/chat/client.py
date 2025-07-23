import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12345)
client_socket.connect(server_address)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Соединение с сервером разорвано")
            client_socket.close()
            break

def send_message():
    while True:
        message = input()
        if message.lower() == "exit":
            client_socket.close()
        try:
            client_socket.send(message.encode("utf-8"))
        except:
            print("Не удалось отправить сообщение")
            break

receive_tread = threading.Thread(target=receive_messages)
receive_tread.daemon = True
receive_tread.start()

sand_threa = threading.Thread(target=send_message)
sand_threa.daemon = True
sand_threa.start()

receive_tread.join()
sand_threa.join()