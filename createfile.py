import os

# Create a folder
os.makedirs("files", exist_ok=True)

# Generate 10 old files
for i in range(1, 11):
    with open(f"files/old{i}.txt", "w") as file:
        file.write(f"This is old file {i}\n")

# Generate 10 new files
for i in range(1, 11):
    with open(f"files/new{i}.txt", "w") as file:
        file.write(f"This is new file {i}\n")

print("Successfully created 20 files!")
