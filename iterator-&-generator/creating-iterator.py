from codecs import strict_errors
from logging.config import stopListening


class Reverse:
    """
    Iterator class that returns elements in reverse order.
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self # meaning the class itself will act like iterator

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# Create an iterator
rev = Reverse('giraffe')
for char in rev:
    print(char)


print("------------")
# Iterator that iterates over a range of numbers

class MyRange:
    """
    Custom iterator that behaves like range(start, stop, step).

    Ensures valid input and prevents non-integer or None values.
    """

    def __init__(self, start, stop, step):
        if not all(isinstance(i, int) for i in (start, stop, step)):
            raise ValueError("All arguments (start, stop, step) must be integers.")
        if step == 0:
            raise ValueError("Step cannot be zero.")
        if start is None or stop is None or step is None:
            raise ValueError("None values are not allowed.")

        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            current_value = self.current
            self.current += self.step
            return current_value


myRange = MyRange(1, 10, 2)

for num in myRange:
    print(num)

print("------------")

class Fibonacci:
    """
    Fibonacci sequence generator as an iterator.
    fibonacci() – This generator yields Fibonacci numbers sequentially up to the specified limit.
    The user should expect integer values representing Fibonacci numbers.
    """
    def __init__(self,stop):
        self.stop=stop
        self.a=0
        self.b=1
        self.start=1

    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.stop:
            raise StopIteration
        else:
            fib_number=self.a
            self.a=self.b
            self.b=self.b+fib_number
            self.start+=1
            return fib_number

fib=Fibonacci(10)
for i in fib:
    print(i)
