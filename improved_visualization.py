import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("data/sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Group sales by date
daily_sales = df.groupby("Date")["Total_Sales"].sum()

# Create visualization
plt.figure(figsize=(12, 6))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o",
    linewidth=2
)

# Add title and labels
plt.title("Daily Sales Analysis", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)

# Add grid
plt.grid(True, linestyle="--", alpha=0.5)

# Rotate date labels
plt.xticks(rotation=45)

# Improve layout
plt.tight_layout()

# Display chart
plt.show()
