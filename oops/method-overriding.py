# Method Overriding - A child class redefines a method of the parent class.

class Parent:
    """A parent class with a method to be overridden by the child class."""

    def show(self):
        return "This is Parent class"


class Child(Parent):
    """A child class that overrides the parent class method."""

    def show(self):  # Overriding method
        return "This is Child class"


obj = Child()
print(obj.show())  # Output: This is Child class


class Account:
    """A base class representing a bank account with a default interest rate."""

    def get_interest_rate(self):
        return 4  # Default interest rate is 4%


class SavingsAccount(Account):
    """A subclass representing a savings account with a higher interest rate."""

    def get_interest_rate(self):
        return 6  # Higher interest for savings accounts


class FixedDeposit(Account):
    """A subclass representing a fixed deposit account with the highest interest rate."""

    def get_interest_rate(self):
        return 8  # Fixed deposits have even higher interest


savings = SavingsAccount()
fd = FixedDeposit()

print("Savings Interest Rate:", savings.get_interest_rate())  # Output: 6
print("Fixed Deposit Interest Rate:", fd.get_interest_rate())  # Output: 8


class Parent:
    """A parent class with a method that can be accessed using super()."""

    def display(self):
        print("Parent Display Method")


class Child(Parent):
    """A child class that overrides the display method and calls the parent method using super()."""

    def display(self):
        super().display()  # Call parent method
        print("Child Display Method")


child_obj = Child()
child_obj.display()

