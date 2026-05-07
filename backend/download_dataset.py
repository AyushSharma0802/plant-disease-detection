import os
import shutil
import kagglehub
from pathlib import Path

print("=" * 80)
print("🌿 DOWNLOADING PLANTVILLAGE DATASET")
print("=" * 80)

# ============================================================================
# 📥 STEP 1: DOWNLOAD DATASET
# ============================================================================

print("\n📥 STEP 1: Downloading PlantVillage dataset from Kaggle...")
print("   (This will take 5-15 minutes depending on internet speed)")
print("   ☕ Go get coffee while waiting!")

try:
    # Download dataset using Kaggle Hub
    path = kagglehub.dataset_download("vipomoondal/plantvillage")
    
    print(f"✅ Download complete!")
    print(f"   📁 Downloaded to: {path}")
    
except Exception as e:
    print(f"❌ Download failed: {e}")
    print("\n💡 Troubleshooting:")
    print("   1. Check internet connection")
    print("   2. Verify Kaggle credentials in ~/.kaggle/kaggle.json")
    print("   3. Try again in a few minutes")
    exit()

# ============================================================================
# 📂 STEP 2: ORGANIZE DATASET
# ============================================================================

print("\n📂 STEP 2: Organizing dataset...")

# Define paths
downloaded_path = Path(path)
destination_path = Path('data/PlantVillage')

# Create destination folder if it doesn't exist
os.makedirs(destination_path, exist_ok=True)

# Find the actual data folder
# Kaggle sometimes puts data in a subfolder
segmented_path = downloaded_path / 'segmented'

if segmented_path.exists():
    source_path = segmented_path
    print(f"   Found segmented folder")
else:
    source_path = downloaded_path
    print(f"   Using root downloaded folder")

# ============================================================================
# 📋 STEP 3: COPY FILES
# ============================================================================

print("\n📋 STEP 3: Copying files to correct location...")

try:
    # Copy all disease folders
    for disease_folder in source_path.iterdir():
        if disease_folder.is_dir():
            dest_folder = destination_path / disease_folder.name
            
            # Skip if already exists
            if dest_folder.exists():
                print(f"   ⏭️  {disease_folder.name} (already exists)")
            else:
                shutil.copytree(disease_folder, dest_folder)
                print(f"   ✅ {disease_folder.name}")
    
    print("\n✅ Files copied successfully!")
    
except Exception as e:
    print(f"❌ Error copying files: {e}")
    exit()

# ============================================================================
# ✅ STEP 4: VERIFY DATASET
# ============================================================================

print("\n✅ STEP 4: Verifying dataset...")

dataset_path = Path('data/PlantVillage')

# Count disease folders
disease_folders = [f for f in dataset_path.iterdir() if f.is_dir()]
num_diseases = len(disease_folders)

print(f"\n📊 DATASET STATISTICS:")
print(f"   Total disease classes: {num_diseases}")

# Count images in each folder
total_images = 0
print(f"\n   Disease breakdown:")

for disease_folder in sorted(disease_folders):
    images = [f for f in disease_folder.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
    num_images = len(images)
    total_images += num_images
    print(f"      {disease_folder.name}: {num_images} images")

print(f"\n   📈 Total images: {total_images}")

# ============================================================================
# 🎉 COMPLETE
# ============================================================================

print("\n" + "=" * 80)
print("🎉 DATASET READY FOR TRAINING!")
print("=" * 80)

print(f"""
✅ Dataset location: {dataset_path}
✅ Total diseases: {num_diseases}
✅ Total images: {total_images}

Next step: Run train_model.py
   python train_model.py

The training script will automatically find the dataset!
""")