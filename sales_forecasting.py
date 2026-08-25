import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load sales data
df = pd.read_csv("data/sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Group sales by date
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

# Create day number for forecasting
daily_sales["Day"] = range(len(daily_sales))

# Prepare data for machine learning
X = daily_sales[["Day"]]
y = daily_sales["Total_Sales"]

# Create forecasting model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict existing sales
daily_sales["Predicted_Sales"] = model.predict(X)

# Predict sales for the next 7 days
future_days = pd.DataFrame({
    "Day": range(len(daily_sales), len(daily_sales) + 7)
})

future_days["Predicted_Sales"] = model.predict(future_days[["Day"]])

print("\nSales Forecast for Next 7 Days:")
print(future_days)

# Find best-selling products
product_sales = df.groupby("Product")["Total_Sales"].sum()
product_sales = product_sales.sort_values(ascending=False)

print("\nProduct Recommendations:")
print(product_sales.head(5))

# Plot actual and predicted sales
plt.figure(figsize=(10, 5))

plt.plot(
    daily_sales["Date"],
    daily_sales["Total_Sales"],
    label="Actual Sales"
)

plt.plot(
    daily_sales["Date"],
    daily_sales["Predicted_Sales"],
    label="Predicted Sales"
)

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Forecasting")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()