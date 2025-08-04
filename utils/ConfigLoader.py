import json
import os

def get_error_message(env: str, key: str) -> str:

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    config_path = os.path.join(project_root, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    return config[env].get(key, f"Missing key: {key}")