"""  
Your Task (The Loop Master Challenge): You have a list of sensor readings: readings = [15, 20, 999, 25, -999, 30]

Write a loop that checks every number:

IF reading is 999: Print "Sensor Error, skipping..." and use continue.

IF reading is -999: Print "Fatal Crash, stopping..." and use break.

ELSE: Print "Reading: {value}".

"""

readings = [15, 20, 999, 25, -999, 30]

for x in readings:

    if x == 999:
        print("Sensor Error, Skipping...")
        continue

    if x == -999:
        print("Fatal Crash, stopping...")
        break

    else:
        print(f"Reading: {x}")