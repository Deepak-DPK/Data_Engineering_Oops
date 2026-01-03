# DAY 3 - Abstraction in Data Engineering Systems

## Abstraction in Data Engineering

In Data Engineering systems, pipelines must remain stable even when data sources change. A pipeline should not care how data is fetched, only what operations are guaranteed. This separation is achieved through abstraction.

Abstraction defines what a component must do, without exposing how it does it. This allows platform engineers to evolve implementations while pipeline code remains untouched.

### Core Idea

Every data source must support a fixed set of operations:

- Establish a connection
- Fetch data

If these operations are guaranteed, the pipeline can safely operate on any source.

Abstraction enforces this guarantee before execution, not at runtime.

## Defining the Contract (source.py)

The abstract base class defines the contract that all data sources must follow.
Any class that fails to implement this contract cannot exist in the system.

```python
from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass
```

This design ensures:

- The base class cannot be instantiated
- Every concrete data source must implement both methods
- Missing behavior is caught early, during development

## Concrete Data Sources (source.py)

Each data source provides its own implementation while respecting the same interface.

```python
class PostgresSource(DataSource):

    def connect(self):
        return "postgress connection"
    
    def fetch(self):
        return "fetched the source from the connection "


class APIDataSource(DataSource):

    def connect(self):
        return "Connect to ExternalAPI"
    
    def fetch(self):
        return "Fetched data from API"


class S3Source(DataSource):

    def connect(self):
        return "Connect to s3 bucket"
    
    def fetch(self):
        return "Fetched data from s3 bucket"
```

All sources:

- Share the same method names
- Hide implementation details
- Can be replaced or extended without breaking pipelines

## System Design: The Pipeline (systemdesign.py)

The pipeline depends only on the abstraction, not on concrete implementations.

```python
def run_pipeline(source: DataSource):
    connection_status = source.connect()
    data = source.fetch()

    return {
        "Connection": connection_status,
        "data": data
    }


p1 = PostgresSource()
a1 = APIDataSource()
s1 = S3Source()

print(run_pipeline(a1))
print(run_pipeline(p1))
print(run_pipeline(s1))
```

- The pipeline logic never changes
- Only the injected source changes

## Why This Matters

This approach provides:

- Strong guarantees about behavior
- Clean separation of responsibilities
- Safe extensibility
- Reduced coupling
- Production-grade stability

It is the foundation used by real Data Engineering frameworks where pipelines must remain reliable as systems grow.

## Key Points to Remember

- Abstraction defines what must exist, not how it works
- Pipelines should depend on abstract contracts
- Concrete implementations can change freely
- Errors are prevented early, not during execution
- This is essential for scalable Data Engineering systems
