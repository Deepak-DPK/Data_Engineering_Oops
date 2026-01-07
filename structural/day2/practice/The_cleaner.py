"""  
Exercise 3: The Cleaner
Concept: for loop + string methods You have a list of dirty column names from a CSV. columns = [" user_id ", " email ", "timestamp"]

Task: Write a loop that:

Strips the whitespace from every item.

Prints the clean version in valid uppercase (e.g., "USER_ID"). (Hint: You can chain methods like .strip().upper())

"""


columns = [" user_id ", " email ", "timestamp"]

for c in columns:
    print(c.strip().upper())