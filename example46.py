pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
    return 2* pi* radius

def area(radius):
    return pi* radius**2

if __name__=="__main__":
    print(cube(3)) #wont execute if imported