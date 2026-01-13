import os
import yaml

processed_path = "data/processed/processed.txt"
model_path = "models/model.txt"
metrics_path = "metrics.txt"

os.makedirs("models", exist_ok=True)

# Load params.yaml
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

model_name = params.get("train", {}).get("model_name", "default_model")

with open(processed_path, "r") as f:
    data = f.read()

model_output = f"Model name: {model_name}\nModel trained on data:\n{data}"

with open(model_path, "w") as f:
    f.write(model_output)

metrics = {
    "data_length": len(data)
}

with open(metrics_path, "w") as f:
    yaml.dump(metrics, f)

print("Training completed")
