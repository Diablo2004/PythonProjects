# Decorators in python are powerful and flexible way to modify or enhance the behaviour of functions without changing their source codes
# Often used to add functionality such as logging,authentication or performance measuring in a clean and readable way

def decorator_function(original_function):
    """
    A simple decorator that wraps a function and adds additional behavior.
    """
    def wrapper_function():
        print("Wrapper function executed before the original function.")
        return original_function()
    return wrapper_function

def display():
    """
    A simple function to display a message.
    """
    return "Display function executed."

# Decorating the function
decorated_display = decorator_function(display)

# Calling the decorated function
print(decorated_display())

# Some important built-in decorators

# 1. @staticmethod
class MyClass:
    """
    This class demonstrates the use of the built-in @staticmethod decorator.
    """

    @staticmethod
    def static_method():
        """
        This method doesn't depend on instance or class, it's just a regular function within the class.
        """
        print("This is a static method.")

MyClass.static_method()

# 2. @classmethod
class MyClassWithClassMethod:
    """
    This class demonstrates the use of the built-in @classmethod decorator.
    """
    count = 0

    @classmethod
    def increment_count(cls):
        """
        This method is a class method. It takes the class as the first argument.
        """
        cls.count += 1
        print(f"Class count is: {cls.count}")

obj = MyClassWithClassMethod()
obj.increment_count()

# 3. @property
class MyClassWithProperty:
    """
    This class demonstrates the use of the @property decorator.
    """

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """
        This is a getter property that returns the value.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        This setter allows us to set a new value for _value.
        """
        self._value = new_value

    @value.deleter
    def value(self):
        """
        This deleter removes the _value attribute.
        """
        print("Deleting value")
        del self._value

obj_with_value = MyClassWithProperty(10)
print(obj_with_value.value)  # Getter
obj_with_value.value = 20  # Setter
print(obj_with_value.value)  # Getter after setting
del obj_with_value.value  # Deleter