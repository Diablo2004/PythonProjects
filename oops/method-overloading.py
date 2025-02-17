# Method Overloading - Defining multiple methods with the same name but different parameters.
#                      Python doesn't support true method overloading like Java or C++
#                      Instead, we can achieve it using default arguments, *args, and type checking.

class Calculator:
    """A class demonstrating method overloading using default arguments."""

    def add(self, a, b=0, c=0):  # Default values allow different calls
        try:
            return a + b + c
        except TypeError:
            print("Error: Invalid input types. Please provide numbers.")

calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15))  # Output: 30
print(calc.add(5, "10"))    # Error handled


class MathOperations:
    """A class demonstrating method overloading using variable-length arguments."""

    def multiply(self, *args):  # Accepts multiple arguments
        try:
            result = 1
            for num in args:
                if not isinstance(num, (int, float)):  # Ensure valid types
                    raise ValueError(f"Invalid input: {num} is not a number.")
                result *= num
            return result
        except ValueError as e:
            print(f"Error: {e}")

math = MathOperations()
print(math.multiply(5))          # Output: 5
print(math.multiply(5, 3))       # Output: 15
print(math.multiply(5, 3, 2))    # Output: 30
print(math.multiply(5, "3"))     # Error handled


class Printer:
    """A class demonstrating method overloading using type checking."""

    def print_data(self, data):
        try:
            if isinstance(data, int):
                print("Integer:", data)
            elif isinstance(data, float):
                print("Float:", data)
            elif isinstance(data, str):
                print("String:", data)
            else:
                raise TypeError(f"Unsupported type: {type(data).__name__}")
        except TypeError as e:
            print(f"Error: {e}")

p = Printer()
p.print_data(10)           # Integer: 10
p.print_data(10.5)         # Float: 10.5
p.print_data("Hello")      # String: Hello
p.print_data([1, 2, 3, 4]) # Error handled
