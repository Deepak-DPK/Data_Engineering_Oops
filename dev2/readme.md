# Day 2 — Polymorphism in Data Engineering (Strict OOP)

## Objective
Understand and apply **polymorphism** in real-world **Data Engineering pipelines**, eliminating conditional logic and enabling scalable ingestion systems.

---

## Core Problem Polymorphism Solves

In Data Engineering, pipelines often ingest data from multiple sources:
- CSV
- JSON
- Parquet

Without polymorphism, pipelines rely on:
- `if / elif` chains
- format-specific branching
- fragile, unscalable code

**Polymorphism allows the same pipeline to work with different data sources using a single interface.**

---

## Key Definition (Engineering-Oriented)

> **Polymorphism allows a pipeline to operate on different data sources using the same method names, without knowing their concrete implementation.**

---

## Mental Model (Must Remember)

- **Same method name**
- **Different behavior**
- **Same pipeline code**

If pipeline logic checks object type → polymorphism is missing.

---

## Base Contract (FileLoader)

```python
class FileLoader:
    def read(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError
```

### Why This Exists

- Enforces a strict contract
- Guarantees every loader supports required operations
- Prevents silent runtime failures

---

## Concrete Loaders (Polymorphic Implementations)

```python
class CSVLoader(FileLoader):
    def read(self):
        return "Reading CSV data"

    def validate(self):
        return "CSV schema validated"


class JSONLoader(FileLoader):
    def read(self):
        return "Reading JSON data"

    def validate(self):
        return "JSON structure validated"


class ParquetLoader(FileLoader):
    def read(self):
        return "Reading Parquet data"

    def validate(self):
        return "Parquet metadata validated"
```

---

## Polymorphic Pipeline (No Conditionals)

```python
def run_pipeline(loader: FileLoader):
    print(loader.read())
    print(loader.validate())
```

### Usage

```python
run_pipeline(CSVLoader())
run_pipeline(JSONLoader())
run_pipeline(ParquetLoader())
```

- Pipeline code **never changes**
- Only the object changes
- This is **true polymorphism**

---

## Critical Insight: Duck Typing vs Polymorphism

### Duck Typing

- Python allows objects with matching methods to work
- Flexible but unsafe in large systems

### Polymorphism with Inheritance

- Enforces contracts
- Safe for production pipelines
- Required for large DE codebases

> **Duck typing enables flexibility. Inheritance + polymorphism enable safety and scale.**

---

## Professional Rules Locked Today

1. Pipelines must not branch on data source type
2. Base classes define **what must exist**, not how
3. Child classes provide **format-specific behavior**
4. `raise NotImplementedError` enforces contracts
5. Polymorphism is mandatory for scalable ingestion systems

---

## Interview-Ready One-Liner

> "Polymorphism allows a single data pipeline to operate on multiple data sources using a common interface, eliminating conditional logic and improving scalability."

---

## Day 2 Status

- Polymorphism: ✅ Mastered
- Duck typing vs enforced contracts: ✅ Clear
- Data Engineering application: ✅ Real-world
- Ready to proceed to: **Abstraction**

