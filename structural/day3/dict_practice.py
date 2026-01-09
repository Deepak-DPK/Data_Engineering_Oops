server = {

    "hostname": "prod-db-01",
    "ip": "192.168.1.5",
    "status": "online"
}

Host = server["hostname"]
address = server["ip"]

print(f"Connecting to {Host} at {address}...")

print("")

print('-'*50)
print("Updating details")
print('-'*50)
user = {"name": "Alice", "score": 10}

# Update score
user["score"] = 20
print(user) # {'name': 'Alice', 'score': 20}

print(" ")

print('-'*50)
print("Adding a New-Key Value Pair")
print('-'*50)

# Add a new field
user["role"] = "Admin"
print(user) # {'name': 'Alice', 'score': 20, 'role': 'Admin'}





