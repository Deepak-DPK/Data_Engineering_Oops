import os


"""
"w" mode is powerful: If the file doesn't exist, Python creates it for you automatically.

"r" mode is strict: If the file is missing, it crashes.

"""

# STEP 1: Create and Write the file
# "w" creates the file if it doesn't exist
with open("welcome.txt", "w") as f:
    f.write("Hello Data Engineer")
    print("File created successfully.")

# STEP 2: Now Read it back
# This works now because Step 1 created it!
with open("welcome.txt", "r") as f:
    content = f.read()
    print(f"File Content: {content}")


with open("hello_word", "w") as s:
    s.write("Hello World WELCOME")
    print("File created successfully")

with open("hello_word","r") as f:
    print(f"Filed Content : {f.read()}")
