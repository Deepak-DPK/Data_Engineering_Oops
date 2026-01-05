rows = ["header", "row1_data", "row2_data"]

# i gets the index (0, 1, 2...)
# r gets the value ("header", "row1_data"...)
for i, r in enumerate(rows):
    print(f"Line {i}: {r}")

print('-'*50)

transactions = [100, 250, 0, 500]    #the value 0 is an error

for i,r in enumerate(transactions):
    if r==0:
        print(f"Error Found at Row {i}!")
    else:
        print(f"Line {i} : {r}")