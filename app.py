import tensorflow as tf
from scapy.all import sniff, IP, TCP
import numpy as np
import threading
from flask import Flask, render_template, jsonify

# Initialize Flask app
app = Flask(__name__)

alerts = []

@app.route('/')
def home():
    return render_template('dashboard.html', alerts=alerts)

@app.route('/alerts')
def get_alerts():
    return jsonify({'alerts': alerts})

def add_alert(alert_message):
    alerts.append(alert_message)
    if len(alerts) > 50:
        alerts.pop(0)  # Keep the list to the last 50 alerts

# Load the saved model
model = tf.keras.models.load_model('nids_model.h5')

def extract_features(packet):
    features = []

    protocol_type_map = {'tcp': 0, 'udp': 1, 'icmp': 2}

    # Placeholder for duration
    features.append(0)

    # Check if packet has IP layer to extract protocol type
    if packet.haslayer(IP):
        features.append(protocol_type_map.get(packet[IP].proto, 3))
    else:
        features.append(3)  # Default value if no IP layer

    # Placeholder for service and flag
    features.append(0)
    features.append(0)

    # Source bytes
    features.append(len(packet))

    # Placeholder for destination bytes
    features.append(0)

    # Land: Check if source and destination IPs and ports are the same
    if packet.haslayer(IP):
        land = 1 if packet[IP].src == packet[IP].dst else 0
    else:
        land = 0
    features.append(land)

    # Placeholder for wrong_fragment
    features.append(0)

    # Urgent: Check for urgent flag in TCP
    if packet.haslayer(TCP):
        urgent = 1 if packet[TCP].flags & 0x20 else 0
    else:
        urgent = 0
    features.append(urgent)

    # Placeholders for remaining features to ensure 121 features in total
    while len(features) < 121:
        features.append(0)

    return np.array(features).reshape(1, -1)

def detect_anomaly(packet):
    features = extract_features(packet)
    prediction = model.predict(features)
    if prediction[0] > 0.5:
        alert_message = f"Anomaly detected: {packet.summary()}"
        print(alert_message)
        add_alert(alert_message)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=lambda: app.run(debug=True, use_reloader=False))
    flask_thread.start()
    sniff(prn=detect_anomaly)
