my_tuple = (10, 20, 30, 40)
list=[1,2,3,4,5]
list[0]=10
# Accessing elements
print(my_tuple[0])
print(my_tuple[-1])

a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))
print(my_tuple.index(3))

mixed_tuple = (10, "hello", 3.14, [1, 2, 3], (4, 5))
print("Mixed Tuple:", mixed_tuple)

a, b, c, d, e = mixed_tuple
print("Unpacked values:", a, b, c, d, e)

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Access nested tuple element:", nested_tuple[1][2])

sliced_tuple = mixed_tuple[1:4]
print("Sliced Tuple:", sliced_tuple)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concat_tuple = tuple1 + tuple2
repeat_tuple = tuple1 * 3
print("Concatenated Tuple:", concat_tuple)
print("Repeated Tuple:", repeat_tuple)

try:
    mixed_tuple[0] = 100
except TypeError as e:
    print("Error:", e)

print("Index of 'hello':", mixed_tuple.index("hello"))
print("Count of 10:", mixed_tuple.count(10))

my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)


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



s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

union_set = s1 | s2
intersection_set = s1 & s2
difference_set = s1 - s2
symmetric_diff_set = s1 ^ s2
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_diff_set)

s1.add(60)
s1.remove(20)
s1.discard(100)
s1.pop()
s1.clear()
print("Updated Set after Operations:", s1)

print("Is s2 a subset of s1?", s2.issubset(s1))
print("Is s1 a superset of s2?", s1.issuperset(s2))

mixed_set = {1, 2, "hello", 3.14, (1, 2)}
print("Set with Different Data Types:", mixed_set)

fs = frozenset([1, 2, 3, 4])
print("Frozen Set:", fs)

my_list = [1, 2, 2, 3, 3, 4]
set_from_list = set(my_list)
print("Set from List:", set_from_list)

even_set = {x for x in range(10) if x % 2 == 0}
print("Set Comprehension (Even Numbers):", even_set)

