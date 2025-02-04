try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")


import os

filename = "sample.txt"

try:
    if os.path.exists(filename):
        if os.path.getsize(filename) == 0:
            raise ValueError("File is empty!")
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    else:
        raise FileNotFoundError("The specified file does not exist.")
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
