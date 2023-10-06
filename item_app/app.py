import pandas as pd
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def main(toy_story_movie_id): 
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

    # Find the movie ID for "Toy Story"
    toy_story_mask = movies["title"].str.contains('Toy Story', case=False)
    comedy_genre_mask = movies["genres"].str.contains('Comedy', case=False)
    toy_story_movie_id_XX = movies.loc[toy_story_mask & comedy_genre_mask, "movieId"].values[0] #

    # Create a DataFrame to store cosine similarities with "Toy Story"
    toy_story_cosines_df = pd.DataFrame(movies_cosines_matrix[toy_story_movie_id])

    # Rename the column to 'toy_story_cosine'
    toy_story_cosines_df = toy_story_cosines_df.rename(columns={toy_story_movie_id: 'toy_story_cosine'})

    # Remove the row corresponding to "Toy Story"
    toy_story_cosines_df = toy_story_cosines_df[toy_story_cosines_df.index != toy_story_movie_id]

    # Sort the DataFrame by cosine similarity in descending order
    toy_story_cosines_df = toy_story_cosines_df.sort_values(by="toy_story_cosine", ascending=False)

    # Calculate the number of users who rated both "Toy Story" and each recommended movie
    users_rated_both = [sum((user_movie_matrix[toy_story_movie_id] > 0) & (user_movie_matrix[movie_id] > 0)) for movie_id in toy_story_cosines_df.index]

    # Add a column for the number of users who rated both movies
    toy_story_cosines_df['users_who_rated_both_movies'] = users_rated_both

    # Filter out recommendations with less than 10 users who rated both movies
    toy_story_cosines_df = toy_story_cosines_df[toy_story_cosines_df["users_who_rated_both_movies"] > 10]

    # Display the top 10 movie recommendations based on cosine similarity to "Toy Story"
    top_10_recommendations = toy_story_cosines_df.head(10)
    return top_10_recommendations

number = st.number_input('Witch movie id? (max 193609)', step=1, min_value=1, value=1)

st.data_editor(main(number))


import time
start_time = time.time()
main()
st.text("--- %s seconds ---" % (time.time() - start_time))