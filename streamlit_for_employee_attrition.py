import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
@st.cache_resource
def load_model_and_encoders():
    model = joblib.load('modelforjobattrition.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
    return model, label_encoders

try:
    model, label_encoders = load_model_and_encoders()
except Exception as e:
    st.error(f"Error loading model or encoders: {e}")
    st.stop()

# Preprocess function
def preprocess_input(input_data):
    processed = input_data.copy()
    for col in ['BusinessTravel', 'Department', 'EducationField', 'Gender', 
                'JobRole', 'MaritalStatus', 'OverTime']:
        if col in label_encoders and col in processed:
            processed[col] = label_encoders[col].transform([processed[col]])[0]
    features = ['Age','BusinessTravel','DailyRate','Department','DistanceFromHome','Education',
                'EducationField','EmployeeCount','EmployeeNumber','EnvironmentSatisfaction',
                'Gender','HourlyRate','JobInvolvement','JobLevel','JobRole','JobSatisfaction',
                'MaritalStatus','MonthlyIncome','MonthlyRate','NumCompaniesWorked','OverTime',
                'PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','StandardHours',
                'StockOptionLevel','TotalWorkingYears','TrainingTimesLastYear','WorkLifeBalance',
                'YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager']
    df = pd.DataFrame({col: [processed.get(col, 0)] for col in features})
    return df

# App Header
st.markdown("""
    <div style="background-color:#1e3c72;padding:20px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🔍 Employee Attrition Prediction</h1>
        <p style="color:#cfd8dc;text-align:center;">
            Predict whether an employee is likely to leave the company based on key factors.
        </p>
    </div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Input Form
st.markdown("### 📝 Enter Employee Details", unsafe_allow_html=True)
with st.form("employee_details"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age', min_value=18, max_value=65, value=30)
        business_travel = st.selectbox('Business Travel', ['Non-Travel', 'Travel_Frequently', 'Travel_Rarely'])
        daily_rate = st.number_input('Daily Rate', min_value=100, max_value=1500, value=800)
        department = st.selectbox('Department', ['Human Resources', 'Research & Development', 'Sales'])
        distance_from_home = st.number_input('Distance From Home (miles)', min_value=1, max_value=50, value=10)
        education = st.selectbox('Education Level', [1, 2, 3, 4, 5], help="1: Below College, 5: Doctor")
        education_field = st.selectbox('Education Field', ['Human Resources', 'Life Sciences', 'Marketing', 
                                                           'Medical', 'Other', 'Technical Degree'])
        environment_satisfaction = st.selectbox('Environment Satisfaction', [1, 2, 3, 4], help="1: Low, 4: High")
        gender = st.selectbox('Gender', ['Female', 'Male'])
        hourly_rate = st.number_input('Hourly Rate', min_value=30, max_value=100, value=50)

    with col2:
        job_involvement = st.selectbox('Job Involvement', [1, 2, 3, 4], help="1: Low, 4: High")
        job_level = st.selectbox('Job Level', [1, 2, 3, 4, 5])
        job_role = st.selectbox('Job Role', ['Healthcare Representative', 'Human Resources', 'Laboratory Technician',
                                             'Manager', 'Manufacturing Director', 'Research Director',
                                             'Research Scientist', 'Sales Executive', 'Sales Representative'])
        job_satisfaction = st.selectbox('Job Satisfaction', [1, 2, 3, 4], help="1: Low, 4: High")
        marital_status = st.selectbox('Marital Status', ['Divorced', 'Married', 'Single'])
        monthly_income = st.number_input('Monthly Income', min_value=1000, max_value=20000, value=5000)
        monthly_rate = st.number_input('Monthly Rate', min_value=2000, max_value=30000, value=15000)
        num_companies_worked = st.number_input('Number of Companies Worked', min_value=0, max_value=10, value=2)
        over_time = st.selectbox('Over Time', ['No', 'Yes'])

    # Extra fields in expander
    with st.expander("📋 Additional Details"):
        percent_salary_hike = st.number_input('Percent Salary Hike', min_value=10, max_value=25, value=15)
        performance_rating = st.selectbox('Performance Rating', [1, 2, 3, 4], help="1: Low, 4: High")
        relationship_satisfaction = st.selectbox('Relationship Satisfaction', [1, 2, 3, 4], help="1: Low, 4: High")
        stock_option_level = st.selectbox('Stock Option Level', [0, 1, 2, 3])
        total_working_years = st.number_input('Total Working Years', min_value=0, max_value=40, value=10)
        training_times_last_year = st.number_input('Training Times Last Year', min_value=0, max_value=10, value=2)
        work_life_balance = st.selectbox('Work Life Balance', [1, 2, 3, 4], help="1: Low, 4: High")
        years_at_company = st.number_input('Years at Company', min_value=0, max_value=40, value=5)
        years_in_current_role = st.number_input('Years in Current Role', min_value=0, max_value=20, value=2)
        years_since_last_promotion = st.number_input('Years Since Last Promotion', min_value=0, max_value=20, value=1)
        years_with_curr_manager = st.number_input('Years With Current Manager', min_value=0, max_value=20, value=2)

    # Fixed values
    employee_count = 1
    employee_number = 1
    standard_hours = 80

    submitted = st.form_submit_button('🔮 Predict Attrition')

# Prediction and result
if submitted:
    input_data = {
        'Age': age,
        'BusinessTravel': business_travel,
        'DailyRate': daily_rate,
        'Department': department,
        'DistanceFromHome': distance_from_home,
        'Education': education,
        'EducationField': education_field,
        'EmployeeCount': employee_count,
        'EmployeeNumber': employee_number,
        'EnvironmentSatisfaction': environment_satisfaction,
        'Gender': gender,
        'HourlyRate': hourly_rate,
        'JobInvolvement': job_involvement,
        'JobLevel': job_level,
        'JobRole': job_role,
        'JobSatisfaction': job_satisfaction,
        'MaritalStatus': marital_status,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies_worked,
        'OverTime': over_time,
        'PercentSalaryHike': percent_salary_hike,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StandardHours': standard_hours,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': training_times_last_year,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': years_in_current_role,
        'YearsSinceLastPromotion': years_since_last_promotion,
        'YearsWithCurrManager': years_with_curr_manager
    }

    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)
    prediction_proba = model.predict_proba(processed_data)

    st.subheader('📊 Prediction Results')
    if prediction[0] == 1:
        st.error(f'🚨 Prediction: Attrition (Probability: {prediction_proba[0][1]:.2%})')
        st.metric(label="Attrition Risk", value="High", delta=f"{(prediction_proba[0][1]*100):.1f}%")
        st.info("This employee is likely to leave the company.")
    else:
        st.success(f'✅ Prediction: No Attrition (Probability: {prediction_proba[0][0]:.2%})')
        st.metric(label="Attrition Risk", value="Low", delta=f"-{(100 - prediction_proba[0][0]*100):.1f}%")
        st.info("This employee is predicted to stay.")

    st.progress(int(prediction_proba[0][1]*100))

    if hasattr(model, 'coef_'):
        st.subheader('🔧 Top Factors Influencing Prediction')
        coef_df = pd.DataFrame({
            'Feature': processed_data.columns,
            'Importance': model.coef_[0]
        }).sort_values('Importance', key=abs, ascending=False)

        st.dataframe(coef_df.head(10).style.background_gradient(cmap='coolwarm').format({"Importance": "{:.4f}"}))

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center;color:gray">
        🚀 Developed with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)
