import pandas as pd
import streamlit as st


df = pd.read_csv(r'./popular_app/best_movies.csv') 
print(df)

st.data_editor(df, num_rows=20)





