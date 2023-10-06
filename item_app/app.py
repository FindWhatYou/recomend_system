import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import time

# Define a function to construct Google Drive download links
def gd_path(file_id):
    return f"https://drive.google.com/uc?export=download&id={file_id}"

# Define file IDs for 'rating' and 'movies' datasets
files_id = {
    'rating': "1F4_-HBPBSySMjxdGxlykWVjvVn9AJ0BS",
    'movies': "1PDuCaAhhVTRLYdftMr6VqX23crMqB_qg",
}

# Load data from Google Drive
rating = pd.read_csv(gd_path(files_id['rating']), sep=",")
movies = pd.read_csv(gd_path(files_id['movies']), sep=",")

# Create a user-movie rating matrix
user_movie_matrix = pd.pivot_table(data=rating,
                                values='rating',
                                index='userId',
                                columns='movieId',
                                fill_value=0)

# Calculate cosine similarity between movies
movies_cosines_matrix = pd.DataFrame(cosine_similarity(user_movie_matrix.T),
                                    columns=user_movie_matrix.columns,
                                    index=user_movie_matrix.columns)

def calculate_recommendations(option): 
    # Find the movie ID for the selected movie
    movie_mask = movies["title"] == option
    movie_id = movies.loc[movie_mask, "movieId"].values[0]

    # Create a DataFrame to store cosine similarities with the selected movie
    movie_cosines_df = pd.DataFrame(movies_cosines_matrix[movie_id])

    # Rename the column to 'movie_cosine'
    movie_cosines_df = movie_cosines_df.rename(columns={movie_id: 'movie_cosine'})

    # Remove the row corresponding to the selected movie
    movie_cosines_df = movie_cosines_df[movie_cosines_df.index != movie_id]

    # Sort the DataFrame by cosine similarity in descending order
    movie_cosines_df = movie_cosines_df.sort_values(by="movie_cosine", ascending=False)

    # Calculate the number of users who rated both the selected movie and each recommended movie
    users_rated_both = [sum((user_movie_matrix[movie_id] > 0) & (user_movie_matrix[recommend_id] > 0)) for recommend_id in movie_cosines_df.index]

    # Add a column for the number of users who rated both movies
    movie_cosines_df['users_who_rated_both_movies'] = users_rated_both

    # Filter out recommendations with less than 10 users who rated both movies
    movie_cosines_df = movie_cosines_df[movie_cosines_df["users_who_rated_both_movies"] > 10]

    # Display the top 10 movie recommendations based on cosine similarity to the selected movie
    top_10_recommendations = movie_cosines_df.head(10)

    show_list = top_10_recommendations.merge(movies,how='inner', on="movieId")[['movieId','title','genres']]
    
    return show_list

# Multiselect for movies
movie_titles_list = movies['title'].tolist()

st.title("Movie Recommender")

option = st.selectbox('Select a movie:', movie_titles_list)

# Calculate recommendations and running time when the user clicks the button
if st.button('Calculate Recommendations'):
    st.write('You selected:', option)
    start_time = time.time()
    recommendations = calculate_recommendations(option)
    st.table(recommendations)
    st.text("--- %s seconds ---" % (time.time() - start_time))
