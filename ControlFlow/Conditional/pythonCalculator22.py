#Python Calculator
operator=input("Enter an operator (+ - * /): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if operator == '+':
    result=num1+num2
    print(result)
elif operator == '-':
    result=num1-num2
    print(result)
elif operator == '*':
    result=num1*num2
    print(result)
elif operator == '/':
    if num2 == 0:
        print("Enter valid input")
    else:
        result=num1/num2
        print(result)
else:
    print("Enter valid operator")