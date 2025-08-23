def count_lines_in_file(filename = "css.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found!")
        return 0


# Part 3: File Handling Operations
def file_operations(filename):
    try:
        # 1. Read the file contents
        with open(filename, "r") as f:
            content = f.read()
            print("File Content:\n", content)

        # 2. Append new content to file
        with open(filename, "a") as f:
            f.write("\nThis line is newly appended.")

        # 3. Show file after appending
        with open(filename, "r") as f:
            print("\nFile after appending:\n", f.read())

    except FileNotFoundError:
        print("File not found!")



filename = "sample.txt"   

print("Total number of lines in file:", count_lines_in_file(filename))