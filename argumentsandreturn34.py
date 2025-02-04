# return = statement used to end  function and send a result back to user

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

#default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")
#default arguments must always be after non-default arguments

greet()
greet("Mehul")

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " "+ last

fullname=create_name("spongebob","squarepants")
print(fullname)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

