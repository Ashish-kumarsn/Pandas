"""
PANDAS merge() — Basic + Inner Join

merge() -> do DataFrames ko common column ke basis par combine karo
on="col" -> matching key specify karo
how="inner" -> default behavior (sirf common rows rakhta hai)

Inner Join = intersection -> dono mein exist karne wali rows hi aati hain
Agar koi row ek mein hai doosre mein nahi -> woh hatt jaati hai
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

# Basic merge (inner join by default)
result = pd.merge(students, marks, on="ID")
print(result)
# Output:
#     ID    Name  Marks
# 0  101  Ashish     95
# 1  102   Rahul     88
# ID 103 (Priya) gaya  -> marks mein tha hi nahi
# ID 104 gaya          -> students mein tha hi nahi
# Sirf 101, 102 dono mein the -> wo aaye


# Explicitly inner join likhna
result = pd.merge(students, marks, on="ID", how="inner")
# Same result


# NOTE: on= column dono DataFrames mein same naam ka hona chahiye
# Result mein sirf ek copy aata hai us column ka (duplicate nahi hota)

# QUICK REFERENCE:
# pd.merge(df1, df2, on="col")               # inner join (default)
# pd.merge(df1, df2, on="col", how="inner")  # same, explicit
# df1.merge(df2, on="col")                   # alternative syntax

# Inner Join visual:
# df1 IDs: 101, 102, 103
# df2 IDs: 101, 102, 104
# Result:  101, 102         (sirf common wale)

