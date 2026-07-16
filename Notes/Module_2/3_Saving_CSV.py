
# SAVING DATA (to_csv)
# Purpose

# - Saves a DataFrame as a CSV file.

# --------------------------------------------------

# Syntax

df.to_csv("file.csv")

# --------------------------------------------------

# Without index=False

# Output contains:

# 0
# 1
# 2

# (Default index is saved.)

# --------------------------------------------------

# Recommended

df.to_csv(
    "file.csv",
    index=False
)

# Only actual data is saved.

# --------------------------------------------------

# Save Selected Columns

df[["Name","Marks"]].to_csv(
    "marks.csv",
    index=False
)

# --------------------------------------------------

# Important

# - Creates a CSV file.
# - Overwrites existing file.
# - Does NOT return a DataFrame.
# - Most commonly used with index=False.  