"""
PANDAS duplicated()

Duplicate rows detect karta hai -> Boolean Series return karta hai
True  = duplicate row (pehle dekha ja chuka hai)
False = pehli baar aa raha hai ya unique hai

Default: poori row check hoti hai, sirf ek column nahi
duplicated() sirf identify karta hai, remove nahi karta -> drop_duplicates() next
"""

import pandas as pd

students = pd.DataFrame({
    "Name": ["Ashish", "Rahul", "Priya", "Rahul"],
    "Age":  [21, 20, 22, 20]
})

print(students)
# Output:
#      Name  Age
# 0  Ashish   21
# 1   Rahul   20
# 2   Priya   22
# 3   Rahul   20  <- Row 1 ka exact copy


# Basic usage
print(students.duplicated())
# 0    False  (pehli baar)
# 1    False  (pehli baar)
# 2    False  (pehli baar)
# 3     True  (Row 1 ka exact copy)

# IMPORTANT: Pandas poori row check karta hai
# Name="Rahul", Age=20  ->  same exact row -> True
# Name="Rahul", Age=21  ->  alag row       -> False (age alag hai)


# Count duplicates (same trick as isna().sum())
print(students.duplicated().sum())   # Output: 1


# Sirf duplicate rows dikhao
print(students[students.duplicated()])
# Output: Row 3 (Rahul, 20)


# Specific column ke basis par check karo
print(students.duplicated(subset=["Name"]))
# 0    False
# 1    False
# 2    False
# 3     True  (Name "Rahul" pehle aaya tha)

# Useful jab koi column unique hona chahiye (jaise Employee_ID, Order_ID)
df = pd.DataFrame({"ID": [1, 2, 2, 3], "Name": ["A", "B", "C", "D"]})
print(df.duplicated(subset=["ID"]))
# Row 2 True -> ID=2 already tha (Name alag tha but hum sirf ID check kar rahe)


# QUICK REFERENCE:
# df.duplicated()                  # poori row check
# df.duplicated().sum()            # kitne duplicates hain
# df[df.duplicated()]              # sirf duplicate rows dikhao
# df.duplicated(subset=["col"])    # sirf ek column check

