"""
PANDAS replace()

Dataset mein galat ya inconsistent values badlo.
replace() vs fillna():
    replace()  -> specific values badlo  (0 -> -1, "Male" -> "M")
    fillna()   -> sirf NaN values badlo  (NaN -> 0)

Original DataFrame nahi badlta (inplace=True ya reassign karo)
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Gender":    ["Male", "Female", "Male", "Female"],
    "Result":    [1, 0, 1, 0],
    "Purchased": ["Yes", "No", "Yes", "No"]
})


# Ek value replace karo
df["Gender"] = df["Gender"].replace("Male", "M")


# Multiple values ek saath -> dictionary
df["Gender"] = df["Gender"].replace({"Male": "M", "Female": "F"})
df["Result"]    = df["Result"].replace({1: "Pass", 0: "Fail"})
df["Purchased"] = df["Purchased"].replace({"Yes": 1, "No": 0})


# Poore DataFrame mein replace karo (har column mein)
df2 = pd.DataFrame({"A": [0, 1, 2], "B": [3, 0, 5]})
print(df2.replace(0, -1))
# har 0 -> -1, chahe kisi bhi column mein ho


# Invalid values ko NaN se replace karo
df["Gender"] = df["Gender"].replace("Unknown", np.nan)


# QUICK REFERENCE:
# df["col"].replace("old", "new")            # ek value
# df["col"].replace({"old1": "new1", ...})   # multiple values
# df.replace(0, -1)                          # poore DataFrame mein
# df.replace({"Yes": 1, "No": 0})            # poore DataFrame mein multiple
# df.replace("Unknown", np.nan)              # invalid -> NaN
# df.replace(0, -1, inplace=True)            # permanent change