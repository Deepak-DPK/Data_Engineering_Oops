"""  
Write the loop:

Iterate through users.

IF active is True: Print "Active User: [Name]".

ELSE: Print "Skipping disabled user: [Name]".

"""


users = [
    {"user": "Alice", "active": True},
    {"user": "Bob", "active": False},
    {"user": "Charlie", "active": True}
]

for x in users:
    if x["active"] == True:
        print(f"Active User: {x["user"]}")
    
    else:
        print(f"Skipping disabled user: {x["user"]}")