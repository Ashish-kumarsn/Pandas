"""
PANDAS Dates & Time — Part 2

Date Filtering  -> Date ke basis par rows filter karo
Date Arithmetic -> Date me days add/subtract karo
Timedelta       -> Time duration (days, hours, minutes, etc.)

NOTE:
- Date column pehle datetime honi chahiye.
- Date filtering bilkul normal boolean filtering jaisa hota hai.
"""

import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-01-10",
        "2026-02-15",
        "2026-03-20"
    ],
    "Sales": [500, 700, 900]
})

# String -> DateTime
df["Date"] = pd.to_datetime(df["Date"])


# DATE FILTERING

# 1. Dates after a specific date
print(df[df["Date"] > "2026-02-01"])

# 2. Dates between two dates
print(
    df[
        (df["Date"] >= "2026-01-15") &
        (df["Date"] <= "2026-03-01")
    ]
)


# DATE ARITHMETIC

# Add 7 days
print(df["Date"] + pd.Timedelta(days=7))

# Subtract 5 days
print(df["Date"] - pd.Timedelta(days=5))


# TIMEDELTA

# Timedelta = Time Duration

print(pd.Timedelta(days=5))
print(pd.Timedelta(hours=12))
print(pd.Timedelta(minutes=30))

# Add Timedelta to a Date
date = pd.Timestamp("2026-01-10")
print(date + pd.Timedelta(days=10))

# Difference between two dates
d1 = pd.Timestamp("2026-01-20")
d2 = pd.Timestamp("2026-01-10")

print(d1 - d2)      # 10 days


# REAL PROJECT EXAMPLE

# Warranty ends after 30 days
df["Warranty_End"] = df["Date"] + pd.Timedelta(days=30)

print(df)


# QUICK REFERENCE

# Date Filtering
# df[df["Date"] > "2026-02-01"]
# df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Date Arithmetic
# df["Date"] + pd.Timedelta(days=7)
# df["Date"] - pd.Timedelta(days=5)

# Timedelta
# pd.Timedelta(days=5)
# pd.Timedelta(hours=12)
# pd.Timedelta(minutes=30)

# Timestamp
# pd.Timestamp("2026-01-10")

# Difference Between Dates
# date1 - date2      # Returns Timedelta