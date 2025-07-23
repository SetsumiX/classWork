import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(5)
print("Сервер запущен, ожидается подключение")

clients = []
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                remove_client(client_socket)
                break
            print(f"Сообщение отправлено из {client_address}: {message}")
            broadcast(message, client_socket)
        except:
            remove_client(client_socket)
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключён новый клиент - {client_address}")
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.daemon = True
    client_thread.start()