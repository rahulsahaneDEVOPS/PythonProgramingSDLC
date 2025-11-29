import os
import sys
import shutil
from datetime import datetime

def backup_files(src_dir, dest_dir):
    # Check if source directory exists
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory does not exist: {src_dir}")
        return

    # Check if destination directory exists
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory does not exist: {dest_dir}")
        return

    # Iterate through all files in source directory
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)

        # Skip directories; only backup files
        if os.path.isdir(src_file):
            continue

        dest_file = os.path.join(dest_dir, filename)

        # If file already exists in destination, append timestamp
        if os.path.exists(dest_file):
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base}_{timestamp}{ext}"
            dest_file = os.path.join(dest_dir, new_filename)

        try:
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} → {dest_file}")
        except Exception as e:
            print(f"Failed to copy {src_file}: {e}")

def main():
    # Expect 2 arguments: source and destination
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    backup_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
