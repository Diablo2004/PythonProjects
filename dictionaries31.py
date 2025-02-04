student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science",
    "grade": "A"
}

print(student)


print(student["name"])
print(student["age"])

print(student.get("name"))
print(student.get("marks"))
print(student.get("marks", "Not Available"))
print(student.keys())

print(student.values())

for key, value in student.items():
    print(f"{key}: {value}")

student.pop("grade")

student.popitem()
print(student)