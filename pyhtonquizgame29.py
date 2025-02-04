# Python quiz game

questions=("How many elements are in the periodic table?: ",
           "Which animal lays the largest eggs?: ",
           "What is the most abundant gas in Earth's atmosphere?: ",
           "How many bones are in the human body?: ",
           "Which planet in the solar system is the hottest?: ")

options=(("A.116","B.117","C.118","D.119"),
         ("A.Whale","B.Crocodile","C.Elephant","D.Ostrich"),
         ("A.Nitrogen","B.Oxygen","C.CO2","D.Hydrogen"),
         ("A.206","B.207","C.208","D.209"),
         ("A.Mercury","B.Venus","C.Mars","D.Jupiter"))

answers=("C","D","A","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)
    while True:
        guess = input("Enter (A, B, C, D): ").upper()
        if guess in ["A", "B", "C", "D"]:
            break
        print("Invalid input. Please enter A, B, C, or D.")
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num+=1

print(f"Your score is: {score}")