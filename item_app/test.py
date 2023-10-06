import pandas as pd

def gd_path(file_id):
    return f"https://drive.google.com/uc?export=download&id={file_id}"

# Define file IDs for 'rating' and 'movies' datasets
files_id = {
    'movies': "1PDuCaAhhVTRLYdftMr6VqX23crMqB_qg",
}

# Load data from Google Drive
movies = pd.read_csv(gd_path(files_id['movies']), sep=",")

movie_titles_list = movies['title'].tolist()

import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    (movie_titles_list))

print(option)

st.write('You selected:', option)
