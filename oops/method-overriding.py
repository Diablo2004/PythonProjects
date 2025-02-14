# Method Overriding - A child class redefines a method of the parent class
class Parent:
    def show(self):
        return "This is Parent class"

class Child(Parent):
    def show(self):  # Overriding method
        return "This is Child class"

obj = Child()
print(obj.show())  # This is Child class


# Real life example - Overriding in Banking System
class Account:
    def get_interest_rate(self):
        return 4  # Default interest rate is 4%

class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6  # Higher interest for savings accounts

class FixedDeposit(Account):
    def get_interest_rate(self):
        return 8  # Fixed deposits have even higher interest

savings = SavingsAccount()
fd = FixedDeposit()

print("Savings Interest Rate:", savings.get_interest_rate())
print("Fixed Deposit Interest Rate:", fd.get_interest_rate())

# Overriding with super()
# Super is a built-in function that allows a subclass to access methods or constructors of its parent class.

class Parent:
    def display(self):
        print("Parent Display Method")

class Child(Parent):
    def display(self):
        super().display()  # Call parent method
        print("Child Display Method")

child_obj = Child()
child_obj.display()

