
'''
Let's get straight back to work. 
You were about to fix this code 
to meet PEP8 Data Engineering 
Standards (snake_case for variables, ALL_CAPS for constants).

FileLoc = "/data/users.csv"
MaxLimit = 100
n = "John Doe"
 '''


file_location = "/data/users.csv"  # snake_case for variables
MAX_LIMIT = 100                    # ALL_CAPS for constants
user_name = "John Doe"             # Descriptive snake_case


"""
Why this matters: When you see FileLocation in a Python script, 
you assume it's a blueprint (Class).
When you see file_location, you know it's data (Variable).
"""


"""
Q2. Data Cleaning You have a raw price string from a website: raw_price = "$$1,200.50" Write code to:

Strip the $$.

Slice out just the 200.50 (ignoring the 1, for now to keep it simple, or handle it if you know how). Hint: Just slice from the correct index.

"""



raw_price = "$$1,200.50"

whole_price = raw_price.strip("$")

new_price = whole_price[2:]

print(new_price)



"""
Q3. f-String Logic Create a variable table = "users". Write an f-string that prints: "SELECT * FROM users WHERE active = 1;"
"""

table = "users"

print(f"SELECT * FROM {table} WHERE active = 1;")


#QUESTION 1 

"""
Day 1 Mini-Exam (3 Questions)
Q1. Debugging & PEP8 The following code crashes and looks unprofessional. Rewrite it using strict PEP8 and fix the logic error (trying to add string to integer).

Python

UserAge = "25"
Next_Year = UserAge + 1
print(Next_Year)
"""

user_age = 25
next_year = user_age + 1 
print(user_age)