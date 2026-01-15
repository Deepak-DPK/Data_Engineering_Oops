
# Day 9: Pandas Loading & Debugging
 
**Topic:** DataFrames, File Loading, and Troubleshooting

---

## 🎯 Learning Objectives
- Master the correct syntax for loading CSV and text files with Pandas
- Understand the difference between dictionaries and DataFrames for data manipulation
- Debug common file loading errors (FileNotFoundError, attribute errors)
- Handle non-standard file separators (pipes, tabs, semicolons)
- Apply vectorization techniques for efficient data processing

---

## ❌ Common Mistakes (The "Gotchas")
These are the specific errors we encountered today. Review these to avoid them in the future.

1. The "Librarian vs. Book" Error
The Mistake:

Python
# INCORRECT
df.read_csv("file.txt") 
# Error: DataFrame object has no attribute 'read_csv'
The Logic:

df (The Book): A DataFrame is the result. It holds data. It cannot go out and fetch files.

pd (The Librarian): The Pandas library is the tool that knows how to read files from the computer.

The Fix: Always ask the Librarian (pd) to read the file.

Python
# CORRECT
df = pd.read_csv("file.txt")
2. The "Ghost File" Error (FileNotFoundError)
The Mistake: You try to read a file, but Python shouts: [Errno 2] No such file or directory.

The Cause:

You created the file in Folder A, but your new notebook is saved in Folder B.

Python only looks in the current folder where the notebook lives.

The Fix:

Always ensure your .csv file and .ipynb file are in the same folder.

Use this debug code to see where Python is looking:

Python
import os
print(os.getcwd())  # Shows current folder
print(os.listdir()) # Shows files in that folder

---

## ## 🔑 Key Concepts (The "Wins")

### 1. **Dictionary vs. DataFrame**

| Aspect | Python Dictionary | Pandas DataFrame |
|--------|------------------|------------------|
| Structure | Bag of items | Structured Excel grid |
| Access Speed | Slow (requires loops) | Fast (vectorization) |
| Operations | Manual iteration | Column-wise math operations |
| Use Case | Small, unstructured data | Large datasets with analysis |

**Key Insight:** Pandas DataFrame allows vectorization - performing operations on entire columns at once, making it much faster and cleaner than dictionaries.

### 2. **Handling Weird Files (The sep Argument)**

Not all data files use commas. Some use pipes (`|`), tabs (`\t`), or semicolons (`;`). If you open a file and it looks like a mess (everything in one column), you need to specify the separator.

**Example:**
```python
# If data looks like: id|name|role
df = pd.read_csv("weird_data.txt", sep="|")
```

### 3. **The "Why" (The Big Picture)**

We don't just write code to write code. We are solving a specific problem:

**The Boss's Problem:** "I have 1 million rows of messy data. Who is the best salesman?"

**The Workflow:**

| Step | Action | Pandas Method |
|------|--------|---------------|
| 1. Load | Get data out of the file | `pd.read_csv` |
| 2. Clean | Fix missing values | `dropna`, `fillna` |
| 3. Group | Organize into piles | `groupby` |
| 4. Report | Calculate the answer | `sum`, `mean` |

---

## 📂 Practice Files

### Core Loading & Debugging
- **[File_loader.ipynb](File_loader.ipynb)** - Practicing file loading with different separators and handling FileNotFoundError
- **[weird_data.txt](weird_data.txt)** - Sample file with pipe-separated values for separator practice

### Real-World Applications
- **[store_sales.csv](store_sales.csv)** - Sample retail dataset for analysis practice
- **[store_sales.ipynb](store_sales.ipynb)** - Sales data analysis workflow demonstration
- **[The_Manual_Lookup.ipynb](The_Manual_Lookup.ipynb)** - Manual data lookup techniques and optimization

---

## 💡 Why This Matters for Data Engineering

| Concept | Real-World Application |
|---------|------------------------|
| **File Loading** | Loading raw data from S3, Azure Blob, or local data lakes into processing pipelines |
| **Separator Handling** | Processing vendor files with inconsistent formats (CSV, TSV, pipe-delimited) |
| **DataFrame vs Dict** | Efficient ETL transformations on millions of rows without memory overflow |
| **Vectorization** | Applying transformations to entire columns in data pipelines (faster than row-by-row loops) |
| **Error Debugging** | Troubleshooting production pipeline failures due to missing files or incorrect paths |
| **Grouping & Aggregation** | Generating business reports (sales by region, revenue by product category) |

---

## 📝 Quick Reference

### Essential Pandas Loading Patterns

| Goal | Code |
|------|------|
| Import Pandas | `import pandas as pd` |
| Read standard CSV | `df = pd.read_csv("file.csv")` |
| Read "Pipe" file | `df = pd.read_csv("file.txt", sep="\|")` |
| Read Tab-delimited | `df = pd.read_csv("file.txt", sep="\t")` |
| Check Data Size | `df.shape` (returns Rows, Cols) |
| Check Data Types | `df.info()` |
| Create Manual DF | `pd.DataFrame(dictionary_data)` |
| Debug File Path | `import os; print(os.getcwd())` |
| List Files in Folder | `import os; print(os.listdir())` |

### Common Error Prevention

```python
# ✅ CORRECT: Ask the librarian (pd) to read
df = pd.read_csv("file.csv")

# ❌ WRONG: Ask the book (df) to read
df.read_csv("file.csv")  # AttributeError!
```