import pandas as pd
import time

# Start timer
start_time = time.time()

# Load only required columns
df = pd.read_csv(
    "data/sales_data.csv",
    usecols=["Date", "Product", "Quantity", "Price"]
)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Use efficient data types
df["Product"] = df["Product"].astype("category")
df["Quantity"] = pd.to_numeric(df["Quantity"], downcast="integer")
df["Price"] = pd.to_numeric(df["Price"], downcast="float")

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Calculate total revenue by product
product_sales = (
    df.groupby("Product", observed=True)["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Display top 5 products
print("\nTop 5 Products:")
print(product_sales.head(5))

# Calculate total revenue
total_revenue = df["Total_Sales"].sum()

print("\nTotal Revenue:", total_revenue)

# Memory usage
memory_used = df.memory_usage(deep=True).sum() / (1024 ** 2)

print("\nMemory Used:", round(memory_used, 2), "MB")

# End timer
end_time = time.time()

print("Execution Time:", round(end_time - start_time, 4), "seconds")
