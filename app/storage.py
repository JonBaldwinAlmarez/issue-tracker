from pathlib import Path

import json

DATA_DIR = Path("data")  # Directory to store data files
DATA_FILE = DATA_DIR / "data.json"  # Path to the JSON data file

# Function to load data from the JSON file


def data_loader():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []


def save_data(data):
    # Ensure the data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
