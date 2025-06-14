import requests
import threading
import time

target = "http://127.0.0.1:8080/"

def flood():
    while True:
        try:
            response = requests.get(target, timeout=1)
            print(f"Response Code: {response.status_code}")
        except requests.exceptions.RequestException:
            pass

for i in range(100):
    thread = threading.Thread(target=flood)
    thread.daemon = True
    thread.start()

while True:
    time.sleep(1)
