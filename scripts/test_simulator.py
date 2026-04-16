from src.simulator.sensor_simulator import generate_all_sensor_readings

readings = generate_all_sensor_readings()

for reading in readings:
    print(reading)
