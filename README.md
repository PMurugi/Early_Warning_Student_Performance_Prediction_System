# Early Warning Student Performance Prediction System

[Click here to launch the Live Dashboard](https://earlywarningstudentperformancepredictionsystem-szadadrnhqwzurt.streamlit.app/)

An end-to-end machine learning web application built with **Streamlit and XGBoost** to identify students who may be at risk of failing or withdrawing early in the semester. The system uses early student engagement and assessment-related features and provides **SHAP-based explanations** to show which features contributed to each prediction.

## Dataset Attribution

This project is trained and evaluated using the **Open University Learning Analytics Dataset (OULAD)**. OULAD contains information about students, courses, assessments, and interactions with the Virtual Learning Environment (VLE).

### Key Indicators

* VLE engagement and click activity
* Assessment-related features
* Student demographic information
* Early academic performance indicators

### Target Outcome

The system treats **Fail/Withdrawn** as the academic-risk class and predicts whether a student is at risk based on early-semester information.

## Key Features

* **Early Risk Detection:** Identifies students who may be at risk of failing or withdrawing based on early-semester indicators.
* **Interactive Dashboard:** Allows an academic advisor to select a student and analyze their predicted academic risk.
* **XGBoost Prediction Model:** Uses a trained XGBoost classifier to generate student risk predictions and probabilities.
* **SHAP Explainability:** Provides a visual explanation of the features that contributed to an individual prediction.
* **Intervention Support:** Provides an example intervention recommendation based on the factors contributing to the predicted risk.

## How to Use the Dashboard

1. **Select a Student ID:** Choose a student from the sidebar dropdown.
2. **Analyze Student Risk:** Click **Analyze Student Risk** to generate the prediction.
3. **View Prediction:** The dashboard displays the predicted risk level and probability of failing/withdrawing.
4. **View SHAP Explanation:** If the student is identified as high risk, the dashboard displays a SHAP waterfall chart showing the features that contributed to the prediction.
5. **Review Intervention:** Use the explanation to understand which factors may require attention and guide an appropriate academic intervention.

## Tech Stack

* **Dashboard:** Streamlit
* **Machine Learning:** XGBoost, Scikit-Learn
* **Explainable AI:** SHAP
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib
* **Version Control:** Git & GitHub

## Project Structure

```text
.
├── Data_Science_Lab/
│   └── # Notebooks and data processing work
│
└── Final_Dashboard_App/
    ├── app.py                         # Main Streamlit application
    ├── requirements.txt               # Python dependencies
    ├── xgboost_student_model.json     # Trained XGBoost model
    ├── test_students.csv              # Sample test data
    └── run_app.bat                    # Windows launcher
```

## Running the Application Locally

Clone the repository and navigate to the application directory:

```bash
cd Final_Dashboard_App
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will then open in a web browser.

## Project Purpose

The goal of this project is to demonstrate how machine learning and explainable AI can support **early identification of students who may require academic support**. Rather than providing only a prediction, the system uses SHAP explanations to make the model's decision-making process more understandable to academic advisors.

## Important Note

The system is intended as an **academic decision-support prototype**. Its predictions should not replace the judgment of academic advisors or other educational professionals. The model identifies patterns associated with academic risk; a prediction does not establish that a student will definitely fail or withdraw.
