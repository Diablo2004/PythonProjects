# Method Overloading - Defining multiple methods with the same name but different parameters.
#                      Python doesn't support true method overloading like java or c++

# Instead we can achieve this using:

# 1.Default Arguments:
class Calculator:
    def add(self, a, b=0, c=0):  # Default values allow different calls
        return a + b + c

calc = Calculator()
print(calc.add(5))   # Output: 5
print(calc.add(5, 10))  # Output: 15
print(calc.add(5, 10, 15)) # Output: 30


# 2.Variable Length Arguments (*args and **kwargs)
class MathOperations: # Class for multiplication
    def multiply(self, *args):  # Accepts multiple arguments
        result = 1
        for num in args:
            result *= num
        return result

math = MathOperations()
print(math.multiply(5))
print(math.multiply(5, 3))
print(math.multiply(5, 3, 2))


# 3.Type Checking(Using isinstance())
class Printer:
    def print_data(self, data):
        if isinstance(data, int):
            print("Integer:", data)
        elif isinstance(data, float):
            print("Float:", data)
        elif isinstance(data, str):
            print("String:", data)
        else:
            print("Unsupported type!")

p = Printer()
p.print_data(10)
p.print_data(10.5)
p.print_data("Hello")
p.print_data([1,2,3,4])

