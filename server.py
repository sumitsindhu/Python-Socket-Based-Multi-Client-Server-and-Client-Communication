import socket
import threading

# List to store all client connections
clients = []

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    try:
        client_socket.send("Welcome to the server!".encode())

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received from {client_address}: {message.decode()}")
            
            # For example: If a client sends 'trigger', the server will trigger an event
            if message.decode().lower() == 'trigger':
                trigger_event()

    except Exception as e:
        print(f"Error with {client_address}: {e}")

    finally:
        # Close the client socket and remove from clients list
        client_socket.close()
        clients.remove(client_socket)
        print(f"Connection closed with {client_address}")

# Function to trigger an event and send a message to all clients
def trigger_event():
    event_message = "An event has occurred on the server!"
    print(event_message)

    # Send the event message to all connected clients
    for client in clients:
        try:
            client.send(event_message.encode())
        except Exception as e:
            print(f"Error sending to a client: {e}")

# Function to start the server and listen for incoming connections
def start_server():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all available interfaces
    server_socket.listen(5)  # Allow a max of 5 pending connections
    print("Server started, waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()

if __name__ == "__main__":
    start_server()
