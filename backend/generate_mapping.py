import os
import json

# Get all class folders from dataset
dataset_path = 'data/dataset'
classes = sorted(os.listdir(dataset_path))

# Create mapping
mapping = {str(i): class_name for i, class_name in enumerate(classes)}

print("Disease Mapping:")
for idx, disease in mapping.items():
    print(f"{idx}: {disease}")

# Save to JSON
with open('ml_model/disease_mapping.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print(f"\n✅ Saved {len(mapping)} classes to ml_model/disease_mapping.json")