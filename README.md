# E-Commerce Sales Analysis

## 1. Project Description

This project analyzes e-commerce sales data using Python.

The project calculates total sales and revenue, identifies top-selling products, performs sales forecasting, provides product recommendations, and creates visualizations.

The project also includes error handling, testing, performance optimization, and logging.

---

## 2. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 3. Project Structure

Sales_Analysis/
│
├── data/
│   └── sales_data.csv
│
├── sales_analysis.py
├── sales_forecasting.py
├── performance_optimization.py
├── dashboard_user_testing.py
├── improved_visualization.py
├── sales_logging.py
├── sales_analysis.log
└── README.md

---

## 4. Features

### Sales Analysis

The project calculates:

- Quantity sold
- Product price
- Total sales
- Total revenue

Total sales is calculated using:

Total Sales = Quantity × Price

### Sales Forecasting

Linear Regression is used to predict future sales based on historical sales data.

### Product Recommendation

Products are ranked according to their total sales.

The top-selling products are displayed as recommendations.

### Data Validation

The project checks for:

- Missing values
- Invalid values
- Missing columns
- Empty datasets

### Performance Optimization

The project improves performance by:

- Loading only required columns
- Using efficient data types
- Reducing memory usage
- Measuring execution time

### Visualization

Matplotlib is used to create:

- Daily sales charts
- Product sales charts
- Sales forecasting charts

### Logging

Important program activities are recorded in:

sales_analysis.log

Logging helps identify errors and monitor program execution.

---

## 5. Installation

Create a virtual environment:

python -m venv .venv

Activate the environment:

.venv\Scripts\activate

Install required libraries:
pip install -r requirements.txt


---

## 6. How to Run

Run the sales analysis:

python sales_analysis.py

Run sales forecasting:

python sales_forecasting.py

Run performance optimization:

python performance_optimization.py

Run user testing:

python dashboard_user_testing.py

Run improved visualization:

python improved_visualization.py

Run logging:

python sales_logging.py

Run the Streamlit dashboard:

python -m streamlit run app.py

---

## 7. Expected Results

The project produces:

- Total revenue
- Top-selling products
- Sales forecasts
- Product recommendations
- Sales visualizations
- Performance information
- User testing results
- Log files

---

## 8. Testing

The project includes tests for:

- Data loading
- Required columns
- Missing values
- Invalid sales values
- Revenue calculation
- Product sales calculation

---

## 9. Future Improvements

Future versions of the project can include:

- Interactive dashboard
- Advanced machine learning forecasting
- Real-time sales analysis
- Customer segmentation
- More advanced recommendation systems
- Database integration

---

## 10. Conclusion

The E-Commerce Sales Analysis project provides a complete system for processing, analyzing, visualizing, and forecasting sales data.

The project demonstrates the use of Python, data analysis, machine learning, testing, performance optimization, and logging.
---

## 11. Live Dashboard

The sales analysis project is deployed using Streamlit.

The dashboard provides:

- Total revenue
- Total quantity sold
- Product-wise sales
- Sales trends
- Top-selling products
- Interactive sales analysis

### Live Demo

https://salesanalysis-kbjypmsv3gxw3guwscdgtf.streamlit.app/