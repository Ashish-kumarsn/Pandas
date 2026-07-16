'''
PANDAS BOOLEAN FILTERING 

Boolean Filtering = rows ko condition ke basis par filter karna.



Two steps:
    Step 1: Boolean mask banao  -> df["col"] > value
    Step 2: Mask apply karo     -> df[df["col"] > value]
'''

import pandas as pd

# Setup
students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age":    [21, 20, 22, 19, 23],
    "Marks":  [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})

print("Original DataFrame:")
print(students)
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 1   Rahul   20     82    ECE
# 2   Priya   22     91    CSE
# 3    Neha   19     76     ME
# 4    Amit   23     88    ECE


# 1. BOOLEAN MASK 
# Condition likhne par Pandas har row check karta hai
# aur True/False return karta hai -> ye hai Boolean Mask

print("\n1. Boolean mask -> df['col'] > value")
print(students["Age"] > 20)
# Output:
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# Name: Age, dtype: bool

# Internally kya hota hai:
# Ashish  Age=21  -> 21 > 20 -> True
# Rahul   Age=20  -> 20 > 20 -> False
# Priya   Age=22  -> 22 > 20 -> True
# Neha    Age=19  -> 19 > 20 -> False
# Amit    Age=23  -> 23 > 20 -> True


# 2. APPLY THE MASK 
# Mask ko DataFrame ke andar daalte hain
# True  -> row rakhta hai
# False -> row hata deta hai

print("\n2. Filter rows -> df[df['col'] > value]")
print(students[students["Age"] > 20])
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 2   Priya   22     91    CSE
# 4    Amit   23     88    ECE


# 3. NUMERIC COMPARISONS 

# Greater than
print("\n3a. Marks > 80:")
print(students[students["Marks"] > 80])

# Greater than or equal
print("\n3b. Marks >= 90:")
print(students[students["Marks"] >= 90])
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 2   Priya   22     91    CSE

# Less than
print("\n3c. Age < 21:")
print(students[students["Age"] < 21])

# Less than or equal
print("\n3d. Age <= 20:")
print(students[students["Age"] <= 20])


# 4. STRING COMPARISON 
# String columns pe bhi exactly waise hi kaam karta hai

# Equal
print("\n4a. Branch == 'CSE':")
print(students[students["Branch"] == "CSE"])
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 2   Priya   22     91    CSE

# Not equal
print("\n4b. Branch != 'ECE':")
print(students[students["Branch"] != "ECE"])
# Output: Ashish, Priya, Neha (Rahul aur Amit hatt gaye)

# == is comparison
# =  is assignment  <- ye bhool mat
# students["Branch"] = "CSE"   -> sab rows ki Branch badal dega (assignment)
# students["Branch"] == "CSE"  -> mask return karega (comparison)


# 5. SAVE FILTERED DATA 
# Real projects mein filtered data ko variable mein save karo
# taaki baar baar filter na karna pade

cse_students = students[students["Branch"] == "CSE"]
print("\n5. Saved filter -> cse_students:")
print(cse_students)


# 6. COMBINE BOOLEAN FILTER WITH loc 
# Boolean filter ke baad specific columns bhi select kar sakte ho
# df.loc[condition, [columns]]

print("\n6. Boolean filter + loc -> sirf CSE students ke Name:")
print(students.loc[students["Branch"] == "CSE", ["Name"]])
# Output:
#      Name
# 0  Ashish
# 2   Priya

print("\nCSE students ke Name aur Marks:")
print(students.loc[students["Branch"] == "CSE", ["Name", "Marks"]])





# COMMON MISTAKES 

# Mistake 1: Sirf mask banaya, filter nahi kiya
# students["Age"] > 20          -> sirf mask return hoga, rows nahi
# students[students["Age"] > 20] -> ye sahi hai

# Mistake 2: == ki jagah = use kiya
# students["Age"] = 20           -> assignment, data badal jayega
# students["Age"] == 20          -> comparison, sahi hai

# Mistake 3: String mein quotes nahi diye
# students["Branch"] == CSE      -> NameError (CSE variable nahi hai)
# students["Branch"] == "CSE"    -> sahi hai



#  QUICK REFERENCE

# df["Age"] > 20                                 # mask banao
# df[df["Age"] > 20]                             # filter karo

# Comparison operators:
# >   greater than
# <   less than
# >=  greater than or equal
# <=  less than or equal
# ==  equal
# !=  not equal

# df[df["Branch"] == "CSE"]                      # string filter
# df[df["Branch"] != "ECE"]                      # not equal filter
# df.loc[df["Branch"] == "CSE", ["Name"]]        # filter + specific columns

# cse = df[df["Branch"] == "CSE"]                # filtered data save karo