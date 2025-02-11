try:
    file = open("example48.txt", "r")
except FileNotFoundError:
    print("The file was not found.")

content = file.read()
print(content)

for line in file:
    print(line.strip())  # strip() removes the newline character

    # file.write("Hello, World!")

file.close()




