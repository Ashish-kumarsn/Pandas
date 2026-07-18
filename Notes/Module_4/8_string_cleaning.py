"""
PANDAS String Cleaning — .str accessor

Python mein strings pe .upper(), .lower() hota hai.
Pandas mein poori column pe same kaam karne ke liye .str use karo.

df["col"].str.lower()   -> poori column pe lower() apply hoga

"""

import pandas as pd

df = pd.DataFrame({
    "Name":  [" Ashish ", " RAHUL ", " priya "],
    "City":  ["New Delhi", "New York", "New Jersey"],
    "Email": ["Ashish@Gmail.COM", "rahul@yahoo.com", "PRIYA@hotmail.com"]
})


# str.lower() -> lowercase
df["Name"] = df["Name"].str.lower()
# " ashish ", " rahul ", " priya "

# str.upper() -> uppercase
df["Email"] = df["Email"].str.upper()

# str.title() -> har word ka pehla letter capital
df["Name"] = df["Name"].str.title()
# "Ashish Kumar" -> "Ashish Kumar"

# str.strip() -> leading/trailing spaces hatao
df["Name"] = df["Name"].str.strip()
# " Ashish " -> "Ashish"
# IMPORTANT: "Ashish" == " Ashish" -> False (space ki wajah se merge/groupby galat hota)

# str.replace() -> string ka ek part replace karo
df["City"] = df["City"].str.replace("New", "Old")
# "New Delhi" -> "Old Delhi"

# str.contains() -> column mein koi substring hai ya nahi -> Boolean mask
print(df["Email"].str.contains("gmail", case=False))
# True/False Series return karta hai
# Filtering ke liye use karo:
gmail_users = df[df["Email"].str.contains("gmail", case=False)]


# Chaining -> multiple methods ek saath
df["Name"] = df["Name"].str.strip().str.lower()
# pehle spaces hato, phir lowercase karo


# lstrip() / rstrip() bhi exist karte hain (sirf left ya sirf right se)
# but strip() hi zyada use hota hai


# QUICK REFERENCE:
# df["col"].str.lower()                      # lowercase
# df["col"].str.upper()                      # uppercase
# df["col"].str.title()                      # Title Case
# df["col"].str.strip()                      # spaces hatao (dono taraf)
# df["col"].str.replace("old", "new")        # part of string replace
# df["col"].str.contains("text")             # substring check -> Boolean mask
# df["col"].str.contains("text", case=False) # case-insensitive check
# df[df["col"].str.contains("text")]         # filter rows

#   Method              Purpose
#   str.lower()         lowercase
#   str.upper()         uppercase
#   str.title()         har word capital
#   str.strip()         spaces hatao
#   str.replace()       string ka part badlo
#   str.contains()      substring hai ya nahi