import os
import yaml
import sys

# Get project root (one level above src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load params.yaml
params_path = os.path.join(BASE_DIR, "params.yaml")

try:
    with open(params_path, "r") as f:
        params = yaml.safe_load(f)
except FileNotFoundError:
    print(f"Error: params.yaml not found at {params_path}")
    sys.exit(1)

raw_path = os.path.join(BASE_DIR, "data", "raw", "demo.test")
processed_path = os.path.join(BASE_DIR, "data", "processed", "processed.txt")

# Create processed directory if it doesn't exist
os.makedirs(os.path.dirname(processed_path), exist_ok=True)

try:
    with open(raw_path, "r") as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: Raw data file not found at {raw_path}")
    sys.exit(1)

# Parameter-driven preprocessing
if params.get("preprocess", {}).get("to_uppercase", False):
    processed_data = data.upper()
else:
    processed_data = data

with open(processed_path, "w") as f:
    f.write(processed_data)

print("Preprocessing completed")
