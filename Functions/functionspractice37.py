def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


students = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]

students_sorted = sorted(students, key=lambda x: x[1], reverse=True)

print(students_sorted)


def calculate_bill(*prices, tax=0.1, discount=0.05, **customer_details):
    subtotal = sum(prices)
    total = subtotal + (subtotal * tax) - (subtotal * discount)

    print(f"Customer: {customer_details.get('name', 'Unknown')}")
    print(f"Items Purchased: {len(prices)}")
    print(f"Total Amount: ${total:.2f}")


calculate_bill(100, 200, 50, tax=0.08, discount=0.1, name="Mehul")



def greet_user(greeting):
    def inner(name):
        return f"{greeting}, {name}!"
    return inner

morning_greet = greet_user("Good Morning")
evening_greet = greet_user("Good Evening")

print(morning_greet("Mehul"))
print(evening_greet("Alice"))


def assign_grades(**students):
    grading_scale = {90: "A", 80: "B", 70: "C", 60: "D"}

    results = {}
    for name, score in students.items():
        grade = next((g for s, g in grading_scale.items() if score >= s), "F")
        #next retrieves the first matching grade based on grading_scale, here s,g equal key,value pair
        results[name] = grade

    return results


grades = assign_grades(Alice=92, Bob=78, Charlie=85, David=59)
print(grades)

