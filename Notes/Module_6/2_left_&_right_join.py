"""
PANDAS Left Join & Right Join

Left Join  -> left DataFrame ki saari rows rakhta hai
             right mein match nahi mila -> NaN
Right Join -> right DataFrame ki saari rows rakhta hai
             left mein match nahi mila -> NaN

TRICK:
    Left Join  = sab left  + matching right
    Right Join = sab right + matching left

PRO TIP: Right Join ki jagah DataFrames swap karke Left Join likho
         pd.merge(df1, df2, how="right") == pd.merge(df2, df1, how="left")
         Left Join zyada readable hai, production mein right join kam dikhta hai
"""

import pandas as pd

students = pd.DataFrame({
    "ID":   [101, 102, 103],
    "Name": ["Ashish", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "ID":    [101, 102, 104],
    "Marks": [95, 88, 91]
})


#  LEFT JOIN
# students (left) ki saari rows aayengi
# marks mein 103 nahi hai -> NaN aayega
# marks ka 104 chhoot jayega (left mein nahi tha)

result_left = pd.merge(students, marks, on="ID", how="left")
print(result_left)
# Output:
#     ID    Name  Marks
# 0  101  Ashish   95.0
# 1  102   Rahul   88.0
# 2  103   Priya    NaN  <- match nahi mila, NaN


#  RIGHT JOIN 
# marks (right) ki saari rows aayengi
# students mein 104 nahi hai -> NaN aayega
# students ka 103 chhoot jayega (right mein nahi tha)

result_right = pd.merge(students, marks, on="ID", how="right")
print(result_right)
# Output:
#     ID    Name  Marks
# 0  101  Ashish     95
# 1  102   Rahul     88
# 2  104     NaN     91  <- match nahi mila, NaN


# COMPARISON:
#   Join       Rows guaranteed    NaN kahan
#   inner      sirf common        koi NaN nahi
#   left       left ki saari      right side mein NaN
#   right      right ki saari     left side mein NaN

# QUICK REFERENCE:
# pd.merge(df1, df2, on="col", how="left")   # left join
# pd.merge(df1, df2, on="col", how="right")  # right join
# pd.merge(df2, df1, on="col", how="left")   # right join ka alternative
