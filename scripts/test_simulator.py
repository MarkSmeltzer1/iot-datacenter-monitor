from src.simulator.sensor_simulator import generate_all_sensor_readings

readings = generate_all_sensor_readings(hotspot_sensor_id="sensor_03")

for reading in readings:
    print(reading)
