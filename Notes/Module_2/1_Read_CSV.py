'''
We are going to cover the read_csv method and the attribute to inspect data

'''

import pandas as pd

df = pd.read_csv("tips.csv")

# print(df)

print(df.shape)  # will give the shape of the data

print(df.columns)  # will give the columns name

print(df["tip"])  # will print the tip series

# now since there are two many rows in the data we will not see every data
# print(df) -> if data is 1 lakh then terminal will be full

##HEAD

print(df.head())  #-> this will return first 5 rows if no parameter is passed and (rows >5)
print(df.head(10))  # This will print first 10 rows
print(df.head(-200))  # This will print every row from start leaving the ast 200 rows


##TAIL

print(df.tail()) # Will print the last 5 rows

print(df.tail(-100)) # removes the first n rows of the DataFrame and returns all the remaining rows


##SAMPLE

print(df.sample())  # print any  random row
print(df.sample(3))  # print 3 random rows





# | Attribute | Method                  |
# | --------- | ----------------------- |
# | `shape`   | `head()`                |
# | `columns` | `tail()`                |
# | `index`   | `sample()`              |
# | `dtypes`  | `info()`                |




# -----------------------------------------

# Workflow

#       df = pd.read_csv(...)

#           ↓

#       df.shape

#           ↓

#       df.head()

#           ↓

#       df.tail()

#           ↓

#       df.sample()

# -----------------------------------------