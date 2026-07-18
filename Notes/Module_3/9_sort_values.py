import pandas as pd 


students = pd.DataFrame({
    "Name": ["Ashish", "Rahul", "Priya", "Neha", "Amit"],
    "Age": [21, 20, 22, 19, 23],
    "Marks": [95, 82, 91, 76, 88],
    "Branch": ["CSE", "ECE", "CSE", "ME", "ECE"]
})

print(students)


# sort_values return the new DataFrame 
sorted = students.sort_values("Marks")

print(sorted)  # by default ascending 

print("printing the old one ")
print(students) # still in the same order


# Sorting in desc

students.sort_values(
    "Marks",
    ascending=False
)


# sorting string column will also work -> alphabetic 

print(students.sort_values("Name"))


#Sorting multiple Columns 

students.sort_values(
    by=["Branch", "Marks"]
)

# First arrange by Branch.

# Inside each Branch, arrange by Marks.

# Name    Marks   Branch

# Priya     91      CSE
# Ashish    95      CSE
# Rahul     82      ECE
# Amit      88      ECE
# Neha      76       ME

# First CSE -> ECE -> ME 
# inside CSE -> 91 then 95 

#Different Order for Different Columns

students.sort_values(
    by=["Branch", "Marks"],
    ascending=[True, False]
)



# By defalut pandas put the missing value in the end if the value on which column is being sorted is isinstance


##IMPORTANT 

# If we want to the change the original dataframe , original dataframe will be lost 

students.sort_values(
    "Marks",
    inplace=True
)

# we can also do that 

students = students.sort_values(
    "Marks"
    
    )


# IMPORTANT:
# sort_values() only changes the order of rows.
# It does NOT change or reset the index.

# Original
# Index  Name    Marks
# 0      Ashish   95
# 1      Rahul    82
# 2      Priya    91
# 3      Neha     76
# 4      Amit     88

# After sorting by Marks
# Index  Name    Marks
# 3      Neha     76
# 1      Rahul    82
# 4      Amit     88
# 2      Priya    91
# 0      Ashish   95

# Notice:
# Rows move, but their original index labels remain the same.

# To reset the index after sorting:
df.sort_values("Marks").reset_index(drop=True)

