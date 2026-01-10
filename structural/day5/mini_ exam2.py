"""   
Q3. The ETL Processor (Capstone) You have a list of raw transaction dictionaries:

Python

data = [
    {"amount": 100, "currency": "USD"},
    {"amount": 50, "currency": "EUR"},
    {"amount": 200, "currency": "USD"}
]
Write a function convert_to_usd(item):

Takes a dictionary row (item) as input.

IF item["currency"] is "EUR", multiply amount by 1.1 and return the new value.

ELSE, just return the original amount.

Loop through the list, call your function, and print the result.


"""


data = [
    {"amount": 100, "currency": "USD"},
    {"amount": 50, "currency": "EUR"},
    {"amount": 200, "currency": "USD"}
]

def convert_to_usd(item):
    if item["currency"] == "EUR":
        mul = item["amount"]*1.1
        return mul
    else:
        return item["amount"]
    
for row in data:
    result = convert_to_usd(row)
    print(f"Final amount: {result}")
