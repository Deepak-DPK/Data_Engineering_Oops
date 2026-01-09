# Day 1: Inheritance in Data Engineering

## 🎯 Learning Objectives
- Eliminate code duplication through inheritance hierarchies
- Implement shared functionality in base classes
- Use `super()` to extend parent class behavior
- Apply protected attributes for safe data sharing

---

## 📚 Core Concepts

### 1. **Inheritance**
Child classes inherit attributes and methods from parent classes, eliminating duplication while enabling specialization.

### 2. **Access Modifiers**

| Convention | Visibility | Use Case |
|------------|------------|----------|
| `self.attr` | Public | External access allowed |
| `self._attr` | Protected | Child class access (convention) |
| `self.__attr` | Private | Name mangling, restricted access |

### 3. **Method Resolution**

```python
super().__init__(args)  # Call parent constructor
```

Ensures parent initialization runs before child-specific logic.

---

## 📂 Practice Files

- **[GenricConnector.py](GenricConnector.py)** - Base connector with protected `_host` and S3 specialization
- **[DatabaseConnector.py](DatabaseConnector.py)** - Private attributes for secure credential handling

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| Base connector class | Shared logic for JDBC, S3, Kafka, SFTP connectors |
| Protected attributes | Connection metadata reused by child connectors |
| `super()` | Extending authentication logic from base to specialized connectors |
| Private attributes | Securing credentials (passwords, API keys) |
| Inheritance hierarchy | Building connector libraries (e.g., PySpark data sources) |

**Real Example:** Apache Spark's `DataSource` API uses inheritance. Each connector (JDBC, Parquet, Delta) extends base functionality while adding format-specific reading logic.

---

## 🔑 Quick Reference

**Base Class with Protected Attribute:**
```python
class BaseConnector:
    def __init__(self, host):
        self._host = host
```

**Child Class Using super():**
```python
class S3Connector(BaseConnector):
    def __init__(self, host, bucket):
        super().__init__(host)
        self.bucket = bucket
```
