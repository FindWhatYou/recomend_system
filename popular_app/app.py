import pandas as pd
import streamlit as st


df = pd.read_csv(r'./popular_app/best_movies.csv') 

number = st.number_input('Insert a number')
displayed_df = df[:number]

st.data_editor(displayed_df, num_rows="dynmic", hide_index=True)





