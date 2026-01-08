
"""   
Your Task: You are processing a product record: product = {"id": 500, "price": 100, "stock": 5}

The price has increased. Update "price" to 120.

We calculated the total value. Create a new key called "total_value" and set it equal to price * stock. (Hint: Use the variables or the dictionary values for the math).

Print the modified product dictionary.

"""


product = {"id": 500, "price": 100, "stock": 5}

product["price"] = 120

product["total_value"] = product["price"] * product["stock"]

print(product)