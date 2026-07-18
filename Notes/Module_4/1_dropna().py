
"""
PANDAS dropna()

Missing values wali rows remove karta hai.

Default behavior:
    - Koi bhi row jisme ek bhi NaN ho -> poori row hati hai
    - Sirf NaN cell nahi, poori row
    - Original DataFrame nahi badlata, new DataFrame return karta hai
"""

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":   [21, np.nan, 22, 19],
    "Marks": [95, 88, np.nan, 76]
})

print(students)
# Output:
#      Name   Age  Marks
# 0  Ashish  21.0   95.0
# 1   Rahul   NaN   88.0   <- Age missing
# 2   Priya  22.0    NaN   <- Marks missing
# 3    Neha  19.0   76.0


# Basic usage -> ek bhi NaN wali poori row hati hai
print(students.dropna())
# Output:
#      Name   Age  Marks
# 0  Ashish  21.0   95.0
# 3    Neha  19.0   76.0
# Rahul aur Priya dono gaye


# Original DataFrame nahi badla
print(students)  # abhi bhi 4 rows hain


# Permanent change karne ke 2 tarike:
students = students.dropna()          # Method 1: reassign
# students.dropna(inplace=True)       # Method 2: inplace


# MISTAKES:
# dropna() sirf NaN cell nahi hatata, poori row hatata hai
# dropna() original DataFrame nahi badlata jab tak reassign na karo


# INTERVIEW CHEATSHEET:
# Q: dropna() default mein kya karta hai? -> ek bhi NaN wali row remove karta hai
# Q: Original DataFrame badlata hai?      -> No, new DataFrame return karta hai
# Q: Sirf NaN cell hata deta hai?         -> No, poori row hati hai




## PARAMETERS TO USE WITH DROPNA 
# 1.

"""
PANDAS dropna() — axis parameter

axis=0 -> NaN wali ROWS hatao   (default)
axis=1 -> NaN wali COLUMNS hatao

Yaad rakhne ki trick:
    0 = Down  = Rows
    1 = Across = Columns
"""

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":   [21, np.nan, 22, 19],
    "Marks": [95, 88, np.nan, 76]
})

print(students)
# Output:
#      Name   Age  Marks
# 0  Ashish  21.0   95.0
# 1   Rahul   NaN   88.0  <- Age missing
# 2   Priya  22.0    NaN  <- Marks missing
# 3    Neha  19.0   76.0


# axis=0 (default) -> NaN wali rows hatao
print(students.dropna(axis=0))
# Output: Ashish, Neha  (Rahul aur Priya gaye)


# axis=1 -> NaN wali columns hatao
print(students.dropna(axis=1))
# Output: sirf Name column bachi
# Age   -> NaN tha (Rahul) -> poora column gaya
# Marks -> NaN tha (Priya) -> poora column gaya




# QUICK REFERENCE:
# df.dropna()         = df.dropna(axis=0)  # rows hatao
# df.dropna(axis=1)                         # columns hatao


# 2.

"""
PANDAS dropna() — how parameter

how="any" -> ek bhi NaN ho to row/column hatao  (default)
how="all" -> sirf tab hatao jab SAARI values NaN hon
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":  ["Ashish", np.nan, np.nan, "Neha"],
    "Age":   [21, np.nan, np.nan, 19],
    "Marks": [95, np.nan, 91, np.nan]
})

print(df)
# Output:
#      Name   Age  Marks
# 0  Ashish  21.0   95.0   <- koi NaN nahi
# 1     NaN   NaN    NaN   <- sab NaN
# 2     NaN   NaN   91.0   <- kuch NaN, kuch valid
# 3    Neha  19.0    NaN   <- kuch NaN, kuch valid


# how="any" (default) -> ek bhi NaN mile to hatao
print(df.dropna(how="any"))
# Output: sirf Row 0 (Ashish) bachi
# Row 1, 2, 3 sab gaye kyunki inme se kisi mein ek NaN tha


# how="all" -> sirf tab hatao jab row ki saari values NaN hon
print(df.dropna(how="all"))
# Output: Row 0, 2, 3 bache (sirf Row 1 gaya kyunki wo poora NaN tha)


# axis=1 ke saath bhi kaam karta hai
df2 = pd.DataFrame({"A": [1,2,3], "B": [np.nan,np.nan,np.nan], "C": [7,8,9]})
print(df2.dropna(axis=1, how="all"))   # B column gaya (sab NaN the)
print(df2.dropna(axis=1, how="any"))   # B column gaya (ek bhi NaN tha)


# COMPARISON TABLE:
# dropna()                      = dropna(axis=0, how="any")  -> row mein ek bhi NaN -> hatao
# dropna(axis=0, how="all")                                  -> row mein sab NaN    -> hatao
# dropna(axis=1, how="any")                                  -> col mein ek bhi NaN -> hatao
# dropna(axis=1, how="all")                                  -> col mein sab NaN    -> hatao


# 3.

"""
PANDAS dropna() — thresh parameter

