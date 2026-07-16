import pandas as pd

students = pd.DataFrame({
    "Name": ["Ashish", "Rahul", "Priya", "Neha"],
    "Age": [21, 20, 22, 19],
    "Marks": [95, 82, 91, 76],
    "Branch": ["CSE", "ECE", "CSE", "ME"]
})

print(students)

# print(students["Name"])
print(students["Marks"])
print(type(students["Marks"]))  # This is series 

print(students[["Marks"]])
print(type(students[["Marks"]])) # This is DataFrame 

# use double bracket for dataframe and you can include multiple columns in this 

print(students[["Marks","Name"]])  # you can swap the column sequence order too


# Yes , you can modify the value using this we will study later 

students["Marks"] = students["Marks"] + 5


print(students)




# View first 5 rows
# df.head()

# # View first n rows
# df.head(n)

# # View last 5 rows
# df.tail()

# # View last n rows
# df.tail(n)

# # Row slicing works like Python lists
# df[1:4]  -> slicing is like df[start:end] but it is row slicing 

# # Negative slicing also works
# df[-2:] -> last two rows 

# df[0] does NOT return the first row
# It searches for a column named 0 and raises KeyError if not found

# For selecting individual rows, use:
# loc -> label-based indexing
# iloc -> position-based indexing