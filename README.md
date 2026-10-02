# Early Warning Student Performance Prediction System

[Click here to launch the Live Dashboard](https://earlywarningstudentperformancepredictionsystem.streamlit.app/)

An end-to-end machine learning web application built with Streamlit and XGBoost to predict student performance and identify academic risk early in the semester.

## Dataset Attribution
This project is trained and evaluated on the Open University Learning Analytics Dataset (OULAD). OULAD contains data about courses, students, and their interactions with the Virtual Learning Environment (VLE) across multiple modules.
- Key Indicators: VLE engagement clicks, assessment submission times, student demographics, and assignment scores.
- Target Outcomes: Early risk classification (Pass, Fail, or Distinction).

## Key Features
- Early Risk Detection: Classifies student performance risk levels based on OULAD VLE engagement and assessment trends.
- Interactive Dashboard: Allows users to filter test cases and explore performance metrics visually.
- Pre-trained XGBoost Model: Utilizes a tuned machine learning classifier trained on historical student interaction data.

## How to Use the Dashboard
1. Select Student ID: Choose a student ID from the sidebar dropdown to auto-load sample test data.
2. Adjust Attributes: Modify engagement metrics or assignment scores using interactive controls.
3. View Prediction: The model processes inputs in real time and displays risk levels and performance metrics.

## Tech Stack
- Frontend / Dashboard: Streamlit
- Machine Learning: XGBoost, Scikit-Learn
- Data Processing: Pandas, NumPy
- Version Control: Git & GitHub Desktop

## Project Structure
```text
.
├── Data_Science_Lab/        # Notebooks & raw data processing scripts
└── Final_Dashboard_App/     # Streamlit app directory
    ├── app.py               # Main application code
    ├── requirements.txt     # Python dependencies
    ├── xgboost_student_model.json  # Trained model weights
    └── test_students.csv    # Sample dataset for testing
