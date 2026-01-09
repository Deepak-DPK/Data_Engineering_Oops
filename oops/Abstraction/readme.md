# Day 3: Abstraction in Data Engineering

## 🎯 Learning Objectives
- Enforce contracts using abstract base classes (ABC)
- Separate interface definition from implementation
- Build extensible systems with guaranteed behavior
- Prevent instantiation of incomplete implementations

---

## 📚 Core Concepts

### 1. **Abstraction**
Defines **what** operations must exist without specifying **how** they work. Forces all implementations to provide required methods.

### 2. **ABC Module (Abstract Base Classes)**

| Component | Purpose | Effect |
|-----------|---------|--------|
| `ABC` | Base class marker | Prevents direct instantiation |
| `@abstractmethod` | Method decorator | Forces child implementation |
| Contract violation | Missing method in child | Raises `TypeError` at instantiation |

### 3. **Dependency Inversion Principle**
Pipelines depend on abstractions, not concrete classes. Enables switching implementations without code changes.

---

## 📂 Practice Files

### Core Implementation
- **[source.py](source.py)** - Abstract `DataSource` class with concrete Postgres implementation
- **[Systemdesign.py](Systemdesign.py)** - Complete pipeline with multiple sources (Postgres, API, S3)
- **[BaseStructure.py](BaseStructure.py)** - Additional abstraction examples

### Assessment
- **[../Exam_mode/QUESTIONS.md](../Exam_mode/QUESTIONS.md)** - Contract-driven data ingestion pipeline challenge
- **[../Exam_mode/contract_driven_data_ingestion_pipeline.py](../Exam_mode/contract_driven_data_ingestion_pipeline.py)** - Solution implementation

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| Abstract contracts | Unified connector API for Spark, Airflow, Databricks |
| Compile-time enforcement | Catch missing methods before production deployment |
| Dependency inversion | Replace data sources without pipeline refactoring |
| `ABC` pattern | Foundation for frameworks like SQLAlchemy, Apache Beam |
| Guaranteed behavior | Safe multi-team development on shared infrastructure |

**Pipeline Example:** Define abstract `DataSource` with `connect()` and `fetch()`. Engineers add MySQL, Snowflake, or BigQuery connectors independently—pipeline runs unchanged.

---

## 🔑 Quick Reference

**Abstract Contract:**
```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def connect(self): pass
```

**Concrete Implementation:**
```python
class PostgresSource(DataSource):
    def connect(self):
        return "Connected"
```

**Pipeline Using Abstraction:**
```python
def run_pipeline(source: DataSource):
    source.connect()
```

