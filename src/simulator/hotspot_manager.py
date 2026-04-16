import random

from src.simulator.layout import RACK_LAYOUT


class HotspotManager:
    def __init__(self, rotation_interval=5):
        self.rotation_interval = rotation_interval
        self.cycle_count = 0
        self.current_hotspot = None
        self.sensor_ids = [sensor["sensor_id"] for sensor in RACK_LAYOUT]
        self.rotate_hotspot()

    def rotate_hotspot(self):
        available = [sid for sid in self.sensor_ids if sid !=
                     self.current_hotspot]
        self.current_hotspot = random.choice(available)

    def get_current_hotspot(self):
        if self.cycle_count > 0 and self.cycle_count % self.rotation_interval == 0:
            self.rotate_hotspot()

        self.cycle_count += 1
        return self.current_hotspot
