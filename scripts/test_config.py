import logging

from src.utils.config_loader import load_config, setup_logging

# Load config
config = load_config()

# Setup logging using config values
setup_logging(
    log_file=config["logging"]["log_file"],
    level=config["logging"]["level"]
)

logging.info("Config loaded successfully!")

print("MQTT Broker:", config["mqtt"]["broker"])
print("InfluxDB URL:", config["influxdb"]["url"])
print("Hotspot Temp Threshold:", config["thresholds"]["hotspot_temp_c"])
