"""  
Exercise 2: The Index Hunter
Concept: enumerate() + == You have a list of daily sales figures. One day has missing data (marked as 0). sales = [5000, 4500, 0, 6000]

Task: Use enumerate to find the zero.

IF the value is 0: Print "Missing data at Day {index}"

ELSE: Print "Day {index}: ${value}"
"""

sales = [5000, 4500, 0, 6000]

for i,r in enumerate(sales):
        if r == 0:
                print(f"Missing data at Day {i}")
        else:
                print(f"Day {i}: ${r}")