user = {
    "id":101,
    "name":"Deepak",
    "is_acitive":True
}

print(user["name"])
print(user["is_acitive"])



# A dataset of 2 users
users = [
    {"id": 1, "name": "Alice"},  # Index 0
    {"id": 2, "name": "Bob"}     # Index 1
]

# Accessing "Bob":
# Step 1: Get the list item at index 1 -> {"id": 2, "name": "Bob"}
# Step 2: Get the value for key "name"
print(users[1]["name"])  # Output: Bob