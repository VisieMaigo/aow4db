import os
import subprocess

# Source and destination directories
src_dir = r"C:\Users\VisieMaigo\Videos\EWP"
dst_dir = r"C:\Users\VisieMaigo\Videos\EWP\Converted"

# Ensure destination directory exists
os.makedirs(dst_dir, exist_ok=True)

# Get a set of already converted .avif files in the destination directory
converted_files = {os.path.splitext(f)[0] for f in os.listdir(dst_dir) if f.lower().endswith('.avif')}

# Loop through all .mp4 files in the source directory
for filename in os.listdir(src_dir):
    if filename.lower().endswith(".mp4"):
        base_name = os.path.splitext(filename)[0]
        if base_name in converted_files:
            print(f"Skipping {filename} (already converted)")
            continue
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, f"{base_name}.avif")
        # ffmpeg command to convert mp4 to avif at 400x514 resolution, scaling exactly (no aspect ratio preservation)
        cmd = [
            "ffmpeg",
            "-i", src_path,
            "-vf", "scale=400:514",
            "-cpu-used", "8",
            "-y",  # Overwrite output file if exists
            dst_path
        ]
        print(f"Converting {src_path} to {dst_path} ...")
        subprocess.run(cmd, check=True)
print("All conversions complete.")
