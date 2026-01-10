# Day 5: Functions (Reusable Logic)

## 🎯 Learning Objectives
- Define reusable functions with clear inputs, outputs, and defaults
- Control scope so helper variables stay local and safe
- Refactor repeated logic into single-call utilities
- Apply small functions to ETL-style loops for cleaner data pipelines

---

## 📚 Core Concepts

| Concept | Why it matters | Quick note |
|---------|----------------|------------|
| Function definition | Encapsulates reusable behavior | def name(args): return value |
| Return values | Moves data back to callers | Avoid silent None by always returning |
| Default arguments | Makes APIs flexible without overloading | Keep defaults immutable |
| Local scope | Prevents cross-function side effects | Variables declared inside stay inside |
| Refactoring | Reduces duplication and bugs | Replace copy-paste with single helpers |

---

## 📂 Practice Files
- **[structural/day5/broken_normal.py](structural/day5/broken_normal.py)** - Demonstrates local scope, returning values, and bonus calculation
- **[structural/day5/Database_connector.py](structural/day5/Database_connector.py)** - Uses defaults for connection settings and formatted responses
- **[structural/day5/etl_arg.py](structural/day5/etl_arg.py)** - Shows default parameters while formatting prices
- **[structural/day5/fun_cal.py](structural/day5/fun_cal.py)** - Calculates with returns and converts Celsius to Fahrenheit
- **[structural/day5/mini_exam.py](structural/day5/mini_exam.py)** - Implements multiplication plus flexible greeting with optional title
- **[structural/day5/mini_ exam2.py](structural/day5/mini_%20exam2.py)** - Cleans a list of user names via strip-and-upper helper inside a loop
- **[structural/day5/refactoring.py](structural/day5/refactoring.py)** - Converts transaction rows to USD with a converter function inside a loop

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-world application |
|---------|------------------------|
| Defaults and formatting | Consistent connection strings, currency/price rendering |
| Scope discipline | Keeps per-row temp variables from leaking across batches |
| Refactoring helpers | Shared cleaning or conversion logic across pipelines |
| Loop + function ETL | Map-style transforms for rows, events, or records |

---

## 🔑 Quick Reference

**Function with default and return**
```python
def connect(host="localhost", port=5432):
    return f"Connected to {host}:{port}"
```

**Loop + helper for ETL-style clean**
```python
def clean(name):
    return name.strip().upper()
for u in users:
    print(clean(u))
```

---

Save this summary as day5_summary.md alongside your Day 5 materials.Day 5 README Save this file as day5_summary.md in your repository.

Markdown

# Day 5: Functions (Reusable Logic)

## Key Concepts
- **Function Definition:** `def name(input):` creates a tool.
- **Return:** Sends data back to the main program. Without it, data is lost.
- **Scope:** Variables inside functions are local.
- **Refactoring:** Converting repetitive code into a single function call.

## Code Snippets

### 1. Basic Function with Return
```python
def add_tax(price):
    return price * 1.10

total = add_tax(100) # total is 110.0
2. Default Arguments
Python

def connect(host="localhost"):
    print(f"Connecting to {host}")

connect()          # Uses "localhost"
connect("prod-db") # Uses "prod-db"
3. The ETL Pattern (Loop + Function)
Python

def clean(row):
    return row.strip().upper()

data = ["  raw ", "data  "]
for item in data:
    print(clean(item))