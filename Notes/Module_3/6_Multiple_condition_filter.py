"""
PANDAS MULTIPLE CONDITIONS

Operators:
    &  -> AND  (dono conditions true honi chahiye)
    |  -> OR   (koi ek true ho)
    ~  -> NOT  (mask reverse karo)

IMPORTANT: and / or / not mat use karo -> ye single boolean ke liye hain, Series ke liye nahi
IMPORTANT: har condition ko parentheses mein wrap karo warna TypeError aayega
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, 20, 22, 19, 23],
    "Marks":  [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})


# AND -> dono conditions true honi chahiye
print(students[
    (students["Age"] > 20) &
    (students["Marks"] >= 90)
])
# Output: Ashish, Priya


# OR -> ek bhi true ho
print(students[
    (students["Branch"] == "ME") |
    (students["Marks"] >= 90)
])
# Output: Ashish, Priya, Neha
# Neha -> Marks >= 90? No. Branch == ME? Yes. -> included


# NOT -> mask ko reverse karo
print(students[
    ~(students["Branch"] == "CSE")
])
# Output: Rahul, Neha, Amit


# Teen ya zyada conditions
print(students[
    (students["Age"] > 20) &
    (students["Marks"] > 88) &
    (students["Branch"] == "CSE")
])
# Output: Ashish, Priya


# MISTAKES:
# df[df["Age"] > 20 & df["Marks"] > 80]        -> TypeError (parentheses missing)
# (df["Age"] > 20) and (df["Marks"] > 80)      -> ValueError (and nahi, & use karo)
# (df["Age"] > 20) or  (df["Marks"] > 80)      -> ValueError (or nahi,  | use karo)

# QUICK REFERENCE:
# df[(df["Age"] > 20) & (df["Marks"] >= 90)]   # AND
# df[(df["Branch"] == "CSE") | (df["Age"] > 20)]  # OR
# df[~(df["Branch"] == "CSE")]                  # NOT