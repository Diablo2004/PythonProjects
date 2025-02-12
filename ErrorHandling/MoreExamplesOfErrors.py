#Key Error
try:
    data = {"name": "Mehul", "age": 21}
    print(data["city"])  # Key does not exist
except KeyError as e:
    print(f"KeyError: {e} not found in dictionary.")

#Value Error
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

#Index Error
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Out of range
except IndexError as e:
    print(f"IndexError: {e}")

#TypeError
try:
    result = "hello" + 5  # Cannot add string and integer
except TypeError as e:
    print(f"TypeError: {e}")

#Zero Division Error
try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

#File Not Found error
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

#Attribute Error
try:
    num = 10
    num.append(5)  # Integers don't have an 'append' method
except AttributeError as e:
    print(f"AttributeError: {e}")

#Import Error
try:
    import non_existent_module  # Module does not exist
except ImportError as e:
    print(f"ImportError: {e}")

#Name Error
try:
    print(unknown_variable)  # Undefined variable
except NameError as e:
    print(f"NameError: {e}")

# stop Iteration Error
try:
    my_iter = iter([1, 2, 3])
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
except StopIteration as e:
    print("StopIteration: No more items in iterator.")
