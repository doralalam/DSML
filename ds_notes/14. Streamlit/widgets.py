import streamlit as st

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