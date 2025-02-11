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


inventory = [
    {"name": "Laptop", "price": 1000, "stock": 10},
    {"name": "Phone", "price": 500, "stock": 25},
    {"name": "Headphones", "price": 150, "stock": 50},
    {"name": "Smartwatch", "price": 250, "stock": 30}
]
def append(name,price,stock):
    inventory.append({"name":name,"price":price,"stock":stock})

    print(inventory)

for i in inventory:
    if i["name"]=="Laptop":
        i["stock"]=5
    else:
        continue

print(inventory)

phone_price = inventory[1]["price"]
print("Price of Phone:", phone_price)

inventory[0]["stock"] = 12
print("Updated stock of Laptop:", inventory[0]["stock"])

inventory.append({"name": "Tablet", "price": 400, "stock": 15})
print("After adding Tablet:", inventory)

del inventory[3]
print("After deleting Smartwatch:", inventory)

for item in inventory:
    print(f"Item: {item['name']}, Stock: {item['stock']}")

in_stock_items = [item for item in inventory if item["stock"] > 20]
print("Items with stock greater than 20:", in_stock_items)

total_value = sum(item["price"] * item["stock"] for item in inventory)
print("Total value of items in stock:", total_value)
