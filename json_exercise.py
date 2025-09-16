import json

data = """
{
  "shop": "TechStore",
  "products": [
    {
      "id": 101,
      "name": "Laptop",
      "category": "Computers",
      "price": 899.99,
      "stock": 4,
      "specs": {
        "cpu": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
      }
    },
    {
      "id": 102,
      "name": "Smartphone",
      "category": "Phones",
      "price": 699.99,
      "stock": 0,
      "specs": {
        "cpu": "Snapdragon 8 Gen 2",
        "ram": "12GB",
        "storage": "256GB"
      }
    },
    {
      "id": 103,
      "name": "Tablet",
      "category": "Tablets",
      "price": 399.99,
      "stock": 12,
      "specs": {
        "cpu": "Apple M1",
        "ram": "8GB",
        "storage": "128GB"
      }
    }
  ]
}
"""

pd = json.loads(data)

# Print product name only if stock > 1
for product in pd["products"]:
   if product["stock"] > 1:
    print(product["name"])

average = 0

# Calculate the total sum of product prices
for product in pd["products"]:
    average += product["price"]

# Compute the average price of products
result = average / len(pd["products"])

print(result)

# Find the most expensive product using max() with price as key
most_expensive = max(pd["products"], key=lambda p: p["price"])
print(most_expensive["name"], most_expensive["price"])