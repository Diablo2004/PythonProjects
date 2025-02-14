class Laptop: # Sample class to implement modification of attributes
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        if discount < 0:
            raise ValueError("Discount cannot be negative!")
        self.price -= self.price * (discount / 100)

# Creating object
laptop1 = Laptop("Dell", 1000)

print("Original Price:", laptop1.price)
try:
    discount_value = int(input("Enter discount percentage: "))  # Taking user input
    laptop1.apply_discount(discount_value)
    print("Discounted Price:", laptop1.price)
except ValueError as e:
    print("Error:", e)
