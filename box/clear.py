import os

csv_path = "box_counts.csv"
captures_dir = "captures"

# Step 1: Clear CSV contents
try:
    with open(csv_path, "w") as f:
        f.truncate()
    print(f"🧹 CSV contents cleared: {csv_path}")
except FileNotFoundError:
    print(f"⚠️ CSV not found: {csv_path}")

# Step 2: Delete images in captures folder
if os.path.exists(captures_dir):
    deleted = 0
    for filename in os.listdir(captures_dir):
        file_path = os.path.join(captures_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted += 1
    print(f"🗑️ Deleted {deleted} files from: {captures_dir}")
else:
    print(f"⚠️ Captures folder not found: {captures_dir}")

