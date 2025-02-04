# Creating a tuple
my_tuple = (10, 20, 30, 40)

# Accessing elements
print(my_tuple[0])
print(my_tuple[-1])

a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))
print(my_tuple.index(3))

#SETS

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}  # Duplicates are automatically removed
print(numbers)
numbers.add(6)
numbers.remove(3)

print(numbers)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (A ∪ B) - Combines all unique elements
print(A | B)

# Intersection (A ∩ B) - Common elements
print(A & B)

# Difference (A - B) - Elements in A but not in B
print(A - B)

# Symmetric Difference (A Δ B) - Elements in either A or B, but not both
print(A ^ B)
