"""   
Your Task (The File Checker): You are writing a script that checks if a required configuration file exists.

Import os.

Create a "fake" list of files to simulate reading a folder: files = ["data.csv", "config.yaml", "script.py"] (Note: We are faking this list because we can't see your real hard drive, but the logic is the same).

Write logic:

IF "config.yaml" is inside the files list: Print "Configuration Found.".

ELSE: Print "Critical Error: Config missing!".


"""




import os 


files=["data.csv", "config.yaml", "script.py"]

x="config.yaml"

if x in files:
    print("Configuration Found.")
else:
    print("Critical Error: Config Missing!")