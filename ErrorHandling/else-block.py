try:
    num = int(input("Enter a number: "))  # May raise ValueError
    result = 10 / num  # May raise ZeroDivisionError
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else: # Works when no exception occurs
    print(f"Success! The result is {result}.")


# 2 - For file handling
try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully:")
    print(content)
    file.close()

# 3 - Authentication
users = {"john": "pass123", "alice": "hello123"}

def authenticate():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in users:
            raise KeyError("Username not found!")
        if users[username] != password:
            raise ValueError("Incorrect password!")
    except KeyError as e:
        print(f"Login failed: {e}")
    except ValueError as e:
        print(f"Login failed: {e}")
    else:
        print(f"Welcome, {username}! You are logged in.")

authenticate()

