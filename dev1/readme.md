# Day 1 — Inheritance in Data Engineering (STRICT OOP)

## Objective
Learn and apply **Inheritance** in Python using **real Data Engineering systems**, focusing on reusable connectors and scalable pipeline design.

This day bridges **Encapsulation → Polymorphism** by introducing structured code reuse.

---

## Problem Inheritance Solves in Data Engineering

In real-world Data Engineering systems, we build multiple connectors:
- PostgresConnector
- MySQLConnector
- S3Connector
- APIConnector

Without inheritance:
- Credential logic is duplicated
- Host handling is repeated
- Bugs multiply across connectors
- Maintenance becomes expensive

**Inheritance eliminates duplication while preserving specialization.**

---

## Engineering Definition (Not Textbook)

> **Inheritance allows multiple connectors to share common structure and behavior through a parent class, while implementing source-specific logic in child classes.**

---

## Mental Model (Must Remember)

- **Parent class** → shared structure + contract
- **Child class** → technology-specific behavior

Inheritance exists **only when systems share structure**.

---

## Encapsulation Review (Foundation for Inheritance)

### Secure Connector Design (from `DatabaseConnector.py`)

```python
class DatabaseConnector:
    def __init__(self,host,user,password):
        self.__host = host
        self.__user = user
        self.__password = password
    
    def connect(self):
        return f"Connected to {self.__host}"
    
    def get_host(self):
        return self.__host
    
host=input("Enter the Host name : ")
user=input("Enter the user name: ")
password =input("Enter the password: ")

d1=DatabaseConnector(host,user,password)

print('-'*20)

print(d1.connect())
print(d1.get_host())
```

### Why This Matters

- Credentials are protected
- Access is controlled
- Safe to extend using inheritance

---

## Base Class Design (Inheritance Entry Point)

### `BaseConnector` (from `GenricConnector.py`)

```python
class BaseConnector:
    def __init__(self,host):
        self._host = host  #protected not private
    
    def connect(self):
        raise NotImplementedError("subclasses must implement connect()")
    
    def get_host(self):
        return self._host
```

### Key Design Decisions

- `_host` is **protected**, not private
- `connect()` defines a **contract**, not behavior
- Base classes should **not be instantiated directly**

---

## Why `raise NotImplementedError` Exists

```python
raise NotImplementedError
```

Purpose:

- Enforces implementation in child classes
- Fails fast if contract is violated
- Prevents silent pipeline failures

> **Base classes define rules, not execution.**

---

## Child Class — S3Connector (from `GenricConnector.py`)

```python
class S3Connector(BaseConnector):
    def __init__(self, host, bucket_name):
        super().__init__(host)
        self.bucket_name = bucket_name
    
    def connect(self):
        return f"Connected to s3 bucket {self.bucket_name} at {self._host}"
```

### What This Demonstrates

- `super()` reuses parent initialization
- Child adds only what is unique
- No duplication
- Clean specialization

---

## Correct Usage Pattern (from `GenricConnector.py`)

```python
host = input("Enter the Host name: ")
bucket_name=input("Enter the bucket name : ")

s1=S3Connector(host,bucket_name)

print('*'*15)

print(s1.get_host())
print(s1.connect())
```

### Important Rule

- **Do NOT instantiate `BaseConnector`**
- Always use a concrete child class

---

## Common Mistakes Avoided

- ❌ Using global variables inside constructors
- ❌ Instantiating base classes
- ❌ Making base attributes private (`__attr`)
- ❌ Duplicating shared logic in child classes

---

## Professional Rules Locked on Day 1

1. Use inheritance only when structure is shared
2. Base classes define **contracts**
3. Child classes implement **technology-specific logic**
4. Use `super()` to preserve parent guarantees
5. Protected attributes (`_attr`) enable safe extension
6. `raise NotImplementedError` enforces discipline

---

## Interview-Ready One-Liner

> “Inheritance allows Data Engineering connectors to share common structure through a base class while implementing source-specific behavior in child classes.”

---

## Day 1 Status

- Encapsulation → Inheritance transition: ✅
- Base vs Child responsibility: ✅
- Contract enforcement using `raise`: ✅
- Data Engineering–specific application: ✅
- Ready for Polymorphism: ✅

---

## Bridge to Day 1 (Dev2 Code Reference)

Inheritance gives the shared contract. Polymorphism is where the pipeline code stays the same while the object changes.

Example from `dev2/LOAD_VALIDATE.py` (file loaders + validation):

```python
#base class
class FileLoader:
    def read(self):
        raise NotImplementedError
    
    def validate(self):
        raise NotImplementedError

# child class
class CSVLoader(FileLoader):
    def read(self):
        return "Reading csv data"
    def validate(self):
        return "CSV schema Validated"

class JSONLoader(FileLoader):
    def read(self):
        return "Reading json data"
    def validate(self):
        return "JSON structure is validated"

class ParaquetLoader(FileLoader):
    def read(self):
        return "Reading paraquet data"
    def validate(self):
        return "paraquet metadata is validated"


def run_pipeline(loader : FileLoader):
    print(loader.read())
    print(loader.validate())
```
