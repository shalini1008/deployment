import streamlit as st
import pandas as pd

st.write("HELLO learner!!")
st.title("streamlit")
st.header("Random")

df = pd.DataFrame( 
    {
    'NAME':['john','MARRAY','SHALINI','BABY'],
    'MARKS':['75','65','90','58']
 } 
 )

st.write(df.head(4))
st.header("describation of data")
st.write(df.describe())
st.header("visualization")
st.line_chart(df['MARKS'])
