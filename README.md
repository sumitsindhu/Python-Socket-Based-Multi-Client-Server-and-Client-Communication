# Python Socket-Based Multi-Client Server and Client Communication

This project demonstrates a simple multi-client server and client communication using Python's `socket` and `threading` libraries. It includes:

- **TCP Client**: A client that connects to the server, sends messages, and displays messages received from the server.
- **TCP Server**: A server that handles multiple clients, receives messages, and triggers events which are broadcasted to all connected clients.

## Files
- `client.py`: The client application.
- `server.py`: The server application.

## Requirements
- Python 3.x

## Running the Server and Client

### Start the Server:
# Run the server script (`server.py`):
   python server.py

# Run the client script (`client.py`):
    python client.py