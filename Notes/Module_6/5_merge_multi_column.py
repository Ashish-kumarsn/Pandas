"""
PANDAS merge() — Multiple Columns

Ek column se match karna kabhi kabhi galat hota hai
jab ek ID multiple rows mein ho (e.g., same student, alag semesters)

Solution: on=["col1", "col2"] -> dono match hone chahiye tabhi row combine hogi
"""

import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 101, 102],
    "Semester":  [1, 2, 1],
    "Name":      ["Ashish", "Ashish", "Rahul"]
})

marks = pd.DataFrame({
    "StudentID": [101, 101, 102],
    "Semester":  [1, 2, 1],
    "Marks":     [85, 92, 88]
})

# WRONG -> sirf StudentID pe merge -> 4 rows aayenge (101 ke dono semesters cross-match hote hain)
wrong = pd.merge(students, marks, on="StudentID")
print("Wrong result rows:", len(wrong))   # 5 rows (3 chahiye the)

# CORRECT -> dono columns pe merge -> (StudentID, Semester) dono match hone chahiye
result = pd.merge(students, marks, on=["StudentID", "Semester"])
print(result)
# Output:
#    StudentID  Semester    Name  Marks
# 0        101         1  Ashish     85
# 1        101         2  Ashish     92
# 2        102         1   Rahul     88


# QUICK REFERENCE:
# pd.merge(df1, df2, on="col")              # single column key
# pd.merge(df1, df2, on=["col1", "col2"])   # multiple column key
# pd.merge(df1, df2, on=["A", "B", "C"])    # jitne chahiye

# WHEN TO USE:
# Ek column se uniquely identify na ho -> multiple columns use karo
# e.g., Product+Year, StudentID+Semester, EmpID+Department