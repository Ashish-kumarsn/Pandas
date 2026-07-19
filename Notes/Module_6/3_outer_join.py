"""
PANDAS Outer Join

Outer Join -> dono DataFrames ki SAARI rows rakhta hai
Match mila -> combine karo
Match nahi mila -> NaN bharo

Think of it as UNION of both DataFrames — kuch nahi hatta

ALL 4 JOINS SUMMARY:
    Inner -> sirf common rows        (intersection)
    Left  -> sab left + matching right
    Right -> sab right + matching left
    Outer -> sab dono se            (union)
"""

import pandas as pd

students = pd.DataFrame({
    "ID":   [101, 102, 103],
    "Name": ["Ashish", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "ID":    [101, 102, 104],
    "Marks": [95, 88, 90]
})

# Outer join
result = pd.merge(students, marks, on="ID", how="outer")
print(result)
# Output:
#     ID    Name  Marks
# 0  101  Ashish   95.0  <- dono mein tha
# 1  102   Rahul   88.0  <- dono mein tha
# 2  103   Priya    NaN  <- sirf students mein tha
# 3  104     NaN   90.0  <- sirf marks mein tha


# COMPARISON (Left=A,B,C  Right=B,C,D):
#   Inner -> B, C          (sirf common)
#   Left  -> A, B, C       (left ke sab)
#   Right -> B, C, D       (right ke sab)
#   Outer -> A, B, C, D    (dono ke sab)





# merge() does not require the key column to be unique.
# Duplicate keys are allowed.
# Pandas creates all possible matching combinations.
# If a key appears m times on the left and n times on the right, the result contains m × n rows for that key.