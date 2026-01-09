"""  
In Data Engineering, "When" is just as important as "What".

"When did the data arrive?"

"How long did the process take?"

"Generate a filename for today: sales_2026_01_09.csv"

We use the datetime module. 

"""

from datetime import datetime

now=datetime.now()
print(now)




"""
2. Formatting Time (String Format Time - strftime) We need to make it readable or useful for filenames. We use special codes:

%Y = Year (2026)

%m = Month (01)

%d = Day (09)

%H:%M:%S = Hour:Minute:Second

""" 

clean_date=now.strftime("%Y-%m-%d")

print(f"Today is : {clean_date}")