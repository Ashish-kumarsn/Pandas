"""
PANDAS Adding Columns

df["New"] = ...  -> column exist nahi karta to Pandas khud bana deta hai
Values ki length rows ki length se match karni chahiye -> warna ValueError
"""

import pandas as pd

df = pd.DataFrame({
    "Name":    ["Ashish", "Rahul", "Priya"],
    "Math":    [80, 70, 90],
    "Science": [90, 60, 95]
})


# List se column banao
df["Result"] = ["Pass", "Pass", "Pass"]

# Doosre column se copy karo
df["Math_Copy"] = df["Math"]

# Calculation se column banao
df["Double"] = df["Math"] * 2
df["Half"]   = df["Math"] / 2

# Multiple columns use karke
df["Total"] = df["Math"] + df["Science"]

# Condition se column banao -> True/False
df["Passed"] = df["Math"] >= 40

print(df)


# MISTAKE:
# df["Grade"] = ["A", "B"]  -> ValueError agar rows 3 hain aur values 2 hain


# QUICK REFERENCE:
# df["col"] = ["a", "b", "c"]         # list se
# df["col"] = df["other_col"]          # doosre column se
# df["col"] = df["marks"] * 2          # calculation se
# df["col"] = df["a"] + df["b"]        # multiple columns se
# df["col"] = df["marks"] >= 40        # condition se (True/False)