name=input("Enter your name: ")

while name == "":
    print("Enter valid name: ")
    name=input("Enter your name: ")
print(f"Hello {name}")

food=input("Enter a  food you like (q to quit): ")
while not food=="q":
    print(f"You like {food}")
    food=input("Enter another food you like: ")
print("thanks")

