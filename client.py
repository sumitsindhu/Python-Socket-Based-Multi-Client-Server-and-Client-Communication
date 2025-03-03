import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Server says: {message.decode()}")
            else:
                break
        except:
            break


def connect_to_server():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    while True:
        message = input("Enter message to send to the server (type 'exit' to quit): ")
        if message.lower() == 'exit':
            client_socket.close()
            break
        client_socket.send(message.encode())

if __name__ == "__main__":
    connect_to_server()
