import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


st.header("PURCHASE PREDICTOR")

st.write("Demo of linear rergression")

Gender = st.text_input(label="Enter gender")
Age = st.number_input(label="Enter Age",min_value=0.0,max_value=120.0,value=50.00,step=1.0)
EstimatedSalary = st.number_input(label="Enter Salary in Rupees",min_value=1000.0,max_value=999999999.9,value=1000.00,step=1.0)

submitted = st.button('Submit')


if submitted:
    pickled_model = pickle.load(open('model.pkl','rb'))

    new_data=pd.DataFrame({'Gender': [''], 'Age': [], 'EstimatedSalary': []})
    new_data['Gender'] = le.fit_transform(new_data['Gender'])
    prediction = pickled_model.predict(new_data)

    prediction_result = 'Will purchase' if prediction[0] == 1 else 'Will not purchase'
    print("Prediction:", prediction_result)

    
    st.write(f"Expected outcome is {prediction_result[0]}")