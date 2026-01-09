# Day 2: Control Flow (Conditionals & Loops)

## 🎯 Learning Objectives
- Implement conditional logic for data validation and filtering
- Process collections efficiently using `for` loops
- Track row positions with `enumerate()` for error reporting
- Build data cleaning and validation pipelines

---

## 📚 Core Concepts

### 1. **Conditional Logic (if/elif/else)**
Gatekeeper pattern that validates data before processing. Essential for handling API response codes, null checks, and business rule enforcement.

### 2. **For Loops**
The standard iteration mechanism for processing lists, files, and datasets. Enables batch operations on collections.

### 3. **Enumerate Function**

| Use Case | Pattern | When to Use |
|----------|---------|-------------|
| Simple iteration | `for item in list:` | Process values only |
| With index | `for i, item in enumerate(list):` | Need row numbers for logging/errors |

---

## 📂 Practice Files

### Core Concepts
- **[if_else.py](if_else.py)** - Conditional logic for status codes and validation
- **[for_loop.py](for_loop.py)** - Iterating over lists and string cleaning operations
- **[enumerateloop.py](enumerateloop.py)** - Index tracking and error detection

### Practice Exercises
- **[practice/GateKeeper.py](practice/GateKeeper.py)** - Response code validation with conditionals
- **[practice/enumeratepractice.py](practice/enumeratepractice.py)** - Finding missing data with index tracking
- **[practice/The_cleaner.py](practice/The_cleaner.py)** - Cleaning dirty column names with string methods

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| `if/elif/else` | API response handling, data quality checks, partition routing |
| `for` loop | Batch file processing, row-by-row transformations, bulk inserts |
| `enumerate()` | Error logging with line numbers, audit trails, checkpoint tracking |
| `.strip()` | Cleaning CSV headers, removing whitespace from user input |
| Validation patterns | Reject invalid records before database writes, avoid downstream errors |

**Pipeline Example:** Read 100 CSV files, skip empty files (`if`), clean column names (`.strip()`), log processing status with file index (`enumerate`).

---

## 🔑 Quick Reference

**Conditional Validation:**
```python
if status == 200:
    process()
elif status == 404:
    log_error()
```

**Index + Value Iteration:**
```python
for i, row in enumerate(data):
    print(f"Row {i}: {row}")
```