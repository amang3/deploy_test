import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,PhysicalHealth, MentalHealth, 
								DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
								Asthma, KidneyDisease, SkinCancer):
   
    prediction=classifier.predict([[HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,PhysicalHealth, MentalHealth, 
								DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
								Asthma, KidneyDisease, SkinCancer]])
    print(prediction)
    return prediction



def main():
    
    st.title("Heart Disease Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    BMI = st.text_input("BMI","Type Here")
    Smoking = st.text_input("Smoking","Type Here")
    AlcoholDrinking = st.text_input("AlcoholDrinking","Type Here")
    Stroke = st.text_input("Stroke","Type Here")
    PhysicalHealth = st.text_input("PhysicalHealth","Type Here")
    MentalHealth = st.text_input("MentalHealth","Type Here")
    DiffWalking = st.text_input("DiffWalking","Type Here")
    Sex = st.text_input("Sex","Type Here")
    AgeCategory = st.text_input("AgeCategory","Type Here")
    Race = st.text_input("Race","Type Here")
    Diabetic = st.text_input("Diabetic","Type Here")
    PhysicalActivity = st.text_input("PhysicalActivity","Type Here")
    GenHealth = st.text_input("GenHealth","Type Here")
    SleepTime = st.text_input("SleepTime","Type Here")
    Asthma = st.text_input("Asthma","Type Here")
    KidneyDisease = st.text_input("KidneyDisease","Type Here")
    SkinCancer = st.text_input("SkinCancer","Type Here")

    result=""
    if st.button("Predict"):
        result = predict_note_authentication(HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,PhysicalHealth, 
                                            MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, 
                                            PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
	main()