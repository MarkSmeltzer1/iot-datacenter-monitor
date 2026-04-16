import random
from datetime import datetime

from src.simulator.layout import RACK_LAYOUT


def generate_sensor_reading(sensor, hotspot_sensor_id=None):
    zone = sensor["zone"]

    if "cold_aisle" in zone:
        temperature_c = round(random.uniform(20.0, 24.0), 2)
    else:
        temperature_c = round(random.uniform(24.0, 28.0), 2)

    humidity_pct = round(random.uniform(35.0, 50.0), 2)
    cpu_load_pct = round(random.uniform(40.0, 75.0), 2)
    status = "normal"

    if sensor["sensor_id"] == hotspot_sensor_id:
        temperature_c = round(random.uniform(30.0, 40.0), 2)
        humidity_pct = round(random.uniform(45.0, 55.0), 2)
        cpu_load_pct = round(random.uniform(80.0, 95.0), 2)
        status = "hotspot"

    reading = {
        "timestamp": datetime.utcnow().isoformat(),
        "sensor_id": sensor["sensor_id"],
        "rack_id": sensor["rack_id"],
        "zone": sensor["zone"],
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
        "cpu_load_pct": cpu_load_pct,
        "status": status
    }

    return reading


def generate_all_sensor_readings(hotspot_sensor_id=None):
    readings = []

    for sensor in RACK_LAYOUT:
        reading = generate_sensor_reading(
            sensor, hotspot_sensor_id=hotspot_sensor_id)
        readings.append(reading)

    return readings
