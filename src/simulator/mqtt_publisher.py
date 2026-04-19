import json
import logging
import time

import paho.mqtt.client as mqtt
from src.simulator.hotspot_manager import HotspotManager
from src.simulator.sensor_simulator import generate_all_sensor_readings
from src.utils.config_loader import load_config


def run_publisher():
    config = load_config()

    broker = config["mqtt"]["broker"]
    port = config["mqtt"]["port"]
    topic = config["mqtt"]["topic"]
    interval = config["simulation"]["interval_seconds"]

    client = mqtt.Client()
    client.connect(broker, port)

    hotspot_manager = HotspotManager(rotation_interval=5)

    print("Starting MQTT publisher...")

    while True:
        hotspot = hotspot_manager.get_current_hotspot()
        readings = generate_all_sensor_readings(hotspot_sensor_id=hotspot)

        for reading in readings:
            message = json.dumps(reading)
            client.publish(topic, message)
            logging.info(
                f"Sent message from {reading['sensor_id']} (status={reading['status']})")

        time.sleep(interval)
