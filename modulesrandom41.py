import random

# Generate a random integer between 1 and 100
random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")


fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(f"Random fruit selected: {random_fruit}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

