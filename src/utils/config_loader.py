import logging
import os

import yaml


def load_config(config_path="config/config.yaml"):
    """Load YAML configuration file"""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def setup_logging(log_file="logs/project.log", level="INFO"):
    """Setup logging configuration"""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    numeric_level = getattr(logging, level.upper(), logging.INFO)

    logging.basicConfig(
        filename=log_file,
        level=numeric_level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Also print logs to console
    console = logging.StreamHandler()
    console.setLevel(numeric_level)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)
