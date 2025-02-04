principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("Enter principle: "))
    if principle<=0:
        print("Cant be <=0")

while rate<=0:
    rate=float(input("Enter rate: "))
    if rate<=0:
        print("Cant be <=0")

while time<=0:
    time=float(input("Enter time: "))
    if time<=0:
        print("Cant be <=0")

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")