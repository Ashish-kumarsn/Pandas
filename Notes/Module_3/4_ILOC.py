"""
PANDAS iloc 

iloc = Integer Location

loc  -> labels use karta hai
iloc -> positions use karta hai (labels ko ignore karta hai)

Positions hamesha 0 se start hote hain: 0, 1, 2, 3 ...
"""

import pandas as pd

# Setup 
students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":    [21, 20, 22, 19],
    "Marks":  [95, 82, 91, 76],
    "Branch": ["CSE", "ECE", "CSE", "ME"]
})

# Custom index set karo taaki loc vs iloc ka difference clear ho
students.index = [101, 102, 103, 104]

print("DataFrame with custom index:")
print(students)
# Output:
#       Name  Age  Marks Branch
# 101  Ashish   21     95    CSE
# 102   Rahul   20     82    ECE
# 103   Priya   22     91    CSE
# 104    Neha   19     76     ME

# Ye table hamesha yaad rakho:
#   Label    Position    Column Positions
#   101         0        0=Name, 1=Age, 2=Marks, 3=Branch
#   102         1
#   103         2
#   104         3


# 1. SELECT ONE ROW 
# iloc position dhundhta hai, label nahi

print("\n1. Single row -> iloc[position]")
print(students.iloc[1])     # position 1 -> Rahul
# Output:
# Name      Rahul
# Age          20
# Marks        82
# Branch      ECE

# Compare karo loc se:
# students.loc[102]   -> label 102 dhundhta hai -> Rahul
# students.iloc[1]    -> position 1 dhundhta hai -> Rahul
# Same result, alag soch


# 2. IndexError WHEN POSITION DOESN'T EXIST 
# iloc labels nahi jaanta
# students.iloc[104]  -> position 104 dhundhega -> IndexError
#                        (sirf 4 rows hain, 0-3)
# Note: loc mein label na mile to KeyError
#       iloc mein position na mile to IndexError


# 3. SELECT MULTIPLE ROWS 
# List of positions pass karo

print("\n2. Multiple rows -> iloc[[pos1, pos2]]")
print(students.iloc[[0, 2]])    # position 0 aur 2 -> Ashish aur Priya
# Output shows labels 101, 103 in index
# Position se select kiya, lekin output mein labels waise hi rahenge


# 4. SELECT A RANGE OF ROWS
# iloc normal Python slicing follow karta hai
# End position EXCLUDED hota hai (loc se ulta)
#
#   loc[101:103]  -> 101, 102, 103  (end included)
#   iloc[0:3]     -> 0, 1, 2        (end excluded)

print("\n3. Range of rows -> iloc[start:end]  (end EXCLUDED)")
print(students.iloc[0:3])       # positions 0, 1, 2 -> Ashish, Rahul, Priya
# Position 3 (Neha) nahi aayegi


# 5. SINGLE CELL 
# iloc[row_position, column_position]
# Column bhi position se dena hoga, name se nahi

# Column positions:
# 0 = Name
# 1 = Age
# 2 = Marks
# 3 = Branch

print("\n4. Single cell -> iloc[row_pos, col_pos]")
print(students.iloc[1, 2])      # position 1 (Rahul), position 2 (Marks) -> 82
print(students.iloc[2, 3])      # position 2 (Priya), position 3 (Branch) -> CSE

# Yahan column name "Marks" use nahi kar sakte
# students.iloc[1, "Marks"]  -> TypeError
# students.iloc[1, 2]        -> correct


# 6. RANGE OF ROWS + SPECIFIC COLUMNS 

print("\n5. Row range + specific columns -> iloc[start:end, [col_pos1, col_pos2]]")
print(students.iloc[0:3, [0, 2]])   # rows 0-2, Name(0) aur Marks(2)
# Output:
#       Name  Marks
# 101  Ashish     95
# 102   Rahul     82
# 103   Priya     91


# 7. ALL ROWS, SPECIFIC COLUMN(S) 
# ':' matlab sab kuch us axis pe

print("\n6. All rows, one column -> iloc[:, col_pos]")
print(students.iloc[:, 0])          # all rows, Name column (position 0)

print("\nAll rows, multiple columns -> iloc[:, [pos1, pos2]]")
print(students.iloc[:, [0, 2]])     # all rows, Name aur Marks


# 8. SPECIFIC ROWS, ALL COLUMNS 

print("\n7. Specific rows, all columns -> iloc[start:end, :]")
print(students.iloc[1:3, :])        # positions 1 aur 2, all columns



#  loc vs iloc COMPARISON
#
#   Feature           loc              iloc
#   ──────────────────────────────────────────────
#   Kya use karta     Labels           Positions
#   Row access        Index label      Row number (0,1,2...)
#   Column access     Column name      Column number (0,1,2...)
#   Slice end         INCLUDED         EXCLUDED
#   Invalid access    KeyError         IndexError


# INTERVIEW CHEATSHEET 

# Q: iloc label-based hai?                     -> No, position-based hai
# Q: iloc mein column name use ho sakta?       -> No, sirf integer positions
# Q: iloc ka slice end included hota?          -> No, excluded (Python slicing jaisa)
# Q: loc ya iloc, kaunsa better hai?           -> Dono alag problems solve karte hain
#    Label pata hai  -> loc
#    Position chahiye -> iloc


#  QUICK REFERENCE

# df.iloc[1]              # one row -> Series
# df.iloc[[0, 2]]         # multiple rows -> DataFrame
# df.iloc[0:3]            # range, end EXCLUDED -> DataFrame
# df.iloc[1, 2]           # single cell -> scalar value
# df.iloc[0:3, [0, 2]]    # row range + specific cols -> DataFrame
# df.iloc[:, 0]           # all rows, one col -> Series
# df.iloc[:, [0, 2]]      # all rows, multiple cols -> DataFrame
# df.iloc[1:3, :]         # specific rows, all cols -> DataFrame

