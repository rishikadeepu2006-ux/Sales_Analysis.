import time
import pandas as pd


# =========================================================
# PERFORMANCE TESTING - SALES ANALYSIS PIPELINE
# =========================================================

def performance_test():

    print("Starting Sales Analysis Performance Test...")
    print("-" * 50)

    # Start timer
    start_time = time.perf_counter()

    # -----------------------------------------------------
    # 1. Load sales data
    # -----------------------------------------------------

    df = pd.read_csv("data/sales_data.csv")

    # -----------------------------------------------------
    # 2. Convert Date column
    # -----------------------------------------------------

    df["Date"] = pd.to_datetime(df["Date"])

    # -----------------------------------------------------
    # 3. Calculate Total Sales
    # -----------------------------------------------------

    df["Total_Sales"] = df["Quantity"] * df["Price"]

    # -----------------------------------------------------
    # 4. Calculate total revenue
    # -----------------------------------------------------

    total_revenue = df["Total_Sales"].sum()

    # -----------------------------------------------------
    # 5. Calculate average sale
    # -----------------------------------------------------

    average_sale = df["Total_Sales"].mean()

    # -----------------------------------------------------
    # 6. Product-wise sales
    # -----------------------------------------------------

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
    )

    # -----------------------------------------------------
    # 7. Category-wise sales
    # -----------------------------------------------------

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
    )

    # -----------------------------------------------------
    # 8. Daily sales
    # -----------------------------------------------------

    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
    )

    # Stop timer
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # =====================================================
    # RESULTS
    # =====================================================

    print("Performance Test Completed")
    print("-" * 50)

    print(f"Number of records : {len(df)}")
    print(f"Total revenue     : {total_revenue:.2f}")
    print(f"Average sale      : {average_sale:.2f}")
    print(f"Products analyzed : {len(product_sales)}")
    print(f"Categories        : {len(category_sales)}")
    print(f"Days analyzed     : {len(daily_sales)}")

    print("-" * 50)
    print(f"Execution time    : {execution_time:.6f} seconds")

    if execution_time < 1:
        print("Performance      : EXCELLENT")
    elif execution_time < 3:
        print("Performance      : GOOD")
    else:
        print("Performance      : NEEDS IMPROVEMENT")


# =========================================================
# RUN PERFORMANCE TEST
# =========================================================

if __name__ == "__main__":
    performance_test()