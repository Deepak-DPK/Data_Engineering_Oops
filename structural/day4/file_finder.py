import os

print("--- DEBUGGING PATHS ---")

# 1. Where does Python THINK it is?
print(f"My Current Working Directory is: {os.getcwd()}")

# 2. What files can Python ACTUALLY see here?
print(f"Files in this directory: {os.listdir()}")

# 3. Does the file exist? (True/False)
print(f"Can I find 'navigator.py'? : {'navigator.py' in os.listdir()}")