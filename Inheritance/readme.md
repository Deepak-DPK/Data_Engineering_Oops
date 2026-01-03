# Day 1 Inheritance in Data Engineering Systems

Modern Data Engineering platforms rely on multiple connectors that interact with different storage systems and services. Although each connector targets a different technology, many of them share the same structural responsibilities such as handling hosts, maintaining connection metadata, and exposing a consistent connection interface.

Inheritance is used to model this shared structure while allowing each connector to specialize its behavior.

---

## Why Inheritance Is Needed

Without inheritance, every connector would reimplement:
- Host handling
- Connection setup logic
- Shared utility methods

This leads to duplicated code, inconsistent behavior, and higher maintenance cost. Inheritance eliminates this duplication by centralizing shared responsibilities in a parent class while allowing child classes to implement system-specific logic.

---

## Base Connector Design

The base connector defines common structure and enforces a connection contract. It is not meant to be executed directly.

```python
class BaseConnector:
    def __init__(self, host):
        self._host = host

    def connect(self):
        raise NotImplementedError("Subclasses must implement connect()")

    def get_host(self):
        return self._host
```

The protected `_host` attribute allows child classes to reuse connection metadata safely.
The `connect()` method defines a required behavior without providing an implementation.

---

## Specialized Connector Implementation

A concrete connector extends the base class and provides technology-specific behavior.

```python
class S3Connector(BaseConnector):
    def __init__(self, host, bucket_name):
        super().__init__(host)
        self.bucket_name = bucket_name

    def connect(self):
        return f"Connected to S3 bucket {self.bucket_name} at {self._host}"
```

This design ensures:

- Shared logic is reused
- Specialization is explicit
- No duplication of base functionality
