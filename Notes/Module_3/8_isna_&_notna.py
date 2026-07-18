"""
PANDAS isna() & notna()

Real datasets mein missing values hoti hain -> NaN ya None
Inhe detect karne ke liye:
    isna()  -> missing hai?     -> True/False mask
    notna() -> missing nahi hai? -> True/False mask

IMPORTANT: df["Age"] == np.nan kabhi mat karo
           NaN kisi se bhi equal nahi hota, khud se bhi nahi
           np.nan == np.nan -> False
"""

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, np.nan, 22, 19, 23],
    "Marks":  [95, 82, np.nan, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", np.nan, "ECE"]
})

print(students)
# Output:
#      Name   Age  Marks Branch
# 0  Ashish  21.0   95.0    CSE
# 1   Rahul   NaN   82.0    ECE
# 2   Priya  22.0    NaN    CSE
# 3    Neha  19.0   76.0    NaN
# 4    Amit  23.0   88.0    ECE


# isna() -> missing rows filter karo
print(students[students["Age"].isna()])     # Rahul (Age missing)
print(students[students["Marks"].isna()])   # Priya (Marks missing)
print(students[students["Branch"].isna()])  # Neha  (Branch missing)


# notna() -> available rows filter karo
print(students[students["Age"].notna()])    # Rahul hata, baaki sab


# Entire DataFrame check karo
print(students.isna())
# Har cell ke liye True/False


# Missing values count karo -> sabse common line
print(students.isna().sum())
# Output:
# Name      0
# Age       1
# Marks     1
# Branch    1


# Combine with other conditions
print(students[
    (students["Marks"].notna()) &
    (students["Marks"] > 90)
])
# Output: Ashish


# MISTAKES:
# df["Age"] == np.nan   -> hamesha False dega, isna() use karo
# df["Age"] != np.nan   -> hamesha True dega,  notna() use karo
# students["Age"].isna() -> sirf mask, filter nahi
# students[students["Age"].isna()] -> ye sahi hai


# NOTE: isnull() aur notnull() bhi same kaam karte hain (purane code mein milenge)
# df.isna()  == df.isnull()
# df.notna() == df.notnull()
# Modern code mein isna() / notna() prefer karo


# QUICK REFERENCE:
# df[df["col"].isna()]                          # missing rows
# df[df["col"].notna()]                         # non-missing rows
# df.isna()                                     # full DataFrame check
# df.isna().sum()                               # missing count per column
# df[(df["col"].notna()) & (df["col"] > val)]   # notna + condition