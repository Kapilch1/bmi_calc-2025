import streamlit as st
st.markdown(
    """
    <style>
        .stApp {
            background-color:	#e8f5e9; /* light blue, you can change to any hex color */
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("BMI Calculator")

height = st.number_input("Enter your Height in cm:", min_value=1)
weight = st.number_input("Enter your Weight in kg:", min_value=1)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
        elif bmi < 25:
            st.info("You have a normal weight.")
        else:
            st.error("You are overweight.")
    else:
        st.error("Please enter valid height and weight.")
