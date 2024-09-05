import numpy as np
import streamlit as st
import pickle


sav_file = pickle.load(open('E:\Python3\Heart_disease_prediction\heart_disease_prediction.sav', "rb"))


def heart_disease(input):
    
    input_array = np.asarray(input)
    input_array = input_array.reshape(1,-1)
    prediction = sav_file.predict(input_array)
    if prediction[0] == 1:
      return "The person is suffered from heart disease"
    else:
      return "The person is not suffered from heart disease"


def main():
    
    st.title("Web app for heart disease prediction")
    
    age = st.text_input(
        "Enter the age of the person"
        )
    sex = st.text_input(
        "Enter the sex of the person (use 1 for male and 0 for female)"
        )
    cp = st.text_input(
        "Enter the value of chest pain (use 0-3 for low, moderate, high, very high)"
        )
    trestbps = st.text_input(
        "Enter the value of resting blood pressure (BP)"
        )
    chol = st.text_input(
        "Enter the value of chserum cholestoral level in mg/dl"
        )
    fbs = st.text_input(
        "Enter the value of fasting blood sugar (use 1 for True and 0 for false)"
        )
    restecg = st.text_input(
        "Enter the value of resting electrocardiographic results (usually b/w 0,1,2)"
        )
    thalach = st.text_input(
        "Enter the value of maximum heart rate achieved per minute"
        )
    exang = st.text_input(
        "Enter the value of exercise induced angina (use 1 for yes or 0 for no)"
        )
    oldpeak = st.text_input(
        "Enter the value of ST depression induced by exercise relative to rest (use values b/w 0-4)"
        )
    slope = st.text_input(
        "Enter the value of the slope of the peak exercise ST segment (use 0,1 and 2)"
        )
    ca = st.text_input(
        "Enter the value of number of major vessels (use the value 0-3)"
        )
    thal = st.text_input(
        "Enter the value of Thalassemia (use 0 for normal, 1 for fixed defect, 2 for reversable defect)"
        )
    res = ''

    
    if st.button("Result"):
        res = heart_disease([
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, 
            exang, oldpeak, slope, ca, thal])
    
    st.success(res)

if __name__ == '__main__':
    main()
  