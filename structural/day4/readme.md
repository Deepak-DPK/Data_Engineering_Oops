# Day 4: Modules, Libraries & File I/O

## 🎯 Learning Objectives
- Understand how to import and use Python standard library modules
- Work with file system operations using the `os` module
- Handle date/time operations for logging and timestamping
- Perform safe file I/O operations using context managers
- Apply these concepts to real Data Engineering scenarios

---

## 📚 Core Concepts

### 1. **Module Imports**
- `import module` - Load entire module (access via `module.function()`)
- `from module import function` - Import specific items directly

### 2. **Essential Modules**
| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `os` | File system navigation | `getcwd()`, `listdir()` |
| `datetime` | Date/time operations | `now()`, `strftime()` |
| `math` | Mathematical operations | `sqrt()`, `pi` |
| `random` | Random selection/generation | `choice()` |

### 3. **File I/O Best Practices**
- Always use `with open()` context manager (auto-closes files)
- **Write mode (`"w"`)**: Creates/overwrites file
- **Read mode (`"r"`)**: Reads existing file (fails if missing)

---

## 📂 Practice Files

### Module Basics
- **[modules_libraries.py](modules_libraries.py)** - Learn `import` vs `from...import` syntax with math examples

### File System Operations
- **[navigator.py](navigator.py)** - Find your current working directory and list files
- **[file_finder.py](file_finder.py)** - Debug path issues and verify file existence

### Date & Time
- **[The_Time_keeper.py](The_Time_keeper.py)** - Capture and format timestamps (`strftime`)
- **[The_Logger.py](The_Logger.py)** - Build timestamped log messages for ETL jobs

### File I/O
- **[file_io.py](file_io.py)** - Write and read files safely using context managers

### Random Operations
- **[random_module.py](random_module.py)** - Simulate random server selection

### Validation Exercise
- **[The_File_checker.py](The_File_checker.py)** - Check if critical configuration files exist

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| **File paths** | Locate data files in pipelines |
| **Timestamps** | Track "when did data arrive?" and pipeline execution times |
| **File I/O** | Read CSVs, write logs, save processed data |
| **Config checks** | Validate required files exist before pipeline starts |
| **Random sampling** | Test data sampling, load balancing |

---

## 🔑 Quick Reference

**DateTime Format Codes:**
- `%Y` - Year (2026)
- `%m` - Month (01)  
- `%d` - Day (09)
- `%H:%M:%S` - Hour:Minute:Second

**Common Patterns:**
```python
# Safe file handling
with open("file.txt", "w") as f:
    f.write("data")

# Timestamp for logs
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

