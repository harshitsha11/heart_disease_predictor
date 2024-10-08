import pandas as pd
import numpy as np
import datetime
import streamlit as st
import joblib
from sklearn.tree import DecisionTreeClassifier

def main():
    html_temp = """
        <h1>Heart Disease Predictor</h1>
    """

    model = joblib.load("heart_disease_predictor.joblib")

    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown("This app will help you to predict Heart Disease presence.")

    p1 = st.number_input("Please enter you age", 1,200,step=1)

    s1 = st.selectbox("Please enter your sex",("Male", "Female"))
    if s1=='Male':
        p2=0
    elif s1=='Female':
        p2=1

    p3 = st.slider("Select the CP",0,3)

    p4 = st.number_input("Enter your trestbps",1,500,step=1)

    p5 = st.number_input("Enter your Cholestrol",1,500,step=1)

    p6 = st.slider("Enter you fbs",0,2)

    p7 = st.slider("Enter you restecg",0,3)

    p8 = st.number_input("Enter you thalach",0,200,step=1)

    p9 = st.slider("Enter your exang",0,2)

    p10 = st.number_input("Enter you oldpeak",0,10,step=1)

    p11 = st.slider("Enter you slope",0,3)

    p12 = st.slider("Enter you ca",0,4)

    p13 = st.slider("Enter you thal",0,5)
    

    data_new = pd.DataFrame({
    'age':p1,
    'sex':p2,
    'cp':p3,
    'trestbps':p4,
    'chol':p5,
    'fbs':p6,
    'restecg':p7,
    'thalach':p8,
    'exang':p9,
    'oldpeak':p10,
    'slope':p11,
    'ca':p12,
    'thal':p13
    },index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        st.success(f"Do you have any Heart Disease?: {'Yes' if pred[0] == 1 else 'No'}")

if __name__ == '__main__':
    main()
