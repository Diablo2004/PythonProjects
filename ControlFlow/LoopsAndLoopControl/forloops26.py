# import time
# credit_card="1234-5678-9012-3456"
#
# for x in credit_card:
#     print(x)
#
# my_time=int(input("Enter the time in seconds: "))
#
# for x in range(my_time,0,-1): #-1 FOR REVERSED
#     seconds=x%60
#     minutes=int(x/60) % 60
#     hours=int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME'S UP!")

x=["mehul","satvik","mrudul"]
y=["20","21","22"]

for name,age in zip(x,y):
    print(name,":",age)


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end=" ")
    print()
