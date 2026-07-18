"""
PANDAS drop() — Deleting Columns

drop() original DataFrame nahi badlta by default -> new DataFrame return karta hai
Permanent change ke liye: df = df.drop(...)  ya  inplace=True

COMMON MISTAKE:
df.drop(columns=["Age"])   -> Age abhi bhi hai! result save nahi kiya
df = df.drop(columns=["Age"])  -> ye sahi hai
"""

import pandas as pd

df = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya"],
    "Age":    [21, 20, 22],
    "Marks":  [85, 72, 91],
    "Branch": ["CSE", "ECE", "IT"]
})


# Ek column hatao
df = df.drop(columns=["Age"])

# Multiple columns hatao
df = df.drop(columns=["Age", "Branch"])

# Column exist nahi karta -> KeyError
# df.drop(columns=["Salary"])  -> KeyError


# inplace=True -> seedha original badlo (reassign ki zarurat nahi)
df.drop(columns=["Age"], inplace=True)


# QUICK REFERENCE:
# df = df.drop(columns=["col"])                    # ek column
# df = df.drop(columns=["col1", "col2"])           # multiple columns
# df = df.drop(columns=["col"], errors="ignore")   # safe drop
# df.drop(columns=["col"], inplace=True)           # inplace