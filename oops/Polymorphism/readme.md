
# Day 2: Polymorphism in Data Engineering

## 🎯 Learning Objectives
- Design unified interfaces for heterogeneous data sources
- Implement polymorphic behavior with method overriding
- Build type-safe pipelines that accept multiple implementations
- Eliminate conditional branching using interface-based design

---

## 📚 Core Concepts

### 1. **Polymorphism**
"Many forms, one interface." Different classes provide different implementations of the same method, allowing pipelines to treat them uniformly without type checking.

### 2. **Interface Design Pattern**

| Component | Role | Benefit |
|-----------|------|----------|
| Base class | Defines method signatures | Enforces contract |
| Child classes | Provide specific implementations | Behavioral diversity |
| Pipeline function | Calls methods via interface | No conditional logic |

### 3. **Type Hints for Safety**
Using `loader: FileLoader` ensures only valid objects are passed, catching errors at design time.

---

## 📂 Practice Files

- **[FILE_LOADER.PY](FILE_LOADER.PY)** - Basic polymorphism: single method (`read()`) with multiple implementations
- **[LOAD_VALIDATE.py](LOAD_VALIDATE.py)** - Complete file loader system with validation and reading operations

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| Polymorphic loaders | Unified ingestion logic for CSV, JSON, Parquet, Avro formats |
| Interface-based design | Plug-and-play connectors (Kafka, S3, JDBC, SFTP) |
| No conditional logic | Cleaner pipelines, easier testing, reduced complexity |
| Type hints | Early error detection, better IDE support, self-documenting code |
| Method overriding | Format-specific validation without branching |

**Pipeline Example:** A single `run_pipeline(loader)` function processes any file format. Adding support for Avro or ORC requires only creating a new class—no pipeline changes needed.

---

## 🔑 Quick Reference

**Base Interface:**
```python
class FileLoader:
    def read(self):
        raise NotImplementedError
```

**Polymorphic Pipeline:**
```python
def run_pipeline(loader: FileLoader):
    data = loader.read()
```
