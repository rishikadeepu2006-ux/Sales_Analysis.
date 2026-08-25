import pandas as pd
import os

# Sales data file
FILE_PATH = "data/sales_data.csv"

print("Starting sales data validation...\n")


# =========================================================
# 1. CHECK IF FILE EXISTS
# =========================================================

if not os.path.exists(FILE_PATH):

    print("ERROR: Sales data file not found.")

else:

    print("Sales data file found.")


    # =========================================================
    # 2. LOAD SALES DATA
    # =========================================================

    try:

        df = pd.read_csv(FILE_PATH)

        print("Sales data loaded successfully.")


        # =========================================================
        # 3. CHECK IF FILE IS EMPTY
        # =========================================================

        if df.empty:

            print("ERROR: Sales data file is empty.")

        else:

            print("Sales data contains records.")


            # =========================================================
            # 4. CHECK REQUIRED COLUMNS
            # =========================================================

            required_columns = [
                "Date",
                "Product",
                "Category",
                "Quantity",
                "Price"
            ]

            missing_columns = [
                column
                for column in required_columns
                if column not in df.columns
            ]


            if missing_columns:

                print(
                    "ERROR: Missing required columns:",
                    missing_columns
                )

            else:

                print("All required columns are present.")


                # =========================================================
                # 5. CHECK DATE
                # =========================================================

                df["Date"] = pd.to_datetime(
                    df["Date"],
                    errors="coerce"
                )

                if df["Date"].isnull().any():

                    print(
                        "ERROR: Invalid or missing Date found."
                    )

                else:

                    print("Date data is valid.")


                # =========================================================
                # 6. CHECK QUANTITY
                # =========================================================

                df["Quantity"] = pd.to_numeric(
                    df["Quantity"],
                    errors="coerce"
                )

                if df["Quantity"].isnull().any():

                    print(
                        "ERROR: Invalid or missing Quantity found."
                    )

                elif (df["Quantity"] < 0).any():

                    print(
                        "ERROR: Quantity cannot be negative."
                    )

                else:

                    print("Quantity data is valid.")


                # =========================================================
                # 7. CHECK PRICE
                # =========================================================

                df["Price"] = pd.to_numeric(
                    df["Price"],
                    errors="coerce"
                )

                if df["Price"].isnull().any():

                    print(
                        "ERROR: Invalid or missing Price found."
                    )

                elif (df["Price"] < 0).any():

                    print(
                        "ERROR: Price cannot be negative."
                    )

                else:

                    print("Price data is valid.")


                # =========================================================
                # 8. CALCULATE TOTAL SALES
                # =========================================================

                if (
                    not df["Date"].isnull().any()
                    and not df["Quantity"].isnull().any()
                    and not df["Price"].isnull().any()
                    and not (df["Quantity"] < 0).any()
                    and not (df["Price"] < 0).any()
                ):

                    df["Total_Sales"] = (
                        df["Quantity"] * df["Price"]
                    )

                    print(
                        "\nSales data validation completed successfully."
                    )

                    print("\nTotal Revenue:")

                    print(df["Total_Sales"].sum())


    except Exception as e:

        print("ERROR: Unable to process sales data.")

        print("Details:", e)