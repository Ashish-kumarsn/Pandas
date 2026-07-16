
import pandas as pd 

df = pd.read_csv("tips.csv")

##INFO  
df.info() # no need to wrap inside print 
##this shows the metadata information about the DataFrame 


#output 
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   total_bill  244 non-null    float64
#  1   tip         244 non-null    float64
#  2   sex         244 non-null    object 
#  3   smoker      244 non-null    object 
#  4   day         244 non-null    object 
#  5   time        244 non-null    object 
#  6   size        244 non-null    int64  
# dtypes: float64(2), int64(1), object(4)
# memory usage: 13.5+ KB



# DATAFRAME INFO()

# Syntax

# df.info()

# -----------------------------------------

# info() displays:

# - Number of rows
# - Number of columns
# - Column names
# - Non-Null Count
# - Data types
# - Memory usage

# -----------------------------------------

# Non-Null Count

# 3 non-null
# → No missing values

# 2 non-null
# → One value is missing

# -----------------------------------------

# Common Data Types

# object   → Text/String

# int64    → Integer

# float64  → Decimal

# bool     → True/False

# -----------------------------------------

# Difference

# head()
# → Shows data

# info()
# → Shows information about the data

# -----------------------------------------

# Most Common Workflow

# df = pd.read_csv(...)

# ↓

# df.shape

# ↓

# df.head()

# ↓

# df.info()



print(df.describe())


# # It prints 
# Count -> number of Non-Null value in that column 
# mean -> avg i.e sum of all values / number of values
# std -> standard deviation -> spread of data across the mean -> low std means less spread
# min -> minimum value of that column 
# 25% -> First quartile after sort ka value 
# 50% -> second quartile i.e median ka value 
# 75% -> third quartile ka value 
# max -> value of the max after sorting 100% 



# describe()   → tell about the Numeric columns only by default 



