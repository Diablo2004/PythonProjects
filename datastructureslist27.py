#collection = single "variable" used to store multiple values
#List = [] ordered and changable.Duplicates OK
# Set = {} unordered and immutable,but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangable. Duplicates OK. FASTER

#LIST
fruits = ["apple","orange","banana","coconut"]

print(fruits[::-1])

for fruit in fruits:
    print(fruit)
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0,"pineapple")
fruits.sort()
fruits.reverse()
#fruits.clear()
print(fruits.index("coconut"))
print(fruits.count("pineapple"))
print(fruits)
list1=[1,2,3,4]
list2=[1,2,3,4]

for x in range(len(list1)):
    list1[x]=list1[x]+list2[x]
    print(list1[x])

#SET


