import random

lowest=1
highest=100
answer=random.randint(lowest,highest)
guesses=0
is_running=True

print("Python number guessing game")
print(f"Select a number between {lowest} and {highest}")

while is_running:
    guess=input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest or guess>highest:
            print("That number is out of range")
            print(f"Select a number between {lowest} and {highest}")
        elif guess<answer:
            print("Too low")
        elif guess>answer:
            print("Too high!")
        else:
            print("Correct")
            print(f"Number of guesses is {guesses}")
            is_running=False

    else:
        print("Invalid guess")
        print(f"Select a number between {lowest} and {highest}")
