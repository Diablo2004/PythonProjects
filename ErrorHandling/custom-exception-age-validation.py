class AgeTooYoungError(Exception):
    def __init__(self, age, message="Age must be 18 or above."):
        self.age = age
        self.message = message
        super().__init__(message)
def check_age(age):
    if age < 18:
        raise AgeTooYoungError(age)
    else:
        print("Age is valid!")

# Testing the custom exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except AgeTooYoungError as e:
    print(f"AgeTooYoungError: {e}")
except ValueError:
    print("Invalid input! Please enter a number.")
