class CountDown:
    """
    Simple countdown iterator class that counts down from a given number.
    """
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start

# Create an iterator
count = CountDown(5)
iterator = iter(count)

# Use next() to get elements one by one
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) - Stops Iteration

print("-------------")

# Example: Using iter() and next() on a list
fruits = ["apple", "banana", "cherry", "date"]

# Create an iterator from the list using iter()
fruit_iter = iter(fruits)

# Use next() to iterate over the items in the list
print(next(fruit_iter))
print(next(fruit_iter))
print(next(fruit_iter))
print(next(fruit_iter))

# print(next(fruit_iter))  # Raises StopIteration

print("------------")

# Example: Using iter() and next() on a string
word = "Python"

# Create an iterator from the string using iter()
char_iter = iter(word)

# Use next() to get each character
print(next(char_iter))
print(next(char_iter))
print(next(char_iter))
print(next(char_iter))
print(next(char_iter))
print(next(char_iter))

# print(next(char_iter))

print("-----------")
# Example: Using iter() and next() on a dictionary's keys
my_dict = {"a": 1, "b": 2, "c": 3}

# Create an iterator for the dictionary keys
key_iter = iter(my_dict)

# Use next() to get each key in the dictionary
print(next(key_iter))
print(next(key_iter))
print(next(key_iter))
# print(next(key_iter))

print("--------------")

# Example: Using iter() and next() to read a file with proper closure
with open("sample.txt", "r") as file:
    file_iter = iter(file)  # Create an iterator for the file

    try:
        print(next(file_iter))
        print(next(file_iter))
        print(next(file_iter))
        # print(next(file_iter))
    except StopIteration:
        print("End of file reached.")


