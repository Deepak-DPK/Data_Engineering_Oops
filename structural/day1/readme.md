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