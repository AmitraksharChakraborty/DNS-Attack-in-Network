from flask import Flask, request, jsonify
from collections import defaultdict
import time

app = Flask(__name__)
traffic_log = defaultdict(int)
start_time = time.time()


@app.route('/monitor')
def monitor():
    global traffic_log
    current_time = time.time()
    alerts = []

    # Check if monitoring time exceeded
    if current_time - start_time > 20:  # Extended monitoring interval
        for ip, count in traffic_log.items():
            print(f"IP: {ip}, Requests: {count}")  # Debug: Print logged traffic
            if count > 20:  # Lowered threshold for testing
                alerts.append(f"Potential attack detected from IP: {ip}, Requests: {count}")
        traffic_log.clear()  # Reset traffic log for next monitoring interval

    if alerts:
        return jsonify({"alerts": alerts})
    else:
        return jsonify({"alerts": "No suspicious activity detected."})


@app.after_request
def log_traffic(response):
    try:
        ip = request.remote_addr
        traffic_log[ip] += 1
        print(f"IP Logged: {ip}")  # Debug: Log each incoming IP
    except Exception as e:
        print(f"Error logging traffic: {e}")
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
