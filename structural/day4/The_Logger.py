from datetime import datetime


"""
( The Logger): You are building a logging system.

Import datetime from datetime.

Get the current time.

Format it to look like this: 09/01/2026 (Day/Month/Year).

Print a log message: " [Date] : ETL Job Started".

"""

current_time = datetime.now()
print(current_time)

format_clean =current_time.strftime("%d/%m/%Y")
print(format_clean)
print(f"{format_clean} : ETL Job Started")