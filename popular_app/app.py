import pandas as pd
import streamlit as st


df = pd.read_csv(r'popular_app/best_movies.csv') 

st.data_editor(df)





