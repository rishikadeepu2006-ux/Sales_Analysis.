import unittest
import pandas as pd
import os


# =========================================================
# LOAD SALES DATA
# =========================================================

DATA_FILE = "data/sales_data.csv"

df = pd.read_csv(DATA_FILE)


# =========================================================
# SALES DATA VALIDATION TESTS
# =========================================================

class TestSalesDataValidation(unittest.TestCase):

    def test_required_columns_exist(self):
        """Check that all required columns are present."""

        required_columns = [
            "Date",
            "Product",
            "Category",
            "Quantity",
            "Price"
        ]

        for column in required_columns:
            self.assertIn(column, df.columns)

    def test_data_is_not_empty(self):
        """Check that the sales dataset contains records."""

        self.assertGreater(len(df), 0)

    def test_no_missing_values(self):
        """Check that sales data does not contain missing values."""

        self.assertFalse(df.isnull().values.any())

    def test_quantity_is_positive(self):
        """Check that quantity values are greater than zero."""

        self.assertTrue((df["Quantity"] > 0).all())

    def test_price_is_positive(self):
        """Check that price values are greater than zero."""

        self.assertTrue((df["Price"] > 0).all())

    def test_date_is_valid(self):
        """Check that all dates can be converted correctly."""

        dates = pd.to_datetime(df["Date"], errors="coerce")

        self.assertFalse(dates.isnull().any())


# =========================================================
# VISUALIZATION TESTS
# =========================================================

class TestSalesVisualization(unittest.TestCase):

    def test_monthly_sales_chart_exists(self):
        """Check that monthly sales visualization exists."""

        self.assertTrue(os.path.exists("monthly_sales.png"))

    def test_product_sales_chart_exists(self):
        """Check that product-wise sales visualization exists."""

        self.assertTrue(os.path.exists("product_wise_sales.png"))

    def test_quantity_chart_exists(self):
        """Check that quantity visualization exists."""

        self.assertTrue(os.path.exists("quantity_by_product.png"))


# =========================================================
# RUN TESTS
# =========================================================

if __name__ == "__main__":
    unittest.main()