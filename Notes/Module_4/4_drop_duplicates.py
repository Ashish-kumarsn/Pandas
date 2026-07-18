"""
PANDAS drop_duplicates() & keep parameter

duplicated()      -> identify karo  (Boolean Series)
drop_duplicates() -> remove karo    (cleaned DataFrame)

Default: poori row compare hoti hai, first occurrence rakhta hai
Original DataFrame nahi badlata (inplace=True ya reassign karo)
"""

import pandas as pd

df = pd.DataFrame({
    "Name": ["Ashish", "Rahul", "Priya", "Rahul", "Neha", "Rahul"],
    "Age":  [21, 20, 22, 20, 19, 20]
})

print(df)
# Output:
#      Name  Age
# 0  Ashish   21
# 1   Rahul   20  <- first Rahul
# 2   Priya   22
# 3   Rahul   20  <- duplicate
# 4    Neha   19
# 5   Rahul   20  <- duplicate


# Basic -> first occurrence rakho, baaki hatao
print(df.drop_duplicates())
# Rows: Ashish, Rahul(1), Priya, Neha


# keep parameter 

# keep="first" (default) -> pehla rakho, baad wale hatao
print(df.drop_duplicates(keep="first"))
# Row 1 ka Rahul bacha, Row 3 aur 5 gaye

# keep="last" -> aakhri rakho, pehle wale hatao
print(df.drop_duplicates(keep="last"))
# Row 5 ka Rahul bacha, Row 1 aur 3 gaye

# keep=False -> saare duplicates hatao, koi nahi bachta
print(df.drop_duplicates(keep=False))
# Rahul ke teeno rows gaye, sirf Ashish, Priya, Neha bache


#  subset parameter 
# Sirf selected columns compare karo

df2 = pd.DataFrame({"ID": [1, 2, 2, 3], "Name": ["Ashish", "Rahul", "Rohit", "Neha"]})
print(df2.drop_duplicates(subset=["ID"]))
# ID=2 duplicate tha -> Rohit gaya (Name alag tha but ID check hua)

# Real use: customers.drop_duplicates(subset=["Email"])


# keep parameter duplicated() ke saath bhi kaam karta hai
print(df.duplicated(keep="first"))   # baad wale Rahul True
print(df.duplicated(keep="last"))    # pehle wale Rahul True
print(df.duplicated(keep=False))     # sare Rahul True


# COMPLETE CHEATSHEET:
# df.duplicated()                      # duplicate rows identify karo
# df.duplicated(subset=["col"])        # specific column se check karo
# df.duplicated().sum()                # kitne duplicates hain
# df[df.duplicated()]                  # sirf duplicate rows dikhao

# df.drop_duplicates()                 # remove karo, first rakho
# df.drop_duplicates(keep="first")     # first rakho (default)
# df.drop_duplicates(keep="last")      # last rakho
# df.drop_duplicates(keep=False)       # sab hatao
# df.drop_duplicates(subset=["col"])   # specific column ke basis par
# df.drop_duplicates(inplace=True)     # permanent change
