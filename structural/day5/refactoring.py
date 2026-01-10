"""   
Rewrite this entire script using a Function and a Loop.

Define a function clean_user(name) that does the stripping and uppercasing and returns the result.

Create a list: users = [" alice ", " bob ", " charlie"].

Loop through the list.

Inside the loop, call your function and print the result.

"""

def clean_user(name):
    return name.strip().upper()

users = [" alice ", " bob ", " charlie"]

for u in users:
    result = clean_user(u)
    print(result)

