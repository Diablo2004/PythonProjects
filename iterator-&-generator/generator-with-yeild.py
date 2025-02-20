def fibonacci():
    """
    Generator that yields the fibonacci sequence
     The user should expect integer values representing Fibonacci numbers.

    """
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib=fibonacci()
for _ in range(10): # underscore is used as a variable name when you want to indicate that the value of variable is not important.
    print(next(fib))

print("-------------")

def even_numbers(start, end):
    """
    even_numbers(start, end) – This generator yields even integers sequentially
    from the specified start value to the end value (both inclusive).

    """
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

evens = even_numbers(1, 20)

for num in evens:
    print(num)

print("-------------")

def is_prime(n):
    """
    Checks if a number n is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    """
    Generator that yields prime numbers indefinitely.
    """
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

primes = prime_numbers()

# Get the first 10 primes
for _ in range(10):
    print(next(primes))

print("-------------")

def character_count(string):
    """
    Generator that counts the occurrence of characters in a string, yielding the running count.
    """
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
        yield counts

count_gen = character_count("hello world")

for count in count_gen:
    print(count)  # Output will show the running count of characters encountered so far.
