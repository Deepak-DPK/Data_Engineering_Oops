

status_code = 404

if status_code == 200:
    print("Success : File Loading ....")
elif status_code == 404:
    print("Error : File Not Found.")
else:
    print("Unknown error : Alert the team")



print('-'*40)


amount = -50

if amount == 0:
    print('No Transaction')
elif amount < 0:
    print("Error : Negative Value")
else:
    print("Processing Transaction....")