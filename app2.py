import streamlit as st
import pandas as pd
import plotly.express as px

a = st.sidebar.radio('R:',[1,2])

st.header('My First App')
st.markdown('Sandeep Kumar')
df = pd.read_csv('iris.csv')
graph = px.line(df, x= 'sepal.length', y='sepal.width') 
st.plotly_charts(graph)

st.write(df)
