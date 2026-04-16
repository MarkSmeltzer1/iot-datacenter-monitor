import json

import paho.mqtt.client as mqtt
from src.utils.config_loader import load_config


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully.")
        client.subscribe(userdata["topic"])
        print(f"Subscribed to topic: {userdata['topic']}")
    else:
        print(f"Failed to connect to MQTT broker. Return code: {rc}")


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        reading = json.loads(payload)

        print("\nReceived sensor reading:")
        print(f"  Sensor ID:    {reading['sensor_id']}")
        print(f"  Rack ID:      {reading['rack_id']}")
        print(f"  Zone:         {reading['zone']}")
        print(f"  Temperature:  {reading['temperature_c']} C")
        print(f"  Humidity:     {reading['humidity_pct']} %")
        print(f"  CPU Load:     {reading['cpu_load_pct']} %")
        print(f"  Status:       {reading['status']}")
        print(f"  Timestamp:    {reading['timestamp']}")

    except json.JSONDecodeError:
        print("Received invalid JSON message.")
    except KeyError as e:
        print(f"Missing expected field in message: {e}")


def run_consumer():
    config = load_config()

    broker = config["mqtt"]["broker"]
    port = config["mqtt"]["port"]
    topic = config["mqtt"]["topic"]

    client = mqtt.Client(userdata={"topic": topic})
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    print("Starting MQTT consumer...")
    client.loop_forever()
