class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

# Creating object
laptop1 = Laptop("Dell", 1000)

print("Original Price:", laptop1.price)
laptop1.apply_discount(10)  # Applying 10% discount
print("Discounted Price:", laptop1.price)
