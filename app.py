import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 E-Commerce Sales Analysis Dashboard")
st.write("Sales analysis dashboard with revenue, product performance and sales trends.")

# Load sales data
try:
    df = pd.read_csv("sales_data.csv")

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]

except FileNotFoundError:
    st.error("Sales data file not found!")
    st.stop()

# -------------------------------
# Key Sales Information
# -------------------------------

total_revenue = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
total_products = df["Product"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Total Revenue",
    f"₹{total_revenue:,.2f}"
)

col2.metric(
    "📦 Total Quantity",
    total_quantity
)

col3.metric(
    "🛍️ Total Products",
    total_products
)

# -------------------------------
# Sales Trend
# -------------------------------

st.subheader("📈 Sales Trend")

daily_sales = df.groupby("Date")["Total_Sales"].sum()

st.line_chart(daily_sales)

# -------------------------------
# Product Analysis
# -------------------------------

st.subheader("🏆 Top Selling Products")

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_sales.head(10))

# -------------------------------
# Sales Data
# -------------------------------

st.subheader("📋 Sales Data")

st.dataframe(
    df,
    use_container_width=True
)

# -------------------------------
# Download Data
# -------------------------------

csv_file = df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Sales Data",
    data=csv_file,
    file_name="sales_analysis.csv",
    mime="text/csv"
)
