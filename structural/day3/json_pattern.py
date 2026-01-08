

"""
This combines everything you have learned:

List: To hold the rows.

Dictionary: To hold the columns/fields.

For Loop: To process them.

If Logic: To filter them.

"""


orders = [
    {"id": 1, "status": "pending"},
    {"id": 2, "status": "shipped"},
    {"id": 3, "status": "pending"}
]

for order in orders:
    # 'order' is {"id": 1, "status": "pending"}
    
    if order["status"] == "pending":
        print(f"Order {order['id']} is waiting.")