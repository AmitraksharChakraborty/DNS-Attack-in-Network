import socket
import time
from collections import deque

# Settings
HOST = '127.0.0.1'
PORT = 9999
TRAFFIC_THRESHOLD = 100  # Max connections allowed in 10 seconds
MONITOR_WINDOW = 10  # Monitoring window in seconds

# Queue to track connection timestamps
connection_times = deque()


def detect_high_traffic():
    """
    Detect if the traffic exceeds the defined threshold.
    """
    now = time.time()
    # Remove timestamps older than the monitoring window
    while connection_times and now - connection_times[0] > MONITOR_WINDOW:
        connection_times.popleft()
    # Check if traffic exceeds the threshold
    if len(connection_times) > TRAFFIC_THRESHOLD:
        return True
    return False


def run_detector():
    """
    Start the detection server to monitor traffic.
    """
    # Create a socket to listen for connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[INFO] Traffic detector running on {HOST}:{PORT}")

        while True:
            try:
                # Accept connections
                client_socket, addr = s.accept()
                connection_times.append(time.time())  # Record the connection time

                # Check for high traffic
                if detect_high_traffic():
                    print("[ALERT] High traffic detected! Potential attack.")
                else:
                    print(f"[INFO] Connection from {addr}")

                client_socket.close()
            except Exception as e:
                print(f"[ERROR] {e}")
                break


if __name__ == "__main__":
    run_detector()


