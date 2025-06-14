import socket
import logging
import time
from collections import deque

# Configure logging
logging.basicConfig(filename='server_traffic.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 8080  # Port to listen on
CONNECTION_LIMIT = 100  # Max connections allowed in 5 seconds

# Queue to track connection timestamps
connection_times = deque()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[INFO] Server is running on {HOST}:{PORT}")

while True:
    try:
        now = time.time()
        # Remove outdated timestamps (older than 5 seconds)
        while connection_times and now - connection_times[0] > 5:
            connection_times.popleft()

        # Check if connection limit is exceeded
        if len(connection_times) >= CONNECTION_LIMIT:
            print("[ALERT] High traffic detected! Temporarily rejecting connections.")
            time.sleep(1)  # Pause to mitigate traffic
            continue

        # Accept a new connection
        client_socket, addr = server_socket.accept()
        connection_times.append(now)  # Record the connection time

        # Log the connection
        logging.info(f"Connection from {addr}")

        # Respond to the client
        client_socket.sendall(b"Welcome to the server!")
        client_socket.close()
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down the server.")
        break
    except Exception as e:
        print(f"[ERROR] {e}")

server_socket.close()


