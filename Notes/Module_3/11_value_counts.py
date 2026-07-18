"""
PANDAS value_counts()

Har unique value kitni baar aayi -> ye count karta hai.
Returns -> Pandas Series (sorted by frequency, highest first)
NaN by default ignore hota hai.

unique()       -> values kya hain?          -> NumPy array
nunique()      -> kitni distinct values?     -> Integer
value_counts() -> har value kitni baar aayi? -> Series
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, 20, 22, 19, 23],
    "Marks":  [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})


# Basic usage
print(students["Branch"].value_counts())
# Output:
# CSE    2
# ECE    2
# ME     1
# Sorted by frequency (highest first), alphabetical nahi

print(type(students["Branch"].value_counts()))
# Output: <class 'pandas.core.series.Series'>


# NaN include karna ho to dropna=False
import numpy as np
df = pd.DataFrame({"Branch": ["CSE", "ECE", None, "CSE"]})
print(df["Branch"].value_counts())              # NaN ignore
print(df["Branch"].value_counts(dropna=False))  # NaN included -> NaN 1 bhi aayega


# Relative frequency (percentage)
print(students["Branch"].value_counts(normalize=True))
# Output: CSE 0.4, ECE 0.4, ME 0.2

print(students["Branch"].value_counts(normalize=True) * 100)
# Output: CSE 40.0, ECE 40.0, ME 20.0


# MISTAKES:
# value_counts() ka output unique() jaisa nahi hota (values nahi, counts hain)
# value_counts() ka output nunique() jaisa nahi hota (single int nahi, Series hai)
# df.value_counts() -> DataFrame pe chalega but duplicate rows count karega, column-wise use karo


# QUICK REFERENCE:
# df["col"].value_counts()                  # frequency count
# df["col"].value_counts(dropna=False)      # NaN bhi include karo
# df["col"].value_counts(normalize=True)    # proportion (0 to 1)
# df["col"].value_counts(normalize=True) * 100  # percentage