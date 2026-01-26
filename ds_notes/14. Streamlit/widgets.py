'''
This code is to demonstrate the various web-application components that are already available in Streamlit
'''

import streamlit as st
import pandas as pd

st.title("Widgets App")

## To take name as input text
name = st.text_input("Enter your name : ")
if name:
    st.write(f'Hello {name} !')

## To take age as slider input ranging from 0 to 100
age = st.slider("Select your age : ",0,100,25)
st.write(f'Your age is {age}')

## To select a subject using drop down (select box)
options = ["Python", "C", "C++", "Java"]
choice = st.selectbox("Select the subect you want to enroll", options)
st.write(f'You have selected {choice}')

## To display a DataFrame
data = {
    "Name":["Ram", "Laxman", "Krishna", "Balram"],
    "Age":[22,19,7,9],
    "City":["Ayodhya", "Lanka", "Dwaraka", "Kurukshetra"]
}
df = pd.DataFrame(data)
st.write("DataFrame: ")
st.write(df)

## To upload a CSV file and read the CSV file
upload_file = st.file_uploader("Choose a CSV file: ", type="csv")

if upload_file is not None:
    uploaded_file_read = pd.read_csv(upload_file)
    st.write("Uploaded CSV File")
    st.write(uploaded_file_read)