"""
PANDAS unique() & nunique()

unique()  -> distinct values kya hain?   -> NumPy array
nunique() -> kitni distinct values hain? -> Integer

Sirf Series pe kaam karta hai, DataFrame pe nahi.
Order of first appearance preserve hota hai, sorted nahi hota.
NaN by default ignore hota hai.
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, 20, 22, 19, 23],
    "Marks":  [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})


# unique() -> distinct values return karta hai
print(students["Branch"].unique())
# Output: ['CSE' 'ECE' 'ME']  (CSE, ECE duplicate the -> hate, ME ek baar -> raha)
# Order: first appearance ke hisaab se

print(type(students["Branch"].unique()))
# Output: <class 'numpy.ndarray'>  (list ya Series nahi)


# nunique() -> count of distinct values return karta hai
print(students["Branch"].nunique())
# Output: 3

print(type(students["Branch"].nunique()))
# Output: <class 'int'>


# NaN by default ignore hota hai nunique() mein
# dropna=False se NaN bhi count hoga
import numpy as np
df = pd.DataFrame({"Branch": ["CSE", "ECE", None, "CSE"]})
print(df["Branch"].nunique())             # Output: 2  (NaN ignore)
print(df["Branch"].nunique(dropna=False)) # Output: 3  (NaN included)


# MISTAKES:
# students.unique()   -> AttributeError  (Series pe chalta hai, DataFrame pe nahi)
# students.nunique()  -> ye chalega but har column ka count dega, column-wise use karo


# QUICK COMPARISON:
# Branch column: CSE, ECE, CSE, ME, ECE
#
# unique()       -> ['CSE', 'ECE', 'ME']   "values kya hain?"
# nunique()      -> 3                       "kitni hain?"
# value_counts() -> CSE 2, ECE 2, ME 1     "har value kitni baar aayi?"

