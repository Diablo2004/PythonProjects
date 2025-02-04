#   *args   =allows you to pass multiple non-key arguments
#   **kwargs=allows you to pass multiple keyword-arguments

def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total
print(add(1,2,3))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("spongebob","squarepants","III")

def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))
print(add_all(5, 10, 15))


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="123 F",city="Jaipur",state="sikkim",zip="1234567")

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Mehul", age=21, city="Jaipur")

def order_summary(*items, **details):
    print("Items Ordered:", items)
    print("Order Details:", details)

order_summary("Pizza", "Pasta", name="Mehul", payment="Credit Card")
