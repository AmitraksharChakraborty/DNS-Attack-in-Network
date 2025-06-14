import socket

host = "127.0.0.1"
port = 8080

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.sendall(b"Hello, server!")  # Send test data
    response = client.recv(1024)  # Receive response from the server
    print(f"Response from server: {response.decode()}")
    client.close()
except Exception as e:
    print(f"Error: {e}")
