# Print numbers until the number 5, skip number 3
for i in range(1, 10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

    # Using while loop
num = int(input("Enter a number to check if it's prime: "))
i = 2

while i < num:
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
    i += 1
else:
    print(f"{num} is a prime number.")
