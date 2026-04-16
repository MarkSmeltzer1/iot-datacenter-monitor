from src.simulator.hotspot_manager import HotspotManager
from src.simulator.sensor_simulator import generate_all_sensor_readings

# Create hotspot manager
manager = HotspotManager(rotation_interval=3)

# Simulate multiple cycles
for i in range(10):
    hotspot = manager.get_current_hotspot()
    print(f"\nCycle {i+1} - Current Hotspot: {hotspot}")

    readings = generate_all_sensor_readings(hotspot_sensor_id=hotspot)

    for r in readings:
        if r["status"] == "hotspot":
            print("🔥", r)
