# Day 3: Data Structures (Lists & Dictionaries)

## Key Concepts
- **Dictionaries:** Store data in Key-Value pairs (`{"id": 1, "name": "Alice"}`).
- **JSON Structure:** A List of Dictionaries (`[{}, {}, {}]`). This is the standard format for API and NoSQL data.
- **Loop Control:**
    - `break`: Emergency Stop. Exits the loop entirely.
    - `continue`: Skip. Jumps to the next item in the loop.

## Code Snippets

### 1. The JSON Pattern (Iterating Rows)
```python
users = [
        {"id": 101, "role": "admin"},
        {"id": 102, "role": "guest"}
]

for user in users:
        print(user["role"]) # Output: admin, guest
```

### 2. Modifying Data
```python
product = {"price": 100}
product["price"] = 120        # Update
product["tax"] = 120 * 0.10   # Add new key
```

### 3. The "Guard Clause" Pattern
```python
for item in data:
        if item == "BAD":
                continue  # Skip bad items immediately
        
        print("Processing good item...") # No 'else' needed
```