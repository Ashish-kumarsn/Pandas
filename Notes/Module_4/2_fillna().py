"""
PANDAS fillna() 

NaN values ko delete karne ki jagah fill karo.
dropna() se zyada use hota hai kyunki data delete karna expensive hai.

fillna() original DataFrame nahi badlata.
Permanent change: df = df.fillna(0)  ya  df.fillna(0, inplace=True)

FILLING STRATEGIES:
    1. Constant     -> fixed value (0, -1, "Unknown")
    2. Mean         -> numerical data, no outliers
    3. Median       -> numerical data, outliers hain
    4. Mode         -> categorical data
"""

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":    [21, np.nan, 22, 19],
    "Marks":  [95, 88, np.nan, 76],
    "City":   ["Delhi", np.nan, "Mumbai", "Delhi"]
})

print(students)
# Output:
#      Name   Age  Marks    City
# 0  Ashish  21.0   95.0   Delhi
# 1   Rahul   NaN   88.0     NaN
# 2   Priya  22.0    NaN  Mumbai
# 3    Neha  19.0   76.0   Delhi


# 1. CONSTANT 
students.fillna(0)          # har NaN -> 0
students.fillna(-1)         # har NaN -> -1  (0 actual value ho sakta hai, -1 clearly missing)
students.fillna("Unknown")  # string columns ke liye

# Alag columns ke liye alag values -> dictionary
students.fillna({"Age": 18, "Marks": 0, "City": "Unknown"})


# 2. MEAN 
# Average se fill karo
# Use karo: numerical data, koi bada outlier nahi

mean_age = students["Age"].mean()       # 20.67
students["Age"] = students["Age"].fillna(mean_age)

# Problem with mean:
# Ages: [20, 20, 21, 22, 100] -> mean = 36.6 (100 ne average upar khich liya)
# Aisa data ho to median better hai


# 3. MEDIAN 
# Middle value se fill karo
# Use karo: numerical data with outliers (salary, house price, income)

median_marks = students["Marks"].median()   # sorted middle value
students["Marks"] = students["Marks"].fillna(median_marks)

# Ages: [20, 20, 21, 22, 100] -> median = 21 (outlier ka asar nahi)


# 4. MODE 
# Sabse zyada baar aane wali value se fill karo
# Use karo: categorical data (City, Branch, Department)

mode_city = students["City"].mode()[0]  # [0] kyunki multiple modes ho sakte hain
students["City"] = students["City"].fillna(mode_city)
# City mein "Delhi" 2 baar aaya -> mode = "Delhi"


# WHICH TO USE? 
# Mean   -> Height, Temperature, Exam scores (symmetric data)
# Median -> Salary, House Price, Income      (outliers wala data)
# Mode   -> City, Branch, Gender             (categorical data)


# COMMON PATTERNS 
df = students.copy()

# Numerical column -> mean/median
df["Age"]   = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Categorical column -> mode
df["City"]  = df["City"].fillna(df["City"].mode()[0])

# Multiple columns ek saath -> dictionary
df.fillna({"Age": df["Age"].mean(), "City": "Unknown"})


# QUICK REFERENCE:
# df.fillna(0)                              # sab NaN -> 0
# df.fillna({"Age": 18, "Marks": 0})        # alag columns, alag values
# df["col"].fillna(df["col"].mean())        # mean se fill
# df["col"].fillna(df["col"].median())      # median se fill
# df["col"].fillna(df["col"].mode()[0])     # mode se fill
# df.fillna(0, inplace=True)               # permanent change
