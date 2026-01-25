import streamlit as st
import numpy as np
import pandas as pd

## Title of the application
st.title("Hello Streamlit !")

## To write simple text
st.write("This is some sample data")

df = pd.DataFrame(
    {
        'first column':[1,2,3,4],
        'second column':[10,20,30,40]
    }
)

## To display the DataFrame
st.write("This is the sample dataframe")
st.write(df)

## Data to create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)

st.write("This is the line chart for random dataframe")

## To create the line chart
st.line_chart(chart_data)