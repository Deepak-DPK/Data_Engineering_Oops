'[start : stop]'

text = 'PYTHON'

'Crucial Rule: The start index is included, but the stop index is excluded'

print(text[0])  #it returns p because indexing starts from zero

print(text[ 0 :   ])  #if we enter only start value and leave stop value  means it goes till the end of index

print(text[   : 3 ])   # if we leave start value and enter stop value means it starts from index 0 to stop value(index stop-1 which is 2)



print('-'*30)


raw_file = "   user_data_2024.csv   "

# Step 1: Clean the spaces
clean_name = raw_file.strip()  # "user_data_2024.csv"

# Step 2: Extract the year (Slicing)
# "user_data_" is 10 chars long (indices 0-9). Year starts at 10.
year = clean_name[10:14]       # "2024"

print(year)


"""
3. Essential Cleaning Methods

.strip(): Removes leading/trailing whitespace (spaces, tabs, newlines).

.upper() / .lower(): Standardizes case.

.replace("old", "new"): Swaps characters.

"""

product_id = "##ID-9950##"

clean_product_id = product_id.strip('#')


print(clean_product_id[3:])