import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/credit_model.pkl")

st.title("Credit Scoring Model")

age = st.number_input("Age", min_value=18, max_value=100)

sex = st.selectbox("Sex", ["Male", "Female"])

job = st.selectbox("Job", [0, 1, 2, 3])

housing = st.selectbox("Housing", ["Own", "Rent", "Free"])

saving_accounts = st.selectbox(
    "Saving Accounts",
    ["little", "moderate", "quite rich", "rich"]
)

checking_account = st.selectbox(
    "Checking Account",
    ["little", "moderate", "rich"]
)

credit_amount = st.number_input("Credit Amount", min_value=0)

duration = st.number_input("Duration (Months)", min_value=1)

purpose = st.selectbox(
    "Purpose",
    [
        "car",
        "radio/TV",
        "education",
        "furniture/equipment",
        "business",
        "domestic appliances",
        "repairs",
        "vacation/others"
    ]
)

sex = 1 if sex == "Male" else 0

housing_map = {
    "Free": 0,
    "Own": 1,
    "Rent": 2
}

saving_map = {
    "little": 0,
    "moderate": 1,
    "quite rich": 2,
    "rich": 3
}

checking_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2
}

purpose_map = {
    "car": 1,
    "radio/TV": 5,
    "education": 3,
    "furniture/equipment": 4,
    "business": 0,
    "domestic appliances": 2,
    "repairs": 6,
    "vacation/others": 7
}

if st.button("Predict"):

    data = np.array([[
        0,  
        age,
        sex,
        job,
        housing_map[housing],
        saving_map[saving_accounts],
        checking_map[checking_account],
        credit_amount,
        duration,
        purpose_map[purpose]
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Good Credit Risk")
    else:
        st.error("Bad Credit Risk")