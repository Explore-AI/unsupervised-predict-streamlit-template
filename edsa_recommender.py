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

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#custom files
# Custom Libraries
from utils.data_loader import (load_movie_titles, read_file,\
                                local_css, remote_css)
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from views import (html_temp, eda_header, rec_header, sweet, prof,\
                    html_overview, slides, home)
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():
    ''' html_template = """
    <div style="background-color:black;padding:10px;border-radius:10px;margin:10px;">
    <h1 style="color:green;text-align:center;">EDSA Movie Recommendation Challenge</h1>
    <h2 style="color:white;text-align:center;">UNSUPERVISED LEARNING PREDICT - TEAM8</h2>
    </div>
    """
    
    title_template ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:20px;">
    <h1 style="color:white;text-align:center;">UNSUPERVISED LEARNING PREDICT</h1>
    <h2 style="color:white;text-align:center;">TEAM 8</h2>
    <h3 style="color:white;text-align:center;"> Amanda</h3>
    <h3 style="color:white;text-align:center;">Ibrahim</h3>
    <h3 style="color:white;text-align:center;">Nichodemus</h3>
    <h3 style="color:white;text-align:center;">Christian</h3>
    <h3 style="color:white;text-align:center;">Bernard</h3>
    <h2 style="color:white;text-align:center;">6 May 2022</h2>
    </div>
    """ '''
    page_options = ["Recommender System","Solution Overview", "Meet The Team"]
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/img/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
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
                    st.title("We think you'll like:")
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
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    options = ["Exploratory Data Analysis", "Feature Engineering", "Modelling"]
    
    if page_selection == "Solution Overview":
        # st.title("Solution Overview")
        # selection = st.radio("Explore Our Options", options)
        selection = st.sidebar.selectbox("Navigation", options)
        
        if selection == "Exploratory Data Analysis":

            st.image('resources/img/Exploratory-Data-Analysis.jpg',use_column_width=True)
            st.markdown(eda_header,unsafe_allow_html=True)

            st.write("Some insights we got from our Exploratory Data Analysis consisted of key attributes such as :")
            if st.checkbox("Average Movie Ratings"):
            # st.write("## Average Movie Ratings")
                st.image('resources/img/averageratings.png',use_column_width=True)
                st.write("The average rating across all movies was skewed to the right. Most ratings were between 3 & 4. There were very few movies rated at less than 3 ")
                
                
            if st.checkbox("Distributins of user ratings for movies over the 25 years"):
                st.image("resources/imgs/dst.PNG", use_column_width=True)
                st.image("resources/imgs/dst1.PNG", use_column_width=True)
                st.image("resources/imgs/dst2.png", use_column_width=True)
                st.write("For the entire 25 year period, a rating of 4.0 is the most abundant rating given by users to movies,\
                followed by a rating of 3.0. Ratings of 5.0, 3.5 and 4.5 are next most numerous ratings users give to movies.\
                When the the 25 years are divided into 5, 5 year periods, the first 5 year period between 1995 and 1999,\
                there is an anomaly in the ratings, quite different from th other periods,\
                but still with ratings of 4.0 and 3.0 being the most abundant, followed by a 5.0 rating.\
                The last 3 intervals there is a contant pattern that has emerged with the distributions of the ratings")
                #components.html()
                
                        #Ratings distributions across movie genres
            if st.checkbox("Ratings distributions across movie genres"):
                st.image("resources/imgs/ratings_by_year.png", use_column_width=True)
                st.write("Movies with between 1 to 4 genres have the most number of ratings for the 25 years, with an average rating for these of roughly bewteen 3.5 to 3.6. Movies with 2 and 3 genres movies get the lions share of the ratings.")
                #components.html()
            if st.checkbox("Count of Movies per Release year"):

                # st.write("## Count of Movies per Release year")
                st.image('resources/img/r-year.png',use_column_width=True)
                st.write("It was observed that there is a sharp increase in the number of movies released from year 2000. 2015 had the highest number of released movies with 2500+ movies, the least number of movies were released in 1993, with less than 700 movies released.")
            if st.checkbox("Most Popular Genres In Data Set"):

            # st.write("## Most Popular Genres In Data Set")
                st.image('resources/img/top-g.png',use_column_width=True)
                st.write("Some observations we made here were that, the most common genre by far was Drama (25,000+ movies), followed by Comedy (17,000+ movies) and Thriller (around 9,000 movies).The least common genres were IMAX and Film-Noir, which both appeared in less than 500 movies.  ")
            # if st.checkbox("Wordcloud showing most common genres"):
            #     st.subheader("Top Genres")
            #     st.image('resources/images/gentres.png',use_column_width=True)
            
            if st.checkbox("Wordcloud Of Most Popular Movies"):

            # st.write("## Wordcloud Of Most Popular Movies")
                st.image('resources/img/movieratingswordcloud.png',use_column_width=True)
                
            if st.checkbox("Most Occuring Movie Rating"):

                # st.write("## Most Occuring Movie Rating")
                st.image('resources/img/ratingscountchart.png',use_column_width=True)
  
        if selection == "Feature Engineering":
            st.title("Feature Engineering") 
            st.image('resources/img/feature.png',use_column_width=True)
        
            st.markdown("""
			We performed feature extraction in the following steps:
   
            - Removed entries with missing values
            
            - Merged data sets
            
            - Extract Release year
            
            - Create corpus for each movie 
			
			""")
        if selection == "Modelling":
            # st.markdown(html_temp,unsafe_allow_html=True)
            # st.markdown(html_overview,unsafe_allow_html=True)
            st.title("Our Approach To Building The Movie Recommender Engine")
            st.image('resources/images/coll-cont-pic.png',use_column_width=True)
            st.write("The diagram above represents recommendation system with collaborative and content based filtering.")
            
            st.write("In this project, our team was tasked to use two approaches that acted as a starting point, namely collerborative and content based filtering.")
            st.write("## Content-based Recommendation")
            st.write("This system recommends items based on similarities. It looks at the properties of an item and tries to look at different items that have similar properties and recommends them to the user. In Content-based Filtering, we seek to make recommendations based on **how similar the properties of an item are to other items.**")
            st.write("Given a movie or list of movies, we can look at its features and compare it to the features of others movies, in so doing,  we'll find similaries bewteen the movies and can reccomend movies based on the level of similarity it shares with the given movie or movie list.")
            st.write("Here we implemented a simple content-based recommender system that takes a movie title and return a list of movies that are most similar to the title given. We **assume that individuals like similar items** such that our recommender system suggests to the use similar movies based on the movie we give (movie name would be the input) in which case it will extract similar movies or based on all of the movies watched by a user (user is the input) where it will look at the user's history and suggest movies similar to the ones the user has been watching in the past.")
 
            st.write("""Overall some of the pros of using content-based recommendation is:
                     
        * No need for data on other users, thus no cold-start or sparsity problems.
        
        * Can recommend to users with unique tastes.
        
        * Can recommend new & unpopular items.
        
        * Can provide explanations for recommended items by listing content-features
            ** (in this case we use genre)
                
                

        However some of the limitations are :

        * It does not recommend items outside a user's content profile
        
        * It is unable to exploit quality judgements of other users
        
        * Consumers might have multiple interests""")	


            st.write("## Collaborative-Based Filtering")
            st.write("""
                    Our content based engine suffers from some severe limitations. It is only capable of suggesting movies which are *similar* to a certain movie. That is, it is not capable of capturing *tastes* and providing recommendations across genres.
                    
                    Also, the engine that we built is not really personal in that it **doesn't capture the personal tastes and biases of a user**. Anyone querying our engine for recommendations based on a movie will receive the same recommendations for that movie, regardless of who s/he is. 
                    
                    Therefore, we used a technique called **Collaborative Filtering** to make recommendations to Movie Watchers. Collaborative Filtering is based on the idea that similarity between users can be used to predict how much a user will like a particular product or service that other users have used/experienced but s/he have not. Collaborative filtering doesn’t need anything else but users’ historical preference on a set of items. The assumption is that people like things similar to other things they like, and things that are liked by other people with similar taste.
                    
                    Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users. It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. It looks at the items they like and combines them to create a ranked list of suggestions.
                    
                    Amazon is known for its use of collaborative filtering, matching products to users based on past purchases. For example, the system can identify all of the products a customer and users with similar behaviors have purchased and/or positively rated. It then can identify other products in any product category the target user may like, computing similarities between products, suggesting them to them through recommendations.

                    There are two types of Collaborative filtering: Memory-based and model-based collaborative filtering approaches.""")
            
            st.write("## Model-Based Collaborative Filtering")
            st.write("""We will trained and evaluated the performance of the models based on a 100k subset of the data. The best performing model will underwent hyperparameter tuning and was the trained on the full dataset for the submission file.""")
            st.write("""
            We used **Surprise**
            
            Surprise is a very valuable tool that can be used within Python to build recommendation systems. Its Documentation is quite useful and explains its various prediction algorithms’ packages. Before we start building a model, it is important to import elements of surprise that are useful for analysis, such as certain model types (SVD, KNNBasic, KNNBaseline, KNNWithMeans, and many more), Dataset and Reader objects (more on this later), accuracy scoring, and built in train-test-split, cross validation and GridSearch.""")
            st.write("""
                     From the Suprise library, the follwoing algorithms were used:

                        ### Basic algorithms
                        ***NormalPredictor:*** this algorithm predicts a random rating based on the distribution of the training set, which is assumed to be normal.

                        ***BaselineOnly:*** this algorithm predicts the baseline estimate for given user and item.

                        ### k-NN algorithms
                        ***KNNBasic:*** this is a basic collaborative filtering algorithm.

                        ***KNNWithMeans:*** this is a basic collaborative filtering algorithm, taking into account the mean ratings of each user.

                        ***KNNWithZScore:*** this is a basic collaborative filtering algorithm, taking into account the z-score normalization of each user.

                        ***KNNBaseline:*** is a basic collaborative filtering algorithm taking into account a baseline rating.

                        ### Matrix Factorization-based algorithms
                        ***SVD:*** this algorithm is equivalent to Probabilistic Matrix Factorization ( which makes use of data provided by users with similar preferences to offer recommendations to a particular user).

                        ***SVDpp:*** this algorithm is an extension of SVD that takes into account implicit ratings.

                        ***NMF:*** this is a collaborative filtering algorithm based on Non-negative Matrix Factorization. It is very similar with SVD.

                        ***SlopeOne:*** this is a straightforward implementation of the SlopeOne algorithm.

                        ***Coclustering:*** is a collaborative filtering algorithm based on co-clustering.

                     """)
            
                                        
            st.write("## Model Performance")
            st.write("""We built and tested six different collaborative filtering models and compared their performance using a statistical measure known as the root mean squared error (**RMSE**), which determines the average squared difference between the estimated values and the actual value. A low RMSE value indicates high model accuracy. The following table shows the RMSE values for the six models:""")
            st.image("resources/img/models.png")
            st.write("SVD is the best performing model with a RMSE of 0.796.")
            


    if page_selection == "Meet The Team":
        st.title("Meet the Team")
        st.image('resources/img/WhatsApp Image 2022-05-03 at 8.49.30 PM.jpeg',use_column_width=True)
		
		# You can read a markdown file from supporting resources folder
        st.markdown("""
		
		CABIN ANALYTICS consists of 5 talented data scientists and developers from various parts of Africa. These are:
		- Amanda (South Africa)
		- Nichodimus  (Kenya)
		- Ibrahim (Kenya)
		- Christian  (Nigeria)
		- Benard (Kenya)
		""")
        st.markdown("""
		CABIN ANALYTICS specializes in Information Technology Services. We take 
		data and arrange it in such a way that it makes sense for business and individual users. We also build and train models that are capable of solving a wide range of recommendations. 
		
		Our team of leading data scientists work tirelessly to make your life and the life of your customers easy.
		"""
		)
        st.markdown(""" 
		For more info:
		email: info@cabinanlytics.com
		""")
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()