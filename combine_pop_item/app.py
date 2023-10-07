import pandas as pd
import streamlit as st


df = pd.read_csv(r'./popular_app/best_movies.csv') 

st.title("Welcome to WBSFLIX")
st.markdown("##Most Popupal Movies Ever")

number = st.number_input('How many top movies do you want to see?', step=1, min_value=2, value=2)
displayed_df = df[:number]

st.data_editor(displayed_df, num_rows="dynmic", hide_index=True)
