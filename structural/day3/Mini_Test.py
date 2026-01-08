"""   
Day 3 Mini-Exam (3 Questions)
Q1. The Dictionary Builder Create a dictionary variable named job_config. It must have:

Key "job_name" with value "daily_ETL".

Key "retries" with value 3.

Key "notify_email" with value "admin@company.com".

Q2. The Debugger The following code is supposed to stop searching when it finds 50, but it keeps running. Fix it.

Python

# BAD CODE
numbers = [10, 20, 50, 60, 70]
for n in numbers:
    if n == 50:
        continue # <--- This is the bug
    print(n)
Q3. The ETL Script (Capstone) You have a list of raw transaction data:

Python

transactions = [
    {"id": 101, "amount": 50, "valid": True},
    {"id": 102, "amount": 0, "valid": False},
    {"id": 103, "amount": 100, "valid": True}
]
Write a loop that:

Iterates through transactions.

IF the transaction is NOT valid (valid is False), print "Skipping invalid ID: {id}" and continue.

ELSE (if valid), print "Processing ID: {id} with amount ${amount}".


"""

print("Q1 CODE--A")

job_config = {
    "job_name" : "daily_ETIL",
    "retries"  : 3,
    "notify_email" : "admin@company.com"
}

for x in job_config:
    print(x)


#-----------------------------------------------------------------------

print("+"*50)

#-----------------------------------------------------------------------

print("Q2 CODE--B")

numbers = [10, 20, 50, 60, 70]
for n in numbers:
    if n == 50:
        break
    print(n)

#-----------------------------------------------------------------------

print("+"*50)

#-----------------------------------------------------------------------

transactions = [
    {"id": 101, "amount": 50, "valid": True},
    {"id": 102, "amount": 0, "valid": False},
    {"id": 103, "amount": 100, "valid": True}
]

for t in transactions:
    if t["valid"] == False:
        print(f'Skipping invalid ID: {t["id"]}')
    else:
        print(f"Processing ID: {t["id"]} with amount ${t["amount"]}")