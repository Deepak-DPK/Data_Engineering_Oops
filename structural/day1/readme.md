# Day 1: Python Foundations for Data Engineering

## Key Concepts
- **Memory Management:** Variables are labels, not boxes.
- **Naming:** strict `snake_case` for variables, `ALL_CAPS` for constants.
- **Strings:**
  - `text.strip()` removes whitespace.
  - `text[0:4]` slices the first 4 characters.
- **f-strings:** `f"Processing {filename}..."` is the standard for logging.

## Code Snippets

### 1. The Reference Trap
```python
a = [1, 2, 3]
b = a
b.append(4)
# a is now [1, 2, 3, 4] because a and b point to the same object.
```

### 2. Cleaning Data
```python
raw_id = "##ID-900##"
clean_id = raw_id.strip("#")[3:]  # Result: "900"
```

### 3. Type Safety
```python
age_str = "25"
# age_str + 1  <-- CRASH
age_int = int(age_str) + 1  # OK
```

---

**Day 1 is closed.**

**Next Session:** Day 2 - Control Flow (Logic that decides *what* to do with the data).

**Action:** Type **"Day 2"** whenever you are ready to start the next session (tomorrow).