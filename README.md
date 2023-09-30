# recomend_system

Popularity rankings
LESSON PROGRESS
16% Complete
Recommender systems can get complex. But, sometimes, simple solutions are the best ones. When a new customer enters the store and Ursula does not know them, she likes to recommend the favourite movies from her customers: movies that are likely to appeal to everyone.

This is exactly what first “row” of WBSFLIX page will constitute: a non-personalized recommender system and it is made of the “top” movies in the dataset.



The objective of this lesson is to end up with a notebook that would generate the titles of this mock-up page. You don’t have to worry about the design of the page or the integration with the database: you are in the experimentation phase. Your code, when complete, will be later on adapted and integrated to the back-end of the webpage. For now, we’ll be happy to just output movie titles so that we can judge the adequacy of the recommendations.

Since users have given an explicit rating to the movies, this should be as easy as grouping the “ratings” dataset by average rating, sorting the values and getting the top rated movies, right?

Well, these are the results:



These movies have a perfect rating, but probably they got it from very few reviews: Ursula would consider a movie as the “favourite of her customers” just because a single person loved it!

You have several options here:

Instead of using the average rating of the movies, get the number of ratings: a movie that has been rated many times is “popular” —it has been watched/rated by a lot of people, regardless of whether they liked it or not.
Use a hybrid method between the average rating (the “quality”) and number of ratings (the “popularity”). There are many ways to implement this hybrid method. For example:
Setting a threshold for “popularity” (e.g. movies that have been rated at least 10 times), then sorting movies just by “quality”.
Creating a new metric that mixes “popularity” and “quality”.
For this first “non-personalized” recommendations, we will not evaluate the systems numerically. Instead, you should choose the best “ranking recommender” based on your intuition: is your system recommending movies that almost nobody has watched? Is it recommending movies with too low of a rating? Ask yourself these questions and create a system that looks satisfying to you. Mathematical evaluation will come at a later stage.
