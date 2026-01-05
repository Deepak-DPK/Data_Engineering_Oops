# A list of server names

servers = ["server_prod", "server_dev", "server_test"]

for s in servers:

    print(f"pinging {s} ....")



print('-'*60)

"f.strip() (with no arguments) is safer "
"because it removes spaces, tabs (\t), and newlines (\n) all at once. "
"In data files, you often get hidden newline characters that break things."

files = [" data.csv", "report.csv", "backup.csv "]

for f in files:
    clean_data = f.strip()
    print(f"Processing: {clean_data}")

