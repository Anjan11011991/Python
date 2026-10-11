
import os
import glob

# Folder containing the files
folder = "files"

# Find only files starting with "old"
old_files = glob.glob(os.path.join(folder, "new*.txt"))

# Delete old files
for file_path in old_files:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except OSError as error:
        print(f"Error deleting {file_path}: {error}")

print("Old file cleanup completed!")
