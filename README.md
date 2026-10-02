# Student Early Warning Performance Prediction System

An end-to-end machine learning web application built with Streamlit and XGBoost to predict student performance and identify academic risk early in the semester.

## Key Features
- **Early Risk Detection:** Predicts student outcome categories (Pass, Fail, Distinction) based on VLE engagement and assessment data.
- **Interactive Dashboard:** Allows users to filter test cases and explore performance metrics visually.
- **Pre-trained Model:** Powered by an XGBoost classifier trained on historical student engagement data.

## Tech Stack
- **Frontend / Dashboard:** Streamlit
- **Machine Learning:** XGBoost, Scikit-Learn
- **Data Processing:** Pandas, NumPy
- **Version Control:** Git & GitHub Desktop

## Project Structure
```text
.
├── Data_Science_Lab/        # Notebooks & raw data processing scripts
└── Final_Dashboard_App/     # Streamlit app directory
    ├── app.py               # Main application code
    ├── xgboost_student_model.json  # Trained model weights
    └── test_students.csv    # Sample dataset for testing
