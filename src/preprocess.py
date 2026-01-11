import os

# Get project root (one level above src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "raw", "demo.test")
processed_path = os.path.join(BASE_DIR, "data", "processed", "processed.txt")

# Create processed directory if it doesn't exist
os.makedirs(os.path.dirname(processed_path), exist_ok=True)

# Read raw data
with open(raw_path, "r") as f:
    data = f.read()

# Simple preprocessing
processed_data = data.upper()

# Write processed data
with open(processed_path, "w") as f:
    f.write(processed_data)

print("Preprocessing completed")

