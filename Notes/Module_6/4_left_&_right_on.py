"""
PANDAS left_on & right_on

on="col"           -> tab use karo jab dono DataFrames mein same column name ho
left_on / right_on -> tab use karo jab column names alag ho

After merging with left_on/right_on -> dono columns result mein aate hain
(on= use karne par sirf ek aata hai)
Duplicate column drop() se hatao
"""

import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 102, 103],
    "Name":      ["Ashish", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "ID":    [101, 102, 103],
    "Marks": [95, 88, 91]
})

# on="ID" -> KeyError (students mein "ID" column nahi hai)

# left_on / right_on se solve karo
result = pd.merge(
    students,
    marks,
    left_on="StudentID",
    right_on="ID"
)
print(result)
# Output:
#    StudentID    Name   ID  Marks
# 0        101  Ashish  101     95
# 1        102   Rahul  102     88
# 2        103   Priya  103     91
# Notice: StudentID aur ID dono aaye (same data, alag naam)


# Extra column hatao
result = result.drop(columns="ID")
print(result)
# Output:
#    StudentID    Name  Marks
# 0        101  Ashish     95


# QUICK REFERENCE:
# pd.merge(df1, df2, on="col")                           # same column name
# pd.merge(df1, df2, left_on="col1", right_on="col2")   # alag column names
# result.drop(columns="col2")                            # duplicate hatao

#   Situation                   Use
#   Same column name            on="col"
#   Different column names      left_on + right_on
