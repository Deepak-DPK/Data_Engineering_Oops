# Day 2: Control Flow (Logic & Loops)

## Key Concepts
- **Gatekeeping:** Use `if/elif/else` to filter bad data before processing.
- **Iteration:** `for item in list:` is the standard way to process datasets.
- **Index Tracking:** Use `enumerate()` when you need the row number.

## Code Snippets

### 1. The Data Validator (Gatekeeper)
```python
amount = -50
if amount < 0:
    print("Error: Negative")
elif amount == 0:
    print("Warning: Zero")
else:
    print("Valid")
```

### 2. Processing Lists
```python
files = [" data.csv ", " report.csv "]
for f in files:
    print(f.strip()) # Output: "data.csv", "report.csv"
```

### 3. Finding Errors with Enumerate
```python
transactions = [100, 0, 500]
for i, value in enumerate(transactions):
    if value == 0:
        print(f"Row {i} has a Zero-Value Error!")
```

---

**Day 2 is closed.**  
**Next Session:** We will immediately finish the **Loop Master Challenge** (`break`/`continue`) and take the **Day 2 Exam**, then move to **Day 3**.

**Action:** Type **"Day 3"** (or "Resume Day 2") when you are ready to pick this up tomorrow.