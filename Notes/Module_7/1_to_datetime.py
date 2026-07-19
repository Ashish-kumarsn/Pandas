"""
PANDAS Dates & Time — Part 1

pd.to_datetime() -> string ko actual datetime mein convert karo
.dt accessor     -> datetime column se year, month, day, hour etc. nikalo

CSV mein dates aksar string (object) hoti hain -> pehla kaam hamesha:
df["Date"] = pd.to_datetime(df["Date"])

NOTE: year/month/day -> properties (no parentheses)
      day_name()     -> method (parentheses chahiye)
"""

import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-10 10:30:00",
        "2026-02-15 14:45:00",
        "2026-03-20 09:15:00"
    ]
})

print(df.dtypes)   # Date -> object (abhi string hai)

# String -> DateTime
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)   # Date -> datetime64[ns]


# .dt se extract karo
print(df["Date"].dt.year)       # 2026, 2026, 2026
print(df["Date"].dt.month)      # 1, 2, 3
print(df["Date"].dt.day)        # 10, 15, 20
print(df["Date"].dt.hour)       # 10, 14, 9
print(df["Date"].dt.minute)     # 30, 45, 15
print(df["Date"].dt.day_name()) # Saturday, Sunday, Friday


# Real project pattern -> naye columns banao
df["Year"]    = df["Date"].dt.year
df["Month"]   = df["Date"].dt.month
df["Day"]     = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()
print(df)


# QUICK REFERENCE:
# df["col"] = pd.to_datetime(df["col"])   # convert to datetime
# df["col"].dt.year                        # year
# df["col"].dt.month                       # month number
# df["col"].dt.day                         # day of month
# df["col"].dt.hour                        # hour
# df["col"].dt.minute                      # minute
# df["col"].dt.second                      # second
# df["col"].dt.day_name()                  # Monday, Tuesday...

#   Property          Returns
#   .dt.year          year number
#   .dt.month         month number (1-12)
#   .dt.day           day number
#   .dt.hour          hour (0-23)
#   .dt.day_name()    weekday name
