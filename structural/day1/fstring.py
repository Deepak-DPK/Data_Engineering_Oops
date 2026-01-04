folder = "sales_data"
date = "2024-01-01"
extension = "csv"

# Python injects the values directly into the string
file_path = f"/data/{folder}/{date}/report.{extension}"

print(file_path)
# Output: /data/sales_data/2024-01-01/report.csv


raw_count=500
status = "SUCCESS"

print(f"Pipeline finished. Status : {status}. Total rows processed: {raw_count}.")