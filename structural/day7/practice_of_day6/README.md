# Day 6: Practice Exercises - Pandas Data Analysis & Filtering

## 🎯 Learning Objectives
- Master DataFrame creation from dictionaries
- Apply conditional filtering to extract meaningful insights
- Perform column-based calculations and transformations
- Export filtered results to CSV for reporting
- Analyze real-world scenarios using pandas operations

---

## 📚 Core Concepts

### 1. **DataFrame Operations**
Pandas DataFrames allow structured data manipulation with powerful filtering and transformation capabilities. These exercises focus on practical data analysis patterns commonly used in data engineering pipelines.

### 2. **Key Pandas Operations**

| Operation | Purpose | Common Use Case |
|-----------|---------|-----------------|
| `pd.DataFrame()` | Create DataFrame from dictionary | Convert raw data structures to analyzable format |
| `df[condition]` | Boolean filtering | Extract records matching criteria |
| `df["new_col"] = calc` | Create calculated columns | Add derived metrics (profit, change, average) |
| `df.to_csv()` | Export to CSV | Generate reports and save results |
| `df.info()` | View DataFrame structure | Check data types and memory usage |

---

## 📂 Practice Files

### Basic DataFrame Practice
- **[practice.ipynb](practice.ipynb)** - Fundamental DataFrame creation, filtering, and boolean indexing exercises

### Real-World Scenarios
- **[The_Crypto_Watchdog.ipynb](The_Crypto_Watchdog.ipynb)** - Track cryptocurrency price movements and identify losing days
- **[The_Store_Profit_Analysis.ipynb](The_Store_Profit_Analysis.ipynb)** - Calculate per-item and total revenue for retail inventory
- **[The_Student_Reportcard.ipynb](The_Student_Reportcard.ipynb)** - Compute student averages and identify failing students

### Generated Datasets
- **[bad_market_days.csv](bad_market_days.csv)** - Output from crypto analysis showing days with negative price movement
- **[The_Store_Profit_Analysis.csv](The_Store_Profit_Analysis.csv)** - Complete profit analysis with calculated columns
- **[The_Student_Report_Card.csv](The_Student_Report_Card.csv)** - Student performance data with averages
- **[products_list.csv](products_list.csv)** - Product inventory data

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| **Conditional Filtering** | Identify failed transactions, anomalies, or threshold violations in pipeline data |
| **Calculated Columns** | Derive business metrics (revenue, conversion rates, KPIs) from raw data |
| **CSV Export** | Generate reports for stakeholders or feed processed data to downstream systems |
| **Boolean Indexing** | Data quality checks - flag records needing attention or remediation |
| **DataFrame Transformations** | ETL operations - clean, transform, and enrich data before loading to warehouse |

---

## 🔑 Quick Reference

**Boolean Filtering:**
```python
# Extract records matching condition
filtered_df = df[df["column_name"] > threshold]
```

**Calculated Columns:**
```python
# Add derived metric
df["new_column"] = df["col1"] - df["col2"]
```

**Export Results:**
```python
# Save to CSV for reporting
df.to_csv("output.csv", index=False)
```

---

## 📊 Exercise Patterns Summary

| Exercise | Input Data | Calculation | Output |
|----------|-----------|-------------|--------|
| **Crypto Watchdog** | Daily open/close prices | daily_change = close - open | Days with negative change |
| **Store Profit** | Cost, selling price, quantity | profit_per_item, total_revenue | Full profit analysis report |
| **Student Report** | Math, science, english scores | average = sum/3 | Students below 70% average |

---