thresh = minimum NON-NaN (valid) values jo honi chahiye row/column mein
Agar valid values thresh se kam hain -> row/column hatao

IMPORTANT: thresh missing values count nahi karta, VALID values count karta hai
IMPORTANT: how aur thresh saath use nahi kar sakte -> TypeError
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, np.nan, np.nan, 4],
    "B": [2, np.nan, 5, np.nan],
    "C": [3, np.nan, np.nan, np.nan]
})

print(df)
# Output:
#      A    B    C
# 0  1.0  2.0  3.0   <- valid = 3
# 1  NaN  NaN  NaN   <- valid = 0
# 2  NaN  5.0  NaN   <- valid = 1
# 3  4.0  NaN  NaN   <- valid = 1


# thresh=1 -> at least 1 valid value chahiye
print(df.dropna(thresh=1))
# Row 1 gaya (valid=0), baaki sab bache


# thresh=2 -> at least 2 valid values chahiye
print(df.dropna(thresh=2))
# Row 0 bachi (valid=3), baaki sab gaye


# thresh=4 -> 4 valid values chahiye but columns sirf 3 hain
print(df.dropna(thresh=4))
# Empty DataFrame


# axis=1 ke saath -> column mein kitni valid values chahiye
df2 = pd.DataFrame({"A": [1,2,3], "B": [np.nan,np.nan,np.nan], "C": [7,8,9]})
print(df2.dropna(axis=1, thresh=2))
# B column gaya (valid=0), A aur C bache


# how vs thresh:
# how="any"  -> ek bhi NaN -> delete  (less flexible)
# how="all"  -> sab NaN    -> delete  (less flexible)
# thresh=2   -> 2 se kam valid values -> delete  (zyada flexible)
#
# Example: row = [10, NaN, 30]
# how="any"  -> DELETE  (ek NaN tha)
# thresh=2   -> KEEP    (2 valid values hain)



# 4.


"""
PANDAS dropna() — subset parameter

subset = sirf in columns ko check karo, baaki ignore karo

Without subset -> har column check hota hai
With subset    -> sirf selected columns decide karte hain

"""

import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name":  ["Ashish", "Rahul", "Priya", "Neha"],
    "Age":   [21, np.nan, 22, 19],
    "Marks": [95, 88, np.nan, 76]
})

print(students)
# Output:
#      Name   Age  Marks
# 0  Ashish  21.0   95.0
# 1   Rahul   NaN   88.0  <- Age missing
# 2   Priya  22.0    NaN  <- Marks missing
# 3    Neha  19.0   76.0


# sirf Marks column check karo
print(students.dropna(subset=["Marks"]))
# Rahul bhi raha (Age missing tha but Marks valid tha, Age check hi nahi hua)
# Priya gayi (Marks missing)


# sirf Age column check karo
print(students.dropna(subset=["Age"]))
# Rahul gaya (Age missing), Priya rahi (Marks missing but Age valid tha)


# dono columns check karo (any ek missing ho to hatao)
print(students.dropna(subset=["Age", "Marks"]))
# Ashish aur Neha bache


# subset + how="all" -> dono missing hon tabhi hatao
print(students.dropna(subset=["Age", "Marks"], how="all"))
# koi nahi gaya (kisi ki bhi dono values ek saath missing nahi)


# subset + thresh -> in columns mein se kitni valid chahiye
print(students.dropna(subset=["Age", "Marks"], thresh=2))
# sirf wo rows jinki Age aur Marks dono valid hain


# COMPLETE dropna() CHEATSHEET
# df.dropna()                                    # rows mein koi bhi NaN -> hatao
# df.dropna(axis=1)                              # columns mein koi bhi NaN -> hatao
# df.dropna(how="any")                           # ek bhi NaN -> hatao (default)
# df.dropna(how="all")                           # sab NaN -> hatao
# df.dropna(thresh=2)                            # 2 se kam valid values -> hatao
# df.dropna(subset=["Marks"])                    # sirf Marks check karo
# df.dropna(subset=["Age", "Marks"])             # sirf ye dono check karo
# df.dropna(subset=["Age", "Marks"], how="all")  # dono missing hon tabhi hatao
# df.dropna(subset=["Age", "Marks"], thresh=2)   # dono valid hon tabhi rakho