
# Day 2 Polymorphism in Data Engineering Pipelines

Data Engineering pipelines often need to ingest data from multiple sources such as files, databases, APIs, or object storage. Although the source types differ, the pipeline steps remain the same: validate the source and read the data.

Polymorphism allows pipelines to operate on different data sources through a single, consistent interface without conditional logic.

---

## The Core Idea

A pipeline should not need to know what type of data source it is handling.  
It should only rely on guaranteed behavior.

Polymorphism achieves this by ensuring different implementations respond to the same method names while providing different internal behavior.

---

## Defining the Common Interface

A base loader defines the required operations that every data source must support.

```python
class FileLoader:
    def read(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError
```

This interface establishes expectations without dictating how the operations are implemented.

## Concrete Loader Implementations

Each loader provides its own implementation while conforming to the same interface.

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

All loaders expose the same methods but behave differently internally.

## Pipeline Design Using Polymorphism

The pipeline interacts only with the interface, not with concrete implementations.

```python
def run_pipeline(loader: FileLoader):
    print(loader.read())
    print(loader.validate())
```

Usage remains identical regardless of the data source.

```python
run_pipeline(CSVLoader())
run_pipeline(JSONLoader())
run_pipeline(ParquetLoader())
```

The pipeline code never changes. Only the injected object changes.

## Why This Matters

This approach:

- Eliminates conditional branching
- Reduces coupling
- Improves extensibility
- Enables safe scaling of ingestion systems

Polymorphism ensures pipelines remain stable even as new data formats and sources are added.

---

If you want, next I can:
- Merge **Inheritance + Polymorphism + Abstraction** into a **single system-level README**
- Convert these into **real-world ETL architecture documentation**
- Or prepare an **exam-style design challenge** to validate mastery
