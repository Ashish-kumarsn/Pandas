"""
PANDAS Updating Values using iloc

iloc = integer positions use karta hai (row number, column number)
loc  = labels use karta hai (row label, column name)

MISTAKE: df.iloc[1, "Marks"] = 75  -> TypeError (column name nahi, position chahiye)
         df.iloc[1, 2] = 75         -> sahi

iloc conditional update support nahi karta -> loc use karo
df.iloc[df["Marks"] > 80, 2] = 100  -> Error
df.loc[df["Marks"] > 80, "Marks"] = 100  -> sahi
"""

import pandas as pd

df = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya"],
    "Age":   [21, 20, 22],      # position 1
    "Marks": [85, 72, 91]       # position 2
})


# Single cell update
df.iloc[1, 2] = 75      # row 1 (Rahul), col 2 (Marks) -> 75
df.iloc[2, 1] = 23      # row 2 (Priya), col 1 (Age)   -> 23


# Poora row update
df.iloc[1] = ["Rahul", 22, 80]   # values column order mein honi chahiye


# Poori column update (: = all rows)
df.iloc[:, 2] = df.iloc[:, 2] + 5    # Marks + 5


# Multiple columns ek row mein
df.iloc[1, [1, 2]] = [21, 75]    # Rahul ki Age aur Marks


# Slicing (end excluded, Python jaisa)
print(df.iloc[0:2, 1:3])         # rows 0-1, cols 1-2 (Age aur Marks)


# QUICK REFERENCE:
# df.iloc[1, 2] = 75              # single cell
# df.iloc[1] = [...]              # poora row
# df.iloc[:, 2] = ...             # poori column
# df.iloc[1, [1, 2]] = [...]      # multiple columns
# df.iloc[0:2, 1:3]               # slice (end excluded)

# loc vs iloc:
# loc  -> column names, conditional update supported
# iloc -> column positions, conditional update NOT supported
# Real world mein loc zyada use hota hai