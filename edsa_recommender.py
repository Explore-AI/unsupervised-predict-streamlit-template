"""

	Streamlit webserver-based Recommender Engine.

	Author: Explore Data Science Academy.

	Note:
	---------------------------------------------------------------------
	Please follow the instructions provided within the README.md file
	located within the root of this repository for guidance on how to use
	this script correctly.

	NB: !! Do not remove/modify the code delimited by dashes !!

	This application is intended to be partly marked in an automated manner.
	Altering delimited code may result in a mark of 0.
	---------------------------------------------------------------------

	Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
	and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

#EDA
from datetime import datetime
import matplotlib.pyplot as plt 
import seaborn as sns
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles, load_rating, load_movie, load_test
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
rating_df = load_rating('resources/data/ratings.csv')
movie = load_movie('resources/data/movies.csv')
# test = load_movie('resources/data/test.csv').head(100000)

rating_df['rating_year'] = rating_df['timestamp'].apply(lambda timestamp: datetime.fromtimestamp(timestamp).year)
ax1 = rating_df.groupby('rating_year')['rating'].count()
# Merging the train and movies data on the movieId column
train = rating_df.merge(movie, on='movieId')

# Merging the test and movies data on the movieId column
# test = test.merge(movie, on='movieId')
# test_list = test['title'].tolist()
# Creating a list of all the genres 
movie_genres = []
train['genres'].apply(lambda genres: movie_genres.extend(genres.split('|')))
movie_genres = sorted(set(movie_genres))
gen = movie['genres'].explode()
# print(movie_genres)
# Creating a genre count column, for the number of genres a movie belongs to
train['genre_count'] = train['genres'].apply(lambda genres: len(genres.split('|')))
#========================================================================
show_slide = """<div  style:"margin: 0 auto";>
	<!-- this is the embed code provided by Google -->
	<iframe src="https://www.canva.com/design/DAE_Lpx-0xI/LfUkdvogjDFwo48f8DYgVw/edit?utm_content=DAE_Lpx-0xI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>    <!-- Google embed ends -->
	</div>"""
#========================================================================
html_overview = """
				<figure style:"align:center;"><img alt="" src="https://cdn-images-1.medium.com/max/591/1*KQxKzb8hE2_t72TBRFl2Bg.png", style:"align:center"><figcaption style="text-align:center;">The diagram above represents recommendation system with collaborative filtering.</figcaption></figure>
				<a>In this project we were given two approaches that acted as a starting point, namely collerborative and content based filtering.</a>
				<br></br>
				<ul><li>Content based filtering: uses item features to recommend similar items to the ones that a user has previously liked or interacted with.</li><li>Collaborative filtering: identifies items that a user will like based on how similar users rated each item. Netflix identifies shows and movies users will enjoy by determining which content similar users&nbsp;watched.</li></ul>
				<br></br>
				<p>As a Team we decided on developing a collaborative filtering recommender engine, we will only look at the building process of a CF model<p>
				<h3>Requirements To Get Started</h3>
				<p>To build the Model for recommender, we used these packages: Pandas, numpy, Surprise, a Python scikit package built for collaborative filtering</p>
				<h3>Surprise<h3>
				<p>
					we used suprise's built in user-ratings matrix conversion, we started supplying a train dataframe that contains a user id column, an item id column, and a rating column.
					From there, Surprise helped us generate a user-ratings matrix where each user id is a row and each movie the company offers is a column. This had the same impact as creating a Pandas pivot table. We then divided the dataframe into a train and test set with an 80/20 split.
				</p>
				<h3>algorithms</h3>
				<p>
				   Surprise offers 11 different prediction algorithms including variations of KNN and dimensionality reduction techniques such as SVD and NMF. For this demonstration, we ended up using svd. 
				</p>
				<ul>
					<li>SVD: A matrix factorization technique popularized by Simon Funk as part of the Netflix prize.</li>
				</ul>

				<h3>Model Accessment</h3>
				<p>
					There are two ways to assess model performance. Qualitatively, you can look at a given user and determine if the recommendation makes sense given other products they like. For example, if someone likes horror movies and doesn’t like romantic comedies, The Shining would be a good recommendation relative to Love Actually. For this dataset, we did not have information about each product, only a movie id so we used a quantitative measure, root mean squared error. A combination of the two methods is ideal, though a quantitive measure is much more realistic in production
				</p>
				<h3>Model Tuning</h3>
				<p>The surprise package offers an option to tune parameters using GridSearchCV. We provided GridSearchCV with a dictionary of parameters and the rmse will be calculated and compared for every combination of the parameters.</p>

				"""

def get_genre_count(number_of_genres, movie_genres, df):  
	genre_count = [0] * len(movie_genres)
	for index, genres in df[df['genre_count'] == number_of_genres]['genres'].items():
		for genre in genres.split('|'):
			genre_count[movie_genres.index(genre)] += 1            
	return genre_count

# App declaration
def main():

	# DO NOT REMOVE the 'Recommender System' option below, however,
	# you are welcome to add more options to enrich your app.
	page_options = ["Recommender System","EDA", "Solution Overview", "Slides", "About"]

	# -------------------------------------------------------------------
	# ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
	# -------------------------------------------------------------------
	page_selection = st.sidebar.selectbox("Choose Option", page_options)
	if page_selection == "Recommender System":
		# Header contents
		st.write('# Movie Recommender Engine')
		st.write('### EXPLORE Data Science Academy Unsupervised Predict')
		st.image('resources/imgs/Image_header.png',use_column_width=True)
		# Recommender System algorithm selection
		sys = st.radio("Select an algorithm",
					   ('Content Based Filtering',
						'Collaborative Based Filtering'))

		# User-based preferences
		st.write('### Enter Your Three Favorite Movies')
		movie_1 = st.selectbox('First Option',title_list[14930:15200])
		movie_2 = st.selectbox('Second Option',title_list[25055:25255])
		movie_3 = st.selectbox('Third Option',title_list[21100:21200])
		fav_movies = [movie_1,movie_2,movie_3]

		# Perform top-10 movie recommendation generation
		if sys == 'Content Based Filtering':
			if st.button("Recommend"):
				try:
					with st.spinner('Crunching the numbers...'):
						top_recommendations = content_model(movie_list=fav_movies,
															top_n=10)
					#st.title("We think you'll like:")
					st.title("Here are the movies Recommender for you!!!")
					for i,j in enumerate(top_recommendations):
						st.subheader(str(i+1)+'. '+j)
				except:
					st.error("Oops! Looks like this algorithm does't work.\
							  We'll need to fix it!")


		if sys == 'Collaborative Based Filtering':
			
			if st.button("Recommend"):
				try:
					with st.spinner('Crunching the numbers...'):
						top_recommendations = collab_model(movie_list=fav_movies,
														   top_n=10)
					#st.title("We think you'll like:")
					st.title("Here are the movies Recommender for you!!!")
					for i,j in enumerate(top_recommendations):
						st.subheader(str(i+1)+'. '+j)
				except:
					st.error("Oops! Looks like this algorithm does't work.\
							  We'll need to fix it!")


	# -------------------------------------------------------------------

	# ------------- SAFE FOR ALTERING/EXTENSION -------------------
	if page_selection == "Solution Overview":
		st.title("Solution Overview")
		# st.write("Describe your winning approach on this page")
		with st.container():
			st.write("---")
			# left_column, right_column = st.columns(2)
			# with left_column:
			st.header("SVD")
			st.write("##")
			st.write(
					"""
					In this project, we succeeded in building an unsupervised machine learning model that is able to recommend movies based on content-based or collaborative filtering and is capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences. Our top performing model has a root mean squared error (RMSE) of 0.78, based on a testing set submitted to the EDSA Kaggle competition.

					The singular value decomposition (SVD) algorithm is a baseline approach to recommender systems, as it has a broad range of applications including dimensionality reduction, solving linear inverse problems, and data fitting. The SVD algorithm generally performs better on large datasets compared to some other models as it decomposes a matrix into constituent arrays of feature vectors corresponding to each row and each column.
					"""
				)
	if page_selection == "Slides":
		st.markdown(show_slide,unsafe_allow_html=True)

	#Building About us page
	if page_selection == 'About':
		with st.container():
			
			# left_column, right_column = st.columns(2)
			# with left_column:
			st.header("About App")
			st.write("---")
			# st.write("##")
			st.write(
					"""
					STATA Consulting was founded in 1995 by some of the brightest minds at Silicon Valley’s leading companies, Some of our clients include Google, Yahoo!, Oracle, and Facebook. 

					The Movie Recommender App was built for a client implementing recommendation algorithm based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences.

					"""
				)
			# st.markdown(html_overview,unsafe_allow_html=True)

	# You may want to add more sections here for aspects such as an EDA,
	# or to provide your business pitch.
	if page_selection == "EDA":
		#Ratings by year
		st.subheader("**This dashboard gives insights on the dataset used for the recommender engine** 📊 ")
		# st.markdown(eda_header,unsafe_allow_html=True)
		
		if st.checkbox("View Ratings by year"):
			fig = px.bar(ax1, title="Ratings by year", height=500)
			st.plotly_chart(fig)
			st.write("The ratings for the movies span a period of 25 years, from 1995 all the way to 2019, with the last 5 years accumalatively having had the most ratings in comparison to any othe other 5 year interval. From 2006 to 2014 there is decline in user engagement when it comes to rating movies. Prior to 2006 there are 3 good years with ratings above 500000 ratings for the year, 3 more years at 400000 ratings and 3 below 300000 ratings for the year. it would be of interest to the spending behaviour of users for each of these years, as that would tell the complete story.")
		if st.checkbox("Top 30 Genre in Dataset"):
			fig = plt.figure(figsize=(20, 10))
			ax = sns.countplot(x=gen, order=gen.value_counts().index[:30],color='red')
			ax.set_title('Top Genres', fontsize=15)
			plt.xticks(rotation =90)
			st.pyplot(fig)
			st.write("As seen from the figure above, movies that are categorised as 'DRAMA', 'COMEDY', 'DOCUMENTARY' tends to be rated more than other genres.")
		if st.checkbox("View WordCloud of Genres"):
			st.set_option('deprecation.showPyplotGlobalUse', False)
			text = list(set(gen))
			plt.rcParams['figure.figsize'] = (13, 13)
			wordcloud = WordCloud(max_font_size=50, max_words=100,background_color="#FFD6CD").generate(str(text))
			plt.imshow(wordcloud,interpolation="bilinear")
			plt.axis("off")
			st.pyplot()
if __name__ == '__main__':
	main()
