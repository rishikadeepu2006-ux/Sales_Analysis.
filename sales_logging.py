import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="sales_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Sales analysis program started")

try:
    # Load sales data
    df = pd.read_csv("data/sales_data.csv")
    logging.info("Sales data loaded successfully")

    # Check if data is empty
    if df.empty:
        logging.warning("Sales data file is empty")
    else:
        logging.info("Sales data contains %d rows", len(df))

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])
    logging.info("Date column converted successfully")

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]
    logging.info("Total sales calculated successfully")

    # Calculate total revenue
    total_revenue = df["Total_Sales"].sum()

    print("Total Revenue:", total_revenue)

    logging.info(
        "Total revenue calculated: %.2f",
        total_revenue
    )

    # Product analysis
    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 5 Products:")
    print(product_sales.head(5))

    logging.info("Product sales analysis completed")

    logging.info("Sales analysis program completed successfully")

except FileNotFoundError:
    logging.error("Sales data file was not found")

except KeyError as error:
    logging.error("Missing required column: %s", error)

except Exception as error:
    logging.exception("Unexpected error occurred: %s", error)
