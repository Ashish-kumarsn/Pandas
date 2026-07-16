##CUSTOM INDEXING -> CUSTOM LABELS



# PANDAS CUSTOM INDEXES 

# Every DataFrame has an Index.
# Index = Row Labels, NOT row numbers.

# Default index Pandas automatically banata hai: 0, 1, 2, 3 ...
# But hum ise change kar sakte hain.


import pandas as pd

#Setup 
students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":    [21, 20, 22, 19],
    "Marks":  [95, 82, 91, 76],
    "Branch": ["CSE", "ECE", "CSE", "ME"]
})

# Default index: 0, 1, 2, 3
print("Default index:")
print(students)
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 1   Rahul   20     82    ECE
# 2   Priya   22     91    CSE
# 3    Neha   19     76     ME


# 1. CHANGE INDEX TO INTEGERS 
# Sirf labels change hote hain, data nahi

students.index = [101, 102, 103, 104]
print("\nCustom integer index:")
print(students)
# Output:
#       Name  Age  Marks Branch
# 101  Ashish   21     95    CSE
# 102   Rahul   20     82    ECE
# 103   Priya   22     91    CSE
# 104    Neha   19     76     ME

# Internally positions are still 0, 1, 2, 3
# But labels are now 101, 102, 103, 104
# These are TWO different things:
#
#   Position     Label
#      0          101
#      1          102
#      2          103
#      3          104


# 2. loc WITH CUSTOM INDEX 
# loc label dhundhta hai, position nahi

print("\nloc[102] -> label 102 dhundhega:")
print(students.loc[102])
# Output:
# Name      Rahul
# Age          20
# Marks        82
# Branch      ECE

print("\nloc[104]:")
print(students.loc[104])
# Output:
# Name      Neha
# Age          19
# Marks        76
# Branch       ME


# 3. KeyError WHEN LABEL DOESN'T EXIST 
# loc[1] -> label 1 dhundhega
# Label 1 exist nahi karta (labels are 101-104)
# So -> KeyError

# students.loc[1]    # KeyError: label 1 not found


# 4. CHANGE INDEX TO STRINGS 
# Index integers hi nahi, strings bhi ho sakta hai

students.index = ["A", "B", "C", "D"]
print("\nString index:")
print(students)
# Output:
#     Name  Age  Marks Branch
# A  Ashish   21     95    CSE
# B   Rahul   20     82    ECE
# C   Priya   22     91    CSE
# D    Neha   19     76     ME

print("\nloc['B']:")
print(students.loc["B"])
# Output:
# Name      Rahul
# Age          20
# Marks        82
# Branch      ECE

# students.loc[1]    # KeyError: label 1 not found
#                    # kyunki ab labels hain A, B, C, D


#REAL WORLD USE CASE 
# Company mein 10 lakh employees hain.
# HR ko EMP847291 dhundhna hai.
# Row number yaad karna impossible hai.
# Label se directly access karo -> that's what loc is for.


#  HOW TO SET INDEX IN REAL PROJECTS 
# Manually assign karna kam common hai.
# Real code mein ye zyada dikhega:

#   df = df.set_index("StudentID")           # existing column ko index banao
#   df = pd.read_csv("file.csv", index_col="StudentID")  # CSV padhte waqt set karo

# set_index() baad mein cover hoga


# INTERVIEW CHEATSHEET 
#
# Q: Index always numeric hota hai?           -> No, string/date/datetime bhi ho sakta hai
# Q: Index change karne se data change hota?  -> No, sirf labels change hote hain
# Q: Position aur label same hote hain?       -> Not necessarily
# Q: loc[1] pe KeyError kab aata hai?         -> Jab label 1 exist na kare


# ── QUICK REFERENCE ──────────────────────────────────────

# df.index = [101, 102, 103, 104]   # integer index assign karo
# df.index = ["A", "B", "C", "D"]  # string index assign karo

# df.loc[102]       # label 102 wali row
# df.loc["B"]       # label "B" wali row
# df.loc[1]         # KeyError agar label 1 exist nahi karta

# Position  = row ki physical jagah (0, 1, 2, ...)  <- iloc use karta hai
# Label     = index mein jo value hai (101, "EMP102", "A", ...)  <- loc use karta hai