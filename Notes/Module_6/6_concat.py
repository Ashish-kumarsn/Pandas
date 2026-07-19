"""
PANDAS concat()

merge() -> key se match karke combine karta hai
concat() -> simply stack karta hai, koi matching nahi

concat() ek list leta hai -> 2, 3, 100 DataFrames ek saath combine ho sakte hain
pd.concat([df1, df2, df3])

axis=0 (default) -> vertical (ek neeche ek)
axis=1           -> horizontal (side by side)
"""

import pandas as pd

df1 = pd.DataFrame({"Name": ["Ashish", "Rahul"], "Marks": [90, 85]})
df2 = pd.DataFrame({"Name": ["Priya", "Neha"],  "Marks": [95, 88]})


#  axis=0 (default) -> row-wise, vertical 
result = pd.concat([df1, df2])
print(result)
# Output:
#      Name  Marks
# 0  Ashish     90
# 1   Rahul     85
# 0   Priya     95  <- index repeat ho raha hai
# 1    Neha     88

# ignore_index=True -> fresh sequential index
result = pd.concat([df1, df2], ignore_index=True)
print(result)
# Output:
#      Name  Marks
# 0  Ashish     90
# 1   Rahul     85
# 2   Priya     95
# 3    Neha     88


#  axis=1 -> column-wise, horizontal 
students = pd.DataFrame({"Name":  ["Ashish", "Rahul", "Priya"]})
marks    = pd.DataFrame({"Marks": [90, 85, 95]})

result = pd.concat([students, marks], axis=1)
print(result)
# Output:
#      Name  Marks
# 0  Ashish     90
# 1   Rahul     85
# 2   Priya     95

# axis=1 index se match karta hai, column values se nahi
# Agar rows ki count alag ho -> NaN aata hai missing index pe


# QUICK REFERENCE:
# pd.concat([df1, df2])                      # vertical (default)
# pd.concat([df1, df2], ignore_index=True)   # fresh index
# pd.concat([df1, df2, df3], ignore_index=True) # multiple DataFrames
# pd.concat([df1, df2], axis=1)              # horizontal

#   axis    Direction       Use
#   0       Vertical        rows append karna (monthly reports, batches)
#   1       Horizontal      columns add karna (side by side)