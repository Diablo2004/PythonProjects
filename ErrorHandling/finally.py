# Basic Example
try:
    print("Trying...")
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

# Ensure File Closure
try:
    f = open("sample.txt", "w")
    f.write("Hello, World!")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Closing file...")
    f.close()  # Ensuring file is closed

# Finally with return statement
def test_finally():
    try:
        print("Inside try block")
        return "Returning from try"
    finally:
        print("Finally block executed")

result = test_finally()
print("Returned:", result)

# Handling division
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Cleaning up resources...")

divide(10, 2)
divide(5, 0)

