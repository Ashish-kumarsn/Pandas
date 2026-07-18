"""
PANDAS isin()

Check karta hai ki column ki value given list mein hai ya nahi.
Returns Boolean Series (mask), same as df["Age"] > 20.

Use karo jab multiple values ke basis par filter karna ho.
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, 20, 22, 19, 23],
    "Marks":  [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})


# Basic usage -> CSE aur ECE students
print(students[students["Branch"].isin(["CSE", "ECE"])])
# Output: Ashish, Rahul, Priya, Amit (Neha hati kyunki ME list mein nahi)


# Numbers ke saath bhi kaam karta hai
print(students[students["Age"].isin([20, 21, 23])])
# Output: Ashish, Rahul, Amit


# Strings ke saath
print(students[students["Name"].isin(["Ashish", "Neha"])])
# Output: Ashish, Neha


# NOT IN -> ~ lagao
print(students[~students["Branch"].isin(["CSE", "ECE"])])
# Output: sirf Neha (ME wali)


# isin() + & -> combine with other conditions
print(students[
    (students["Branch"].isin(["CSE", "ECE"])) &
    (students["Marks"] > 90)
])
# Output: Ashish, Priya


# isin() vs multiple OR -> same result, isin() zyada clean hai
# Without isin():
# df[(df["Branch"] == "CSE") | (df["Branch"] == "ECE") | (df["Branch"] == "IT")]
# With isin():
# df[df["Branch"].isin(["CSE", "ECE", "IT"])]


# SQL equivalent:
# WHERE Branch IN ('CSE', 'ECE')     ->  df[df["Branch"].isin(["CSE", "ECE"])]
# WHERE Branch NOT IN ('CSE', 'ECE') ->  df[~df["Branch"].isin(["CSE", "ECE"])]


# MISTAKES:
# df["Branch"].isin("CSE")                  -> list pass karo, string nahi
# df["Branch"].isin(["CSE"])                -> sahi, ek value bhi list mein daalte hain
# students["Branch"].isin(["CSE", "ECE"])   -> sirf mask, filter nahi
# students[students["Branch"].isin([...])]  -> ye sahi hai

# QUICK REFERENCE:
# df[df["col"].isin([v1, v2])]              # IN
# df[~df["col"].isin([v1, v2])]             # NOT IN
# df[(df["col"].isin([v1, v2])) & (cond)]   # isin + other condition