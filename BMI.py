import streamlit as st
import matplotlib.pyplot as plt

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home","BMI calculator","BMI Categories Chart"])
if page == "Home":
    st.title("Welcome to the BMI Analyzer APP")
    st.write("""
             This app helps you calculate your body mass index (BMI) and visually understand what it means.
             Navigate to BMI Calculator to calculate yours
             """)
elif page == "BMI Calculator":
    st.title("BMI Calculator")

    with st.form("bmi_form"):
        name=st.text_input("Enter your name: ")
        age = st.number_input("Enter your age", min_value = 1, max_value=120)
        gender = st.radio("Gender",["Male","Female"])
        height = st.number_input("Height (in cm)", min_value = 50.0, max_value=250.0)
        weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=300.0)
        submitted=st.form_submit_button("calculate BMI")

    if submitted:
        if height and weight:
            bmi = weight/((height/100)**2)
            st.success(f"{name}, your BMI is: **{bmi:.2f}**")

            if bmi < 18.5:
                category = "Underweight"
                color = "blue"

            elif 18.5<=bmi<24.9:
                category = "Normal weight"
                color = "green"

            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "orange"

            else:
                category = "Obese"
                color = "red"
            st.markdown(f"BMI Category: {color}[{category}]")
        else:
            st.warning ("Please enter valid height and weight")

elif page == "BMI Calculator":
    st.title("BMI Calculator")

    with st.form("bmi_form"):
        name=st.text_input("Enter your name: ")
        age=st.number_input("enter your age", min_value=1, max_value=120)
        gender = st.radio("Gender",["Male","Female","Other"])
        height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0)
        weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=300.0)
        submitted = st.form_submit_button("Calculate BMI")

    if submitted:
        if height and weight:
            bmi = weight / ((height / 100) ** 2)
            st.success(f"{name}, your BMI is: **{bmi:.2f}**")

            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
                color = "green"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"

            st.markdown(f"### BMI Category: :{color}[{category}]")
        else:
            st.warning("Please enter valid height and weight.")

elif page == "BMI Categories Chart":
    st.title("📊 BMI Categories Chart")

    categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
    bmi_ranges = [18.4, 24.9, 29.9, 40]

    colors = ['blue', 'green', 'orange', 'red']

    fig, ax = plt.subplots()
    bars = ax.bar(categories, bmi_ranges, color=colors)
    ax.set_title("BMI Range Chart")
    ax.set_ylabel("Upper Limit of BMI")
    st.pyplot(fig)

    st.info("""
    - **Underweight**: < 18.5  
    - **Normal**: 18.5 - 24.9  
    - **Overweight**: 25 - 29.9  
    - **Obese**: ≥ 30
    """)