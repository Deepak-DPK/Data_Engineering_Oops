# Day 3: Dictionaries, JSON Patterns & Loop Control

## 🎯 Learning Objectives
- Master dictionary operations for key-value data manipulation
- Understand JSON structure (list of dictionaries) as the standard data format
- Apply `break` and `continue` for efficient loop control
- Build ETL-style data processing logic with filtering and transformation

---

## 📚 Core Concepts

### 1. **Dictionaries**
Key-value pairs that map field names to values. Essential for representing records, configurations, and API responses.

### 2. **JSON Pattern (List of Dictionaries)**
The universal format for structured data in APIs, NoSQL databases, and data pipelines. Each dictionary represents a row/record.

### 3. **Loop Control Statements**

| Statement | Purpose | Use Case |
|-----------|---------|----------|
| `break` | Exit loop immediately | Stop processing when end marker found |
| `continue` | Skip current iteration | Skip invalid/corrupted records |

---

## 📂 Practice Files

### Core Dictionary Operations
- **[dict.py](dict.py)** - Dictionary basics and nested access patterns
- **[dict_practice.py](dict_practice.py)** - Hands-on dictionary manipulation exercises
- **[update_dict.py](update_dict.py)** - Modifying and adding key-value pairs

### JSON Processing
- **[json_pattern.py](json_pattern.py)** - Processing lists of dictionaries (row-based iteration)
- **[json_practice.py](json_practice.py)** - Real-world JSON data filtering exercises

### Loop Control
- **[break.py](break.py)** - Using break/continue for data validation and error handling
- **[practice1.py](practice1.py)** - Combined practice with loops and dictionaries

### Assessment
- **[Mini_Test.py](Mini_Test.py)** - Day 3 capstone: Build an ETL script with filtering logic

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| Dictionaries | Configuration files, metadata storage, record representation |
| JSON Pattern | API responses, NoSQL documents, event streams, log parsing |
| `break` | Stop reading file when EOF marker found, circuit breaker pattern |
| `continue` | Skip malformed records, filter out test data, handle nulls |
| List of Dicts | Standard format for Spark DataFrames, Pandas, database query results |

**Pipeline Example:** Read 10,000 user events, skip invalid records (`continue`), stop early if critical error found (`break`), transform valid data into dictionaries for database insert.

---

## 🔑 Quick Reference

**Accessing Nested Data:**
```python
users[0]["name"]  # List index, then dict key
```

**Update/Add Keys:**
```python
record["price"] = 150      # Update
record["tax"] = 15.0       # Add
```

**Guard Clause Pattern:**
```python
if record["status"] == "invalid":
    continue  # Skip immediately
```