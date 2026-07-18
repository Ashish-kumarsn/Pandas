"""
PANDAS groupby() — Multiple Columns

Ek column ke bajaye list pass karo -> multiple columns se group banao
Har unique combination ek alag group banta hai (CSE+M, CSE+F, ECE+M, etc.)
Result mein Multi-Level Index aata hai (2 index levels)
Column order matter karta hai -> groupby(["Branch","Gender"]) vs groupby(["Gender","Branch"])

MISTAKE: groupby("Branch", "Gender")   -> wrong (list nahi hai)
         groupby(["Branch", "Gender"]) -> sahi
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit", "Riya"],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE", "CSE"],
    "Gender": ["M", "M", "F", "F", "M", "F"],
    "Marks":  [90, 80, 95, 70, 85, 88]
})


# Mean -> Branch + Gender wise
print(students.groupby(["Branch", "Gender"])["Marks"].mean())
# Branch  Gender
# CSE     F         91.5
#         M         90.0
# ECE     M         82.5
# ME      F         70.0


# Count
print(students.groupby(["Branch", "Gender"])["Marks"].count())


# Multiple aggregations
print(students.groupby(["Branch", "Gender"])["Marks"].agg(["mean", "max", "min", "count"]))


# agg with dict
print(students.groupby(["Branch", "Gender"]).agg({"Marks": ["mean", "max"]}))


# QUICK REFERENCE:
# df.groupby(["col1", "col2"])["num"].mean()              # mean
# df.groupby(["col1", "col2"])["num"].count()             # count
# df.groupby(["col1", "col2"])["num"].agg([...])          # multiple agg
# df.groupby(["col1", "col2"]).agg({"col": [...]})        # dict style
