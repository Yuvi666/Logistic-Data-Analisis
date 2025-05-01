# Logistic-Data-Analysis

## Problem Understanding

The logistics company wants to analyze delivery data to gain insights into delivery performance, cost factors, and efficiency across city pairs. The goal is to explore the dataset, clean it as needed, and extract meaningful patterns to inform operational decisions.

## Approach

1. Data Cleaning:
   - Checked for missing values and confirmed there were none.
   - Verified and converted date columns (pickup_date and delivery_date) to datetime format.
   - Ensured numerical columns such as weight_kg, distance_km, and cost were in the correct format.

2. Feature Engineering:
   - Created a new column delivery_days by calculating the difference between delivery and pickup dates.

3. Analysis:
   - Calculated average delivery time for each origin-destination city pair.
   - Assessed delivery success rate grouped by origin city.
   - Analyzed correlation between weight and cost, and between distance and cost.

4. Modeling:
   - Built a simple linear regression model to predict delivery cost using weight_kg and distance_km as predictors.
   - Evaluated model performance using R² and Mean Squared Error.

## Key Insights

- Most city pairs showed a consistent delivery duration, with a few outliers suggesting potential delays or inefficiencies.
- Some origin cities had notably lower delivery success rates, which could indicate issues with specific routes or hubs.
- There was a strong positive correlation between distance and cost, as expected.
- The regression model showed that both weight and distance significantly contribute to delivery cost, aligning with operational assumptions.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### How to Run the Streamlit App (Optional / Bonus Task)

## Prerequisites

## Environment Setup 

To create a clean Python environment for this project using venv , follow the steps below.

### Using venv (Standard Python)

```bash
# Create a virtual environment
python -m venv env

# Activate the environment
# On Windows:
env\Scripts\activate

Ensure Python is installed and the following libraries are available:

- streamlit
- pandas
- plotly
- seaborn
- matplotlib

Install them using pip if needed:

```bash
pip install streamlit pandas plotly seaborn matplotlib
```

### Running the App

1. Make sure the dataset file `logistics_shipments_5000.csv` is in the same directory as the script.
2. Save the Python code in a file, for example: `streamlit_app.py`
3. Run the Streamlit app with the following command:

```bash
streamlit run streamlit_app.py
```

4. The app will open in your default web browser. Use the sidebar to filter by city and explore the visualizations.

---

## File Structure

```
├── streamlit_app.py                 # Streamlit app
├── logistics_shipments_5000.csv     # Dataset (must be in the same directory)
├── README.md                        # Project documentation
```
