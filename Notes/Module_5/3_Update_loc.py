"""
PANDAS Updating Values using loc

df.loc[row, column] = value  -> specific cell update karo
df.loc[:, column]            -> poori column (:  = all rows)
df.loc[row, ["col1","col2"]] -> multiple columns ek saath

MISTAKE: df.loc[1]["Marks"] = 75  -> ye mat karo (chained indexing)
         df.loc[1, "Marks"] = 75  -> ye sahi hai
"""

import pandas as pd

df = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya"],
    "Age":   [21, 20, 22],
    "Marks": [85, 72, 91]
})


# Ek cell update karo
df.loc[1, "Marks"] = 75          # Rahul ke marks 72 -> 75
df.loc[2, "Age"]   = 23          # Priya ki age 22 -> 23


# Poori column update karo (: = all rows)
df.loc[:, "Marks"] = df["Marks"] + 5    # sabke marks + 5
df.loc[:, "Age"]   = df["Age"] + 1      # sabki age + 1


# Multiple columns ek row mein
df.loc[1, ["Age", "Marks"]] = [21, 75]  # Rahul ki age aur marks dono


# Poora row replace karo
df.loc[1] = ["Rahul", 22, 80]    # columns ke same order mein values deni hain


# QUICK REFERENCE:
# df.loc[1, "Marks"] = 75               # single cell
# df.loc[:, "Marks"] = df["Marks"] + 5  # poori column
# df.loc[1, ["Age", "Marks"]] = [21, 75] # multiple columns
# df.loc[1] = ["Rahul", 22, 80]          # poora row






"""
PANDAS Conditional Updating using loc

df.loc[condition, "col"] = value  -> condition wali rows update karo
Boolean mask decide karta hai kaunsi rows update hongi

MISTAKE: df.loc[df["Marks"] < 40]["Result"] = "Fail"  -> mat karo (chained indexing)
         df.loc[df["Marks"] < 40, "Result"] = "Fail"  -> ye sahi hai
"""

import pandas as pd

df = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha"],
    "Marks":  [85, 32, 91, 25],
    "Branch": ["CSE", "ECE", "CSE", "ME"]
})


# Condition se column update karo
df["Result"] = "Pass"                                    # pehle default set karo
df.loc[df["Marks"] < 40, "Result"] = "Fail"             # sirf fail wale update honge


# Numeric value conditionally update karo
df.loc[df["Marks"] < 40, "Marks"] += 5                  # failed students ko 5 grace marks


# String condition
df.loc[df["Branch"] == "CSE", "Branch"] = "AI"          # CSE -> AI


# Multiple conditions -> parentheses zaruri hain
df["Grade"] = "B"
df.loc[
    (df["Marks"] > 80) & (df["Branch"] == "CSE"),
    "Grade"
] = "A"


# QUICK REFERENCE:
# df.loc[df["col"] < val, "col2"] = new_val              # single condition
# df.loc[df["col"] == "x", "col"] = "y"                 # string condition
# df.loc[df["col"] < val, "col"] += 5                   # arithmetic update
# df.loc[(cond1) & (cond2), "col"] = val                # AND condition
# df.loc[(cond1) | (cond2), "col"] = val                # OR condition
# df.loc[~(cond), "col"] = val                          # NOT condition