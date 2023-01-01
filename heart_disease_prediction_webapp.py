# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:48:33 2022

@author: LENOVO
"""
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:\softwares/trained_model.sav' ,'rb'))

#creating  a function for prediction

def heart_disease_prediction(input_data):
    


    #change the input data to a numpy array

    input_data_as_numpy_array=np.asarray(input_data)

    #Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
      return 'The Person does not have heart disease'
    else:
      return 'Person has heart disease' 

def main():
    #giving a title
    st.title('Heart Disease Prediction Web App')
    
    #getting input data from the user
    
    age = st.number_input('Enter Your Age')
    sex = st.number_input('Enter Your Sex')
    cp = st.number_input('Enter Your CP')
    trestbps = st.number_input('Enter Your resting blood pressure (trestbps)')
    chol = st.number_input('Enter Your cholestrol level')
    fbs = st.number_input('Enter You fasting blood sugar (fbs)')
    restecg = st.number_input('Enter Your  resting electrocardiographic (restecg)')
    thalach = st.number_input('Enter The persons maximum heart rate achieved (Thalach)')
    exang = st.number_input('Enter Exercise induced angina (Exang)')
    oldpeak = st.number_input('Enter Your Oldpeak')
    slope = st.number_input('Enter Your slope')
    ca = st.number_input('Enter Your ca')
    thal = st.number_input('Enter Your thal')
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([    age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    
    
    st.success(diagnosis) 
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    