#Right Angled Triangle
n = 5
for i in range(1, n+1):
    print("*" * i)

print("------------")
#Inverted Right angled Triangle
n = 5
for i in range(n, 0, -1):
    print("*" * i)

print("------------")

#Pyramid
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

print("------------")

#Diamond
n = 5
for i in range(1, n+1, 2):
    print(" " * ((n-i)//2) + "*" * i)
for i in range(n-2, 0, -2):
    print(" " * ((n-i)//2) + "*" * i)

print("------------")

#Numbered Triangle

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("------------")

#Flloyds Triangle

n = 5
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()
