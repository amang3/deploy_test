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
        <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
	    HeartDisease = st.text_input("Variance","Type Here")
	    BMI = st.text_input("Variance","Type Here")
        Smoking = st.text_input("Variance","Type Here")
        AlcoholDrinking = st.text_input("Variance","Type Here")
        Stroke = st.text_input("Variance","Type Here")
        PhysicalHealth = st.text_input("Variance","Type Here")
        MentalHealth = st.text_input("Variance","Type Here")
        DiffWalking = st.text_input("Variance","Type Here")
        Sex = st.text_input("Variance","Type Here")
        AgeCategory = st.text_input("Variance","Type Here")
        Race = st.text_input("Variance","Type Here")
        Diabetic = st.text_input("Variance","Type Here")
        PhysicalActivity = st.text_input("Variance","Type Here")
        GenHealth = st.text_input("Variance","Type Here")
        SleepTime = st.text_input("Variance","Type Here")
        Asthma = st.text_input("Variance","Type Here")
        KidneyDisease = st.text_input("Variance","Type Here")
        SkinCancer = st.text_input("Variance","Type Here")
	
        result=""
        if st.button("Predict"):
            result = predict_note_authentication(HeartDisease, BMI, Smoking, AlcoholDrinking, Stroke,PhysicalHealth, 
											    MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, 
											    PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer)
        st.success('The output is {}'.format(result))