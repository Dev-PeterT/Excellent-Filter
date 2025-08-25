import json
from pathlib import Path

def load_config(config_name: str):
    # Base script's pathy by script location and not working directory
    script_directory = Path(__file__).parent
    config_folder = script_directory.parent / "config"

    # Create the file path
    config_path = config_folder / f"{config_name}.json"

    # Check if the file exists
    if not config_path.exists():
        raise FileNotFoundError("❌ Config file '{config_name}.json' not found.")
    
    # Load the json file
    with open(config_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    return config_data