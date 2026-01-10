# def make_password():
#     password = "123"  # Created INSIDE
#     return password

# make_password()
# print(password) # ERROR! NameError: name 'password' is not defined




def make_password():
    password = "123"  # Created INSIDE
    return password
    
    # Save the result into a global variable 'my_pass'
my_pass = make_password()
print(my_pass) # Works!



# ----------------------------------------------------------------

print("*"*40)

#-----------------------------------------------------------------

# def calculate_salary(base):
#     bonus = 500
#     return base + bonus

# calculate_salary(5000)
# # Error! 'bonus' is trapped inside the function.
# print(f"Total with bonus: {base + bonus}")


def calculate_salary(base):
    bonus = 500
    return base+bonus

total_bonus =calculate_salary(200)
print(f"The Total With Bonus: {total_bonus}")