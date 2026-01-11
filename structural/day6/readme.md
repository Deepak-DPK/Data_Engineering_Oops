# Day 6: Pandas - The Data Engineer's Excel

## 🎯 Learning Objectives
- Understand DataFrame structure and manipulation
- Master vectorized operations for performance optimization
- Learn data filtering and selection techniques
- Create, transform, and export DataFrames efficiently
- Apply Pandas operations to real-world data engineering tasks

---

## 📚 Core Concepts

### 1. **DataFrame**
A two-dimensional labeled data structure with columns of potentially different types. Think of it as a powerful in-memory table that's the foundation of data transformation pipelines.

### 2. **Vectorization**
Performing operations on entire columns/arrays at once using optimized C code under the hood. Eliminates the need for Python loops, resulting in 10-100x speed improvements.

### 3. **Data Selection & Filtering**
Boolean indexing allows you to select rows based on conditions, enabling data quality checks and subset extraction for downstream processing.

---

## 📊 Key Operations Table

| Operation | Purpose | Example Syntax |
|-----------|---------|----------------|
| `pd.DataFrame()` | Create DataFrame from dict/list | `df = pd.DataFrame(data)` |
| `df.head(n)` | Preview first n rows | `df.head(5)` |
| `df.shape` | Get dimensions (rows, cols) | `rows, cols = df.shape` |
| `df[condition]` | Filter rows by condition | `df[df['price'] > 100]` |
| `df['new_col']` | Create/modify column | `df['total'] = df['a'] * df['b']` |
| `df.to_csv()` | Export to CSV file | `df.to_csv('output.csv')` |

---

## 📂 Practice Files

### Core Learning
- **[pandas_first_chapter.ipynb](pandas_first_chapter.ipynb)** - Interactive notebook covering DataFrame creation, inspection, filtering, and transformation operations

### Sample Data
- **[inventory_report.csv](inventory_report.csv)** - Sample dataset for practicing Pandas operations and data manipulation techniques

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| **DataFrame Operations** | Transform raw data from APIs/databases before loading into warehouses |
| **Vectorization** | Process millions of rows efficiently in ETL pipelines without memory overflow |
| **Boolean Filtering** | Apply data quality rules and business logic (e.g., remove invalid records) |
| **Column Creation** | Derive metrics and calculated fields (revenue = price × quantity) |
| **CSV Export** | Generate reports and intermediate files for downstream systems |
| **Data Inspection** | Quickly validate data structure and content during pipeline development |

---

## 🔑 Quick Reference

**Basic DataFrame Workflow:**
```python
df = pd.DataFrame(data)          # Create
df.head()                         # Inspect
df_filtered = df[df['col'] > 10]  # Filter
df['new'] = df['a'] * df['b']    # Transform
df.to_csv('output.csv')          # Export
```

**Common Patterns:**
- **Load:** `pd.read_csv('file.csv')`
- **Filter:** `df[df['status'] == 'active']`
- **Multiple conditions:** `df[(df['a'] > 10) & (df['b'] < 20)]`
- **Sort:** `df.sort_values('column')`
- **Group:** `df.groupby('category').sum()`