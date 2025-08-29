import os

# 1. Opening a file (reading)
print("1. Opening file:")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# 2. Deleting a file
print("\n2. Deleting file:")
file_to_delete = "delete_me.txt"
# create file for demo
with open(file_to_delete, "w") as f:
    f.write("This file will be deleted.")
# delete it
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"{file_to_delete} deleted successfully!")
else:
    print("File not found.")

# 3. Splitting file (line by line into separate files)
print("\n3. Splitting file:")
with open("sample.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    filename = f"part{i}.txt"
    with open(filename, "w") as f:
        f.write(line)
    print(f"Created {filename}")

# 4. Deleting file (again - using exception handling)
print("\n4. Deleting file with error handling:")
try:
    os.remove("part1.txt")
    print("part1.txt deleted successfully!")
except FileNotFoundError:
    print("File does not exist.")