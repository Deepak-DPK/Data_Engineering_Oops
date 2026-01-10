def calculate(price):
    tax = price * 0.10
    total = price * tax
    return total 

item_1=calculate(100)
item_2=calculate(340)

print(f"Total 1: {item_1}")
print(f"Total 2: {item_2}")



"""
(The Converter): You need a tool to convert temperature from Celsius to Fahrenheit for a sensor dataset. Formula: (C * 9/5) + 32

Define a function called to_fahrenheit(celsius).

Inside, do the math.

Return the result.

Call it with temp = 25 and print the result.

"""

def to_fahrenheit(celsius):
    formula=(celsius*9/5) + 32
    return formula

temp = to_fahrenheit(25)

print(f"The Fahrenheit of the celsius is : {temp}")