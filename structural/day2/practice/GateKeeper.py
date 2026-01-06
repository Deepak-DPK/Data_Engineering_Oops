"""
Exercise 1: The Data Gatekeeper
Concept: for loop + if/else You have a list of server response codes. responses = [200, 404, 200, 500, 200]

Task: Write a loop that checks each code:

IF the code is 200: Print "OK"

ELSE: Print "Alert: Failed Request"
"""

responses = [200, 404, 200, 500, 200]

for r in responses:
    if r == 200 :
        print("Ok")
    else:
        print("Alert: Failed Request")