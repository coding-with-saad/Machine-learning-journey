product_name = "Gaming Laptop"
brand = "Dell"
price = 235000.50
discount = 10
stock = 15
is_available = True

specifications = {
    "Processor": "Intel Core i7",
    "RAM": "16 GB",
    "Storage": "1 TB SSD",
    "GPU": "RTX 4060"
}

colors = ["Black", "Silver"]

print("========= PRODUCT DETAILS =========")
print("Product:", product_name)
print("Brand:", brand)
print("Price:", price)
print("Discount:", discount, "%")
print("Available:", is_available)
print("Stock:", stock)
print()

print("Specifications")
for key, value in specifications.items():
    print(key, ":", value)

print()

print("Available Colors")
for color in colors:
    print("-", color)