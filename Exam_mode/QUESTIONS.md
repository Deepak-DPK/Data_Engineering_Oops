# Contract-Driven Data Ingestion Pipeline

## Problem Statement

Design a data ingestion platform that supports multiple data sources. The system must be extensible, safe, and pipeline-ready.

## Part A: Abstract Contract (Mandatory)

Create an abstract base class named `DataSource`.

**Requirements:**
- Use `ABC` from the `abc` module
- Define exactly three abstract methods: `connect()`, `validate()`, `read()`
- No implementation logic

## Part B: Base Implementation (Inheritance + Encapsulation)

Create a concrete class named `BaseSource` that:
- Inherits from `DataSource`
- Accepts `source_name` in constructor and stores it as a protected attribute
- Implements `connect()` → returns `"Connected to <source_name>"`
- Does NOT implement `validate()` or `read()`

## Part C: Concrete Sources (Polymorphism)

Create three concrete data sources: `PostgresSource`, `APIDataSource`, `S3Source`

Each must:
- Inherit from `BaseSource`
- Implement `validate()` and `read()`
- Return strings indicating which source is validating/reading

## Part D: Pipeline (System Design)

Write a function:
```python
def run_pipeline(source: DataSource):
```

It must:
- Call `connect()`, `validate()`, `read()`
- Return a dictionary with keys: `"source"`, `"connection"`, `"validation"`, `"data"`
- Use no type checks or conditional logic

## Part E: Execution

Instantiate one of each source type and run all three through the pipeline, printing results.
