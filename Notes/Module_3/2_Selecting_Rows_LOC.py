## NOW WE STUDY IN DETAILS ABOUT SELECTING ROWS


# As we saw that there is not any inbuild method to select the rows ,
# what we have to do it to use head, tail or the slicing which is not good .


# Now i am introducing to you a two new methods -> loc and iloc


#  when we do student[1] -> python think we have to find the details of the column whose name is 1 
#  Thus the error




# loc = Label-Based Indexer

# Meaning: Access rows and columns by their LABELS (names),
#          not by their numeric position.

# Syntax:
#     df.loc[row_label]                      # single row
#     df.loc[row_label, column_label]        # row + column

# Think of it like: Matrix[row][column]

import pandas as pd


students = pd.DataFrame({
    "Name":   ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":    [21, 20, 22, 19],
    "Marks":  [95, 82, 91, 76],
    "Branch": ["CSE", "ECE", "CSE", "ME"]
})

print("Original DataFrame:")
print(students)
# Output:
#      Name  Age  Marks Branch
# 0  Ashish   21     95    CSE
# 1   Rahul   20     82    ECE
# 2   Priya   22     91    CSE
# 3    Neha   19     76     ME



#1. SELECT ONE ROW 

print("1. Single row → loc[label]")
print(students.loc[1])          # Rahul's row (label = 1)
print(type(students.loc[1]))    # <class 'pandas.core.series.Series'>



#2. SELECT MULTIPLE ROWS
# Pass a LIST of labels → double brackets
# Returns a DataFrame

print("2. Multiple rows → loc[[label1, label2]]")
print(students.loc[[0, 2]])     # Ashish and Priya
print(type(students.loc[[0, 2]]))   # DataFrame



# 3. SELECT A RANGE OF ROWS 
# IMPORTANT: loc slicing is INCLUSIVE of the end label
# This is different from normal Python slicing!
#
#   Python list[0:2]  →  0, 1        (2 excluded)
#   df.loc[0:2]       →  0, 1, 2     (2 INCLUDED)

print("3. Range of rows → loc[start:end]  (end is INCLUSIVE)")
print(students.loc[0:2])        # rows 0, 1, 2 — all three



#4. SINGLE CELL 
# loc[row_label, column_label] → one exact value
# Row first, column second — just like matrix notation

print("4. Single cell → loc[row, 'column']")
print(students.loc[1, "Marks"])     # Rahul's Marks → 82
print(students.loc[2, "Branch"])    # Priya's Branch → CSE



#5. ONE ROW, MULTIPLE COLUMNS 
# Pass a list of column names
# Returns Series (still one row)

print("5. One row, multiple columns → loc[row, ['col1', 'col2']]")
print(students.loc[1, ["Age", "Marks"]])    # Rahul's Age and Marks


#6. RANGE OF ROWS + SPECIFIC COLUMNS 
# Most commonly used loc pattern in real projects

print("6. Row range + specific columns → loc[start:end, ['col1', 'col2']]")
print(students.loc[0:2, ["Name", "Marks"]])     # rows 0-2, Name & Marks only


# 7. ALL ROWS, SPECIFIC COLUMN(S)
# ':' means "everything" on that axis
# df.loc[:, "col"]  →  all rows, one column

print("7. All rows, one column → loc[:, 'column']")
print(students.loc[:, "Name"])                      # All names

print("\nAll rows, multiple columns → loc[:, ['col1', 'col2']]")
print(students.loc[:, ["Name", "Marks"]])           # Name and Marks for everyone

print("\n" + "="*50 + "\n")


#8. SPECIFIC ROWS, ALL COLUMNS 
# ':' on the column side = all columns

print("8. Specific rows, all columns → loc[start:end, :]")
print(students.loc[1:2, :])     # Rahul and Priya, all columns


# COMMON MISTAKES 

# Mistake 1: Treating loc like Python slicing
# students.loc[0:2]  does NOT skip index 2 — it includes it

# Mistake 2: Forgetting quotes around column names
# students.loc[1, Marks]     → NameError
# students.loc[1, "Marks"]   → correct ✔

# Mistake 3: Using () instead of []
# students.loc(1)    → wrong
# students.loc[1]    → correct ✔


# INTERVIEW CHEATSHEET 
#
# Q: Is loc label-based or position-based?   → Label-based
# Q: Does loc include the end label in slicing? → YES (inclusive)
# Q: What does ':' mean in loc?              → Select everything on that axis
# Q: Single row → Series or DataFrame?       → Series
# Q: Multiple rows → Series or DataFrame?    → DataFrame


# QUICK REFERENCE 

# df.loc[1]                        # one row → Series
# df.loc[[0, 2]]                   # multiple rows → DataFrame
# df.loc[0:2]                      # range, end INCLUDED → DataFrame
# df.loc[1, "Marks"]               # single cell → scalar value
# df.loc[1, ["Age", "Marks"]]      # one row, multiple cols → Series
# df.loc[0:2, ["Name", "Marks"]]   # range + specific cols → DataFrame
# df.loc[:, "Name"]                # all rows, one col → Series
# df.loc[:, ["Name", "Marks"]]     # all rows, multiple cols → DataFrame
# df.loc[1:2, :]                   # specific rows, all cols → DataFrame
