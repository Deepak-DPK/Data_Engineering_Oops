import math

#Q1 
def multiply(a,b):
    mul = a*b
    return mul

print(multiply(4,6))



def great_user(name, title="Staff"):
    return f"Hello {title} {name}"

user_name=input("Enter you name: ")
user_role=input("Enter your role: ")

if user_role == "":
    Role=great_user(user_name)
else:
    Role = great_user(user_name,user_role)

print(Role)

