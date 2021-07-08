import streamlit as st
import pandas as pd

df = pd.read_csv('C:\\streamlit\iris.csv')
st.write(df)
