"""
PANDAS groupby()

Data ko groups mein baanto based on ek column ki values.
groupby() khud kuch calculate nahi karta -> sirf groups banata hai.
Calculation ke liye aggregation lagani padti hai: mean(), sum(), count(), etc.

groupby() -> GroupBy object return karta hai, DataFrame nahi.
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit", "Riya"],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE", "CSE"],
    "Marks":  [90, 80, 95, 70, 85, 88]
    "Age":[23,13,24,53,33,53]
})

# GroupBy object banao
groups = students.groupby("Branch")
print(groups)   # DataFrameGroupBy object, DataFrame nahi

# Ek specific group dekho
print(groups.get_group("CSE"))
# Output: Ashish, Priya, Riya (sirf CSE wale)

# Aggregations -> tabhi actual result milta hai
# Saare numeric columns ka mean (Name ignore hoga)
print(students.groupby("Branch").mean())
print(students.groupby("Branch")["Marks"].mean())  #it will only selec the marks column 

print(students.groupby("Branch").sum())     # branch-wise total
print(students.groupby("Branch").count())   # branch-wise count
print(students.groupby("Branch").max())     # branch-wise max
print(students.groupby("Branch").min())     # branch-wise min

# FLOW:
# DataFrame -> groupby() -> Groups -> aggregation() -> Result

# QUICK REFERENCE:
# df.groupby("col")                  # GroupBy object banao
# df.groupby("col").get_group("X")   # ek group dekho
# df.groupby("col").mean()           # group-wise mean
# df.groupby("col").sum()            # group-wise sum
# df.groupby("col").count()          # group-wise count
# df.groupby("col").max()            # group-wise max
# df.groupby("col").min()            # group-wise 





## Important 
# One column

students.groupby("Branch")["Marks"].mean()

# Multiple columns

students.groupby("Branch")[["Marks", "Age"]].mean()

# All numeric columns

students.groupby("Branch").mean()

