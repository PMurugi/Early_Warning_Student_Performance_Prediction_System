import os
import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
import shap
import matplotlib.pyplot as plt

# 1. Page Configuration
st.set_page_config(page_title="Early-Warning Student Predictor", layout="wide")
st.title("Academic Advisor Dashboard: Early-Warning System")
st.markdown("Select a student's profile to predict their academic risk based on their first 4 weeks of engagement.")

# 2. Loading the AI Model and the Student Data
# Get directory of current script (Final_Dashboard_App folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_data():
    model = XGBClassifier()
    # Use BASE_DIR to build full path to model and dataset
    model_path = os.path.join(BASE_DIR, "xgboost_student_model.json")
    data_path = os.path.join(BASE_DIR, "test_students.csv")
    
    model.load_model(model_path)
    students = pd.read_csv(data_path)
    return model, students

model, students = load_data()

# 3. Sidebar: Select a Student
st.sidebar.header("Student Selection")
# Create a fake ID list just for the prototype
student_ids = [f"Student #{i}" for i in range(1, len(students) + 1)]
selected_student = st.sidebar.selectbox("Select a Student ID:", student_ids)

# Find the exact row of the selected student
student_index = student_ids.index(selected_student)
student_data = students.iloc[[student_index]].astype(float)

# 4. The Prediction Button
if st.sidebar.button("Analyze Student Risk"):
    
    # AI makes the prediction
    prediction = model.predict(student_data)[0]
    probability = model.predict_proba(student_data)[0][1] * 100
    
    # Display the Result
    st.subheader("Prediction Results")
    if prediction == 1:
        st.error(f"HIGH RISK DETECTED. Probability of Failing/Withdrawing: {probability:.2f}%")
        
        # 5. Explainable AI (SHAP)
        st.markdown("### Why is this student at risk? (SHAP Explanation)")
        st.write(student_data.dtypes)
        st.write(student_data)
        
        # Create SHAP explainer
        explainer = shap.Explainer(model.predict, student_data)

        # Explain the selected student
        shap_values = explainer(student_data)

        # Create the waterfall plot
        plt.figure(figsize=(8, 5))
        shap.plots.waterfall(shap_values[0], max_display=5, show=False)

        st.pyplot(plt.gcf())
        plt.clf()
        
        # 6. Evidence-Based Intervention
        st.warning("**Recommended Intervention:** The chart above shows the exact metrics driving this risk score. If early clicks or quiz scores are the top red factors, immediately schedule a check-in meeting to assess LMS connectivity issues or provide academic tutoring.")
        
    else:
        st.success(f"LOW RISK. Probability of Failing/Withdrawing: {probability:.2f}%")
        st.info("**Status:** This student is engaging consistently. No immediate intervention required.")
