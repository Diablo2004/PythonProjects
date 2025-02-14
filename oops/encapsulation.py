# Encapsulation - Refers to restricting direct access to an objects data and methods
#                 Data Hiding
#                 Controlled Access
#                 Security

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public Attribute
        self.__balance = balance  # Private Attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def get_balance(self):  # Getter Method
        return self.__balance

# Creating object
account = BankAccount("John Doe", 1000)

# Accessing public attribute
print("Account Holder:", account.account_holder)

# Accessing private attribute directly (Not Recommended!)
# print(account.__balance)  # AttributeError

# Accessing private data using method
print("Current Balance:", account.get_balance())

account.deposit(200)
account.withdraw(300)



# Using Getters And Setters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private Attribute

    def get_age(self):  # Getter
        return self.__age

    def set_age(self, new_age):  # Setter
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

# Creating object
student1 = Student("Alice", 20)

# Accessing private attribute using getter
print("Age:", student1.get_age())

# Updating private attribute using setter
student1.set_age(22)
print("Updated Age:", student1.get_age())

# Trying to set an invalid age
student1.set_age(-5)
