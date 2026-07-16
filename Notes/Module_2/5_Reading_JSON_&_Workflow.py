##JSON DATA READING 
import pandas as pd 

# AI projects me JSON bahut common hai.

# Especially jab data aata hai:

# APIs
# Web applications
# REST services
# Cloud applications


df = pd.read_json("student.json")

print(df)


# JSON

# - Stores data as key-value pairs.
# - Similar to Python dictionaries.




# =================================================
# PANDAS DATA INSPECTION WORKFLOW
# =================================================

# Step 1

# df = pd.read_csv("file.csv")

# -----------------------------------------

# Step 2

# df.head()

# See first few rows.

# -----------------------------------------

# Step 3

# df.shape

# Rows and columns.

# -----------------------------------------

# Step 4

# df.info()

# - Missing values
# - Data types
# - Memory usage

# -----------------------------------------

# Step 5

# df.describe()

# Statistical summary.

# -----------------------------------------

# Step 6

# df.tail()

# Inspect last rows.

# -----------------------------------------

# Step 7

# df.sample(5)

# Random inspection.

# -----------------------------------------

# Golden Workflow

# Read

# ↓

# Inspect

# ↓

# Understand

# ↓

# Clean

# ↓

# Analyze

# ↓

# Build ML Model