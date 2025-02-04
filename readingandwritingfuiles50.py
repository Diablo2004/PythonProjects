# Open a file in read mode ('r')
try:
    with open("sample.txt", "r") as file:
        content = file.read()  # Reads the entire file
        print(content)
except FileNotFoundError:
    print("The file does not exist.")

# Open a file in write mode ('w')
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Open a file in append mode ('a')
with open("sample.txt", "a") as file:
    file.write("\nThis line will be added without removing previous content.")
