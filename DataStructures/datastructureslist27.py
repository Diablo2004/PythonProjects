#collection = single "variable" used to store multiple values
#List = [] ordered and changable.Duplicates OK
# Set = {} unordered and immutable,but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangable. Duplicates OK. FASTER

#LIST
fruits = ["apple","orange","banana","coconut"]

print(fruits[::-1])

print(fruits.pop(0))
for fruit in fruits:
    print(fruit)

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.pop(0)
# fruits.reverse()
# #fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("pineapple"))
# print(fruits)

list1=[1,2,3,4]
list2=[1,2,3,4]

for x in range(len(list1)):
    list1[x]=list1[x]+list2[x]
    print(list1[x])


#
# students = ["Alice", "Bob", "Charlie", "David", "Eva"]
# grades = [85, 92, 88, 70, 95]
#
# result=sum(grades)/len(grades)
# print(result)


from functools import reduce

my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sliced elements (1:4):", my_list[1:4])

my_list[2] = 99
print("After modifying index 2:", my_list)

my_list.append(60)
my_list.insert(2, 15)
print("After appending and inserting:", my_list)

my_list.pop()
print("After pop:", my_list)
my_list.remove(99)
print("After removing 99:", my_list)

print("Is 40 in list?", 40 in my_list)
print("Is 100 in list?", 100 in my_list)

print("Index of 40:", my_list.index(40))

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted List:", numbers)
numbers.sort(reverse=True)
print("Reverse Sorted List:", numbers)

my_list.reverse()
print("Reversed List:", my_list)

copy_list = my_list.copy()
print("Copied List:", copy_list)

concatenated_list = my_list + numbers
print("Concatenated List:", concatenated_list)

doubled_list = my_list * 2
print("Doubled List:", doubled_list)

even_numbers = [x for x in my_list if x % 2 == 0]
print("Even Numbers:", even_numbers)

squared_numbers = [x**2 for x in my_list]
print("Squared List:", squared_numbers)

unique_numbers = list(set(my_list))
print("Unique List:", unique_numbers)

sum_of_elements = sum(my_list)
print("Sum of elements:", sum_of_elements)

max_element = max(my_list)
print("Max element:", max_element)

min_element = min(my_list)
print("Min element:", min_element)

filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print("Filtered Even Numbers:", filtered_list)

mapped_list = list(map(lambda x: x * 2, my_list))
print("Mapped List (Doubled):", mapped_list)

reduced_sum = reduce(lambda x, y: x + y, my_list, 0)
print("Reduced Sum:", reduced_sum)

zipped_list = list(zip(my_list, numbers))
print("Zipped List:", zipped_list)

flattened_list = [item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]
print("Flattened List:", flattened_list)

nested_list = [[i for i in range(3)] for j in range(3)]
print("Nested List:", nested_list)

my_list.clear()
print("Cleared List:", my_list)



