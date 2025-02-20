import time

def timer(func):
    """
    A decorator that measures the time taken by a function to execute.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(4)

slow_function()

print("------------")

# A decorator that denies access based on user roles

def requires_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied: Admin privileges required.")
            return
        return func(user)
    return wrapper

@requires_admin
def delete_database(user):
    print(f"Database deleted by {user}.")

delete_database("guest")  # Output: Access Denied
delete_database("admin")  # Output: Database deleted by admin.

print("-----------")

# A decorator that counts how many times a function is called

def count_call(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_call
def say_hello():
    print("Hello!")

say_hello()
say_hello()

print("---------------")

# Applying multiple decorators to a single function

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@uppercase_decorator
@exclaim_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO!!!

print("----------------")

# A decorator that takes arguments to control behaviour
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()



