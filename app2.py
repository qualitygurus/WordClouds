import streamlit as st
import pandas as pd

st.header('My First App')
st.markdown('Sandeep Kumar')
df = pd.read_csv('iris.csv')
st.write(df)
