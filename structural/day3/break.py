# Processing a list of IDs.
# -1 indicates "End of File" (Stop everything).
# 0 indicates "Bad Data" (Skip this one).
ids = [101, 0, 102, -1, 103]

for x in ids:
    if x == 0:
        print("Skipping bad row...")
        continue  # Jumps to the next iteration immediately.
    
    if x == -1:
        print("End of file marker found. Stopping.")
        break     # Kills the loop completely.
    
    print(f"Processing ID: {x}")

# Output:
# Processing ID: 101
# Skipping bad row...
# Processing ID: 102
# End of file marker found. Stopping.