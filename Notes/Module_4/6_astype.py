"""
PANDAS astype() — Changing Data Types

CSV/Excel se aane wala data aksar galat dtype mein hota hai.
Jaise Age "21" (string) hota hai, 21 (int) nahi.
String pe mean(), sum() kaam nahi karte properly.

object dtype = usually string hota hai Pandas mein
float -> int = truncate hota hai, round nahi (95.9 -> 95)
"""

import pandas as pd

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya"],
    "Age":    ["21", "20", "22"],    # strings hain
    "Marks":  ["95", "88", "91"],   # strings hain
    "Passed": [1, 0, 1]
})

print(students.dtypes)
# Name      object
# Age       object  <- problem
# Marks     object  <- problem
# Passed     int64


#  EK COLUMN 
students["Age"]    = students["Age"].astype(int)
students["Marks"]  = students["Marks"].astype(float)
students["Passed"] = students["Passed"].astype(bool)


# MULTIPLE COLUMNS EK SAATH (better way)
students = students.astype({
    "Age":    int,
    "Marks":  float,
    "Passed": bool
})



# import pandas as pd

# df = pd.DataFrame({
#     "Age": ["21", "20", "Twenty Two", "19"]
# })

# # This will fail
# df["Age"] = df["Age"].astype(int)

print(students.dtypes)
# Age      int64
# Marks    float64
# Passed   bool


# QUICK REFERENCE:
# df.dtypes                                          # current dtypes check karo
# df["col"].astype(int)                              # string -> int
# df["col"].astype(float)                            # int -> float
# df["col"].astype(str)                              # kuch bhi -> string
# df["col"].astype(bool)                             # 0/1 -> False/True
# df.astype({"col1": int, "col2": float})            # multiple columns

