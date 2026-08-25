import pandas as pd


# =========================================================
# LOAD SALES DATA
# =========================================================

def load_sales_data(file_path):
    """Load sales data from a CSV file."""
    df = pd.read_csv(file_path)

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    return df


# =========================================================
# SALES CALCULATIONS
# =========================================================

def calculate_total_sales(df):
    """Calculate total revenue."""
    return float(df["Total_Sales"].sum())


def calculate_average_sales(df):
    """Calculate average sale."""
    return float(df["Total_Sales"].mean())


def calculate_highest_sale(df):
    """Find the highest sale."""
    return float(df["Total_Sales"].max())


def calculate_lowest_sale(df):
    """Find the lowest sale."""
    return float(df["Total_Sales"].min())


def calculate_total_quantity(df):
    """Calculate total quantity sold."""
    return int(df["Quantity"].sum())


# =========================================================
# PRODUCT ANALYSIS
# =========================================================

def get_product_sales(df):
    """Calculate sales for each product."""
    return (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def get_best_product(df):
    """Find the best-selling product."""
    product_sales = get_product_sales(df)

    return {
        "product": str(product_sales.idxmax()),
        "sales": float(product_sales.max())
    }


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

def get_category_sales(df):
    """Calculate sales for each category."""
    return (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


# =========================================================
# DAILY ANALYSIS
# =========================================================

def get_daily_sales(df):
    """Calculate total sales for each day."""
    return (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )


def get_best_sales_day(df):
    """Find the day with the highest sales."""
    daily_sales = get_daily_sales(df)

    best_day = daily_sales.idxmax()

    return {
        "date": best_day.strftime("%Y-%m-%d"),
        "sales": float(daily_sales.max())
    }


# =========================================================
# GENERATE SALES SUMMARY
# =========================================================

def generate_summary(df):
    """Generate a complete sales summary."""

    best_product = get_best_product(df)
    best_day = get_best_sales_day(df)

    return {
        "total_revenue": calculate_total_sales(df),
        "average_sale": calculate_average_sales(df),
        "highest_sale": calculate_highest_sale(df),
        "lowest_sale": calculate_lowest_sale(df),
        "total_quantity_sold": calculate_total_quantity(df),

        "best_selling_product": best_product["product"],
        "best_product_sales": best_product["sales"],

        "best_sales_day": best_day["date"],
        "best_day_sales": best_day["sales"]
    }


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    file_path = "data/sales_data.csv"

    sales_data = load_sales_data(file_path)

    summary = generate_summary(sales_data)

    print("\n===== SALES ANALYSIS SUMMARY =====")

    for key, value in summary.items():
        print(f"{key}: {value}")