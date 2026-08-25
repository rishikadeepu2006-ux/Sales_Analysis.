import pandas as pd


# Load sales data
df = pd.read_csv("data/sales_data.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]


print("===================================")
print("   SALES DASHBOARD USER TESTING")
print("===================================")


# Test 1: Check whether data is loaded
print("\nTest 1: Data Loading")

if len(df) > 0:
    print("PASS - Sales data loaded successfully")
else:
    print("FAIL - No sales data found")


# Test 2: Check required columns
print("\nTest 2: Required Columns")

required_columns = [
    "Date",
    "Product",
    "Quantity",
    "Price",
    "Total_Sales"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if len(missing_columns) == 0:
    print("PASS - All required columns are available")
else:
    print("FAIL - Missing columns:", missing_columns)


# Test 3: Total revenue
print("\nTest 3: Total Revenue")

total_revenue = df["Total_Sales"].sum()

if total_revenue >= 0:
    print("PASS - Total revenue calculated successfully")
    print("Total Revenue:", total_revenue)
else:
    print("FAIL - Revenue calculation error")


# Test 4: Product sales
print("\nTest 4: Product Sales")

product_sales = df.groupby("Product")["Total_Sales"].sum()

if len(product_sales) > 0:
    print("PASS - Product sales calculated successfully")
    print(product_sales.head())
else:
    print("FAIL - Product sales not available")


# Test 5: Check missing values
print("\nTest 5: Missing Values")

missing_values = df.isnull().sum().sum()

if missing_values == 0:
    print("PASS - No missing values found")
else:
    print("WARNING - Missing values found:", missing_values)


# Test 6: Check negative values
print("\nTest 6: Invalid Sales Values")

if (df["Quantity"] < 0).any() or (df["Price"] < 0).any():
    print("FAIL - Negative quantity or price found")
else:
    print("PASS - Sales values are valid")


# Final result
print("\n===================================")
print("USER TESTING COMPLETED")
print("===================================")