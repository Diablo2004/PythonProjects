# Password check with limited attempts
password = "secure123"
attempts = 3

while attempts > 0:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print(f"Wrong password. {attempts} attempts remaining.")
else:
    print("Access denied.")
else if:

