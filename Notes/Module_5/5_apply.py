"""
PANDAS apply()

Problem: Har value pe custom logic lagana ho (loops avoid karne ke liye)
Solution: apply() -> function har value pe automatically call karta hai

apply(bonus)   -> function reference do, Pandas khud call karega har value pe
apply(bonus()) -> WRONG, ye function turant call kar deta hai, result pass karta hai

apply() kisi bhi type ke saath kaam karta hai: numbers, strings, booleans, etc.
"""

import pandas as pd

df = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya"],
    "Marks": [85, 72, 91]
})


# CUSTOM FUNCTION 
def bonus(mark):
    if mark >= 80:
        return mark + 10
    return mark + 5

df["Marks"] = df["Marks"].apply(bonus)
# Pandas internally karta hai:
# bonus(85) -> 95
# bonus(72) -> 77
# bonus(91) -> 101


#  GRADING EXAMPLE
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(grade)   # naya column bana diya existing column se
print(df)
# Output:
#      Name  Marks Grade
# 0  Ashish     95     A
# 1   Rahul     77     B
# 2   Priya    101     A


# STRING FUNCTION
def make_upper(name):
    return name.upper()

df["Name"] = df["Name"].apply(make_upper)


# BUILT-IN FUNCTIONS BHI CHAL JAATE HAIN
df["Name_Length"] = df["Name"].apply(len)        # len() har naam pe
df["Name_Upper"]  = df["Name"].apply(str.upper)  # str.upper har naam pe


# COMMON MISTAKE:
# df["Marks"].apply(bonus())  -> WRONG (bonus() turant call hoga, result pass hoga)
# df["Marks"].apply(bonus)    -> SAHI  (function reference pass karo, Pandas call karega)


# QUICK REFERENCE:
# df["col"].apply(my_func)          # custom function
# df["col"].apply(len)              # built-in function
# df["col"].apply(str.upper)        # built-in method
# df["new_col"] = df["col"].apply() # naya column banana








"""
PANDAS DataFrame.apply() — axis=0 vs axis=1

Series.apply()    -> har VALUE pe function (ek column)
DataFrame.apply() -> har COLUMN ya har ROW pe function

axis=0 (default) -> ek column at a time function ko milta hai
axis=1           -> ek row at a time function ko milta hai

Function ko Series milti hai (ek column ya ek row), single value nahi.

NOTE: Agar simple arithmetic se kaam chal jaaye to apply() mat use karo
      df["Total"] = df["Math"] + df["Science"]   <- ye faster aur cleaner hai
      df.apply(total, axis=1)                     <- sirf tab jab complex logic ho
"""

import pandas as pd

df = pd.DataFrame({
    "Math":    [80, 70, 90],
    "Science": [90, 60, 95],
    "English": [85, 75, 88]
})


#  axis=0 (default) -> har column pe function
def col_total(column):      # column ek Series hai (80, 70, 90)
    return column.sum()

print(df.apply(col_total))         # ya df.apply(col_total, axis=0)
# Output:
# Math       240
# Science    245
# English    248


#  axis=1 -> har row pe function 
def row_total(row):         # row ek Series hai (Math=80, Science=90, English=85)
    return row.sum()

df["Total"] = df.apply(row_total, axis=1)
# Row 0: 80+90+85 = 255
# Row 1: 70+60+75 = 205
# Row 2: 90+95+88 = 273


# Specific columns access karo row ke andar
def percentage(row):
    return (row["Math"] + row["Science"] + row["English"]) / 3

df["Avg"] = df.apply(percentage, axis=1)


# COMMON MISTAKE:
# df.apply(row_total)        -> axis=0 default hai, function ko column milega
# df.apply(row_total, axis=1) -> ye sahi, row milegi


# QUICK REFERENCE:
# df["col"].apply(func)          # Series.apply -> har value pe
# df.apply(func)                 # DataFrame.apply -> har column pe (axis=0)
# df.apply(func, axis=0)         # same as above
# df.apply(func, axis=1)         # har row pe
# df["new"] = df.apply(f, axis=1) # result naye column mein store karo

#   axis    Function ko kya milta hai
#   0       ek column (Series)     -> default
#   1       ek row    (Series)








# Normal function
def bonus(x):
    return x + 5

df["Marks"] = df["Marks"].apply(bonus)

# Same using lambda
df["Marks"] = df["Marks"].apply(lambda x: x + 5)  # it help you writing one line functions 

# String example
df["Name"] = df["Name"].apply(lambda x: x.upper())

# Conditional
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 80 else "Fail"
)

