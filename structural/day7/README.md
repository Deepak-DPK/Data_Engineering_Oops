# Day 7: Data Cleaning & Missing Value Handling

## 🎯 Learning Objectives
- Detect and quantify missing values in datasets
- Apply strategic techniques to handle null values (drop vs fill)
- Generate synthetic datasets with missing data for practice
- Implement selective filling strategies for different columns
- Understand when to remove vs impute missing data

---

## 📚 Core Concepts

### 1. **Missing Data Detection**
Real-world datasets often contain missing values (NaN/null) that must be identified and handled before analysis. Pandas provides powerful methods to detect and quantify these gaps in data quality.

### 2. **Data Cleaning Strategies**

| Strategy | Method | When to Use |
|----------|--------|-------------|
| **Drop Rows** | `df.dropna()` | When missing data is minimal and rows are expendable |
| **Fill Values** | `df.fillna(value)` | When you can provide reasonable defaults or averages |
| **Selective Fill** | `df.fillna({col: val})` | When different columns need different fill strategies |
| **Check Nulls** | `df.isnull()` | To identify which cells contain missing values |
| **Count Nulls** | `df.isnull().sum()` | To quantify missing data per column |

### 3. **NumPy Integration**
NumPy's `np.nan` is used to represent missing numeric data, allowing pandas to differentiate between zero values and truly missing data.

---

## 📂 Practice Files

### Data Generation
- **[fake_dictionary.ipynb](fake_dictionary.ipynb)** - Create synthetic employee dataset with intentional missing values using np.nan

### Data Cleaning Operations
- **[dataset_cleaner.ipynb](dataset_cleaner.ipynb)** - Handle missing values with selective filling and row dropping strategies

### Datasets
- **[employees.csv](employees.csv)** - Sample employee data with missing salary, department, and age values

### Practice Exercises (Subfolder)
- **[practice_of_day6/](practice_of_day6/)** - Previous day's exercises on DataFrame filtering and calculations

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| **Missing Data Detection** | Data quality validation in ETL pipelines - identify incomplete records before loading |
| **Selective Filling** | Apply business rules - fill missing departments with "Unassigned", prices with 0, etc. |
| **Row Dropping** | Remove corrupted or incomplete records that can't be salvaged |
| **Null Counting** | Generate data quality reports showing completeness metrics by column |
| **Synthetic Data** | Create test datasets with known issues to validate pipeline error handling |

---

## 🔑 Quick Reference

**Detect Missing Values:**
```python
df.isnull()              # Boolean mask of nulls
df.isnull().sum()        # Count nulls per column
```

**Handle Missing Data:**
```python
df.dropna()                           # Remove rows with any null
df.fillna({"col": "default"})         # Fill specific columns
```

**Create Test Data:**
```python
import numpy as np
data = {"col": [1, np.nan, 3]}        # np.nan for missing values
```

---

## 🛠️ Data Cleaning Workflow

| Step | Operation | Purpose |
|------|-----------|---------|
| 1️⃣ **Load** | `pd.read_csv()` | Import dataset to inspect |
| 2️⃣ **Detect** | `df.isnull().sum()` | Identify columns with missing data |
| 3️⃣ **Strategy** | Decide: drop or fill? | Based on business requirements |
| 4️⃣ **Fill** | `df.fillna({...})` | Apply defaults for salvageable columns |
| 5️⃣ **Drop** | `df.dropna()` | Remove remaining incomplete records |
| 6️⃣ **Validate** | Check cleaned dataset | Ensure no nulls remain where required |

---

## 📊 Exercise Patterns

| Notebook | Input | Cleaning Strategy | Output |
|----------|-------|-------------------|--------|
| **fake_dictionary** | Raw dict with np.nan | Generate CSV with missing data | employees.csv |
| **dataset_cleaner** | employees.csv | Fill department → drop remaining nulls | Clean DataFrame |

---
