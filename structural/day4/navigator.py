import os 


# Where is this script running?
current_path = os.getcwd()
print(f"I am working in : {current_path}")


# Show me the files
files = os.listdir()
print(f"Files found: {files}")