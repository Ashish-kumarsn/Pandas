"""
PANDAS groupby().agg()

agg() = ek saath multiple aggregations karo
mean()/sum()/max() -> ek ek aggregation alag alag
agg()              -> sab ek saath

MISTAKE: .agg("mean", "sum")    -> wrong (list chahiye)
         .agg(["mean", "sum"])  -> sahi
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit", "Riya"],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE", "CSE"],
    "Marks":  [90, 80, 95, 70, 85, 88],
    "Age":    [21, 20, 22, 19, 23, 21]
})


# Ek column pe multiple aggregations
print(students.groupby("Branch")["Marks"].agg(["mean", "sum", "max", "min", "count"]))
# Output:
#         mean  sum  max  min  count
# Branch
# CSE     91.0  273   95   88      3
# ECE     82.5  165   85   80      2
# ME      70.0   70   70   70      1


# Alag columns pe alag aggregations -> dictionary
print(students.groupby("Branch").agg({
    "Marks": "mean",
    "Age":   "max"
}))


# Multiple functions + multiple columns
print(students.groupby("Branch").agg({
    "Marks": ["mean", "max", "min"],
    "Age":   ["mean", "max"]
}))
# Output mein multi-level columns aate hain -> ye normal hai


# QUICK REFERENCE:
# df.groupby("col")["num"].agg(["mean","sum","max"])      # list of functions
# df.groupby("col").agg({"col1": "mean", "col2": "max"}) # dict -> alag alag
# df.groupby("col").agg({"col1": ["mean","max"], ...})   # multiple per column

#   Use           When
#   mean()        sirf average chahiye
#   agg([...])    multiple aggregations ek saath
#   agg({...})    alag columns ke liye alag functions


# agg() always returns a DataFrame