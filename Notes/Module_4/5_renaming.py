"""
PANDAS rename()

Column names ya row labels (index) badlo, data nahi badlta.
Original DataFrame nahi badlta (inplace=True ya reassign karo)
Non-existent column/index rename karne par Pandas silently ignore karta hai.
"""

import pandas as pd

students = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya"],
    "Age":   [21, 20, 22],
    "Marks": [95, 88, 91]
})

print(students)
# Output:
#      Name  Age  Marks
# 0  Ashish   21     95
# 1   Rahul   20     88
# 2   Priya   22     91


# COLUMNS RENAME 
# columns = {"Old Name": "New Name"}

# Ek column rename karo
print(students.rename(columns={"Marks": "Score"}))
# Marks -> Score, baaki same

# Multiple columns ek saath
print(students.rename(columns={
    "Name": "Student_Name",
    "Marks": "Score"
}))


# INDEX RENAME 
# index = {old_label: new_label}

# Ek index rename karo
print(students.rename(index={0: "A"}))
# 0 -> A, 1 aur 2 same rahe

# Multiple indexes ek saath
print(students.rename(index={0: "A", 1: "B", 2: "C"}))
# Output:
#      Name  Age  Marks
# A  Ashish   21     95
# B   Rahul   20     88
# C   Priya   22     91


# DONO EK SAATH 
print(students.rename(
    columns={"Marks": "Score"},
    index={0: "A", 1: "B", 2: "C"}
))


# PERMANENT CHANGE 
students = students.rename(columns={"Marks": "Score"})   # reassign
# ya
# students.rename(columns={"Marks": "Score"}, inplace=True)


#ALTERNATIVE: SAARE COLUMNS EK SAATH BADLO
# rename() -> sirf selected columns badlo
# df.columns -> saare columns ek saath replace karo (common after read_csv)

students.columns = ["Student_Name", "Student_Age", "Score"]
# Useful jab CSV mein column names messy hon


# QUICK REFERENCE:
# df.rename(columns={"Old": "New"})               # ek column
# df.rename(columns={"A": "B", "C": "D"})         # multiple columns
# df.rename(index={0: "A", 1: "B"})               # row labels
# df.rename(columns={...}, index={...})            # dono saath
# df.rename(columns={...}, inplace=True)           # permanent
# df.columns = ["col1", "col2", "col3"]            # saare columns replace
