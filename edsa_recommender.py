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
import joblib
import os
import pickle
from markdown import markdown

# Data handling dependencies
import pandas as pd
import numpy as np

# Import visualisations
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


# Import label encoder
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies = pd.read_csv('resources/data/movies.csv')
imdb = pd.read_csv('resources/data/imdb_data.csv')
tags = pd.read_csv('resources/data/tags.csv')
train = pd.read_csv('resources/data/train.csv')
g_tags = pd.read_csv('resources/data/genome_tags.csv')
g_scores = pd.read_csv('resources/data/genome_scores.csv')

 
# Drop duplicates from movies dataset
movies.drop_duplicates(keep='first', inplace=True)

# Merging dataframes
# Ensure movies['genres'] column contains strings and split into a list of genres
movies['genres'] = movies['genres'].apply(str).apply(lambda x: x.split('|'))
# Create a label binarizer class
mlb = MultiLabelBinarizer()
# Create a new dataframe with the binarized genres
df_genres = pd.DataFrame(mlb.fit_transform(movies['genres']), columns=mlb.classes_)
df = pd.merge(left=movies,right=df_genres, left_index=True, right_index=True)
        
# Ensure imdb['title_cast', 'plot_keyword'] columns contain strings and split into strings
imdb['title_cast'] = imdb['title_cast'].apply(str).apply(lambda x: x.split('|'))
imdb['plot_keywords'] = imdb['plot_keywords'].apply(str).apply(lambda x: x.split('|'))

# Merge imdb data with df
df = pd.merge(left=df,right=imdb, left_on='movieId', right_on='movieId')

df['year'] = df['title'].str.extract('(\d\d\d\d)')
df['budget'] = df['budget'].str.replace('$', '').str.replace(',','')


#@st.cache(persist=True)
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.title("Pages")
    page_selection = st.sidebar.radio(label="",options = ["Information","EDA and Insights","Recommender System","Solution Overview"])
    
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
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
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


    # Build information page
    if page_selection == "Information":
        st.write('### Recommender Systems')
        st.info("A recommender system is a subclass of information filtering system that seeks to predict the rating or preference a user would give to an item")
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        
        if st.button("How does the app work"):
                    app_info = open("resources/info.md").read() 
                    st.markdown(app_info,unsafe_allow_html=True) 
        
        if st.button("Data description"):
                    data_descript = open("resources/data_description.md").read()
                    st.markdown(data_descript,unsafe_allow_html=True)

        st.subheader("Raw data")
        if st.checkbox('Show data'):  # data is hidden if box is unchecked
                    st.write(df.tail())  # will write the df to the page
    
    # Build EDA page
    if page_selection == "EDA and Insights":
        st.write('## Exploratory Data Analysis and Insights')
        st.info("The main characteristics of the data are summarized and insights are drawn.")
        st.write('###  Use the sidebar to view visualizations and insights for particular variables')

        # Adding to sidebar
        variable_selection = st.sidebar.radio(label="Select variable(s):",options = ["Genres","Ratings","Movies","Genre and Ratings","Directors"])

        if variable_selection == "Genres":
            a = pd.melt(df_genres)
            plt.figure(figsize=(10,8))
            sns.countplot(data=a.loc[a['value'] == 1], y='variable', palette = 'viridis')
            plt.title('* Some movies are labelled with multiple genres')
            plt.suptitle('Number of movies belonging to each category', fontsize=15)
            plt.xlabel('Count')
            plt.ylabel('')
            st.pyplot()

            st.markdown('Insights on visualization', unsafe_allow_html=True)

        if variable_selection == "Genre and Ratings":
            # Calculate the number of ratings per genre of movie
            df_genres['movieId'] = df['movieId']
            genre_ratings = pd.merge(left=train, right=df_genres, left_on='movieId', right_on='movieId')
            genre_ratings.drop(['userId', 'movieId', 'timestamp'], axis=1, inplace=True)
            genre_ratings = genre_ratings.groupby(by=['rating'], axis=0).sum()

            # Examine how the different movie genres are historically rated by users
            names = list(genre_ratings.columns)
            labels = list(genre_ratings.index)
            colours = sns.color_palette(palette='viridis', n_colors=len(labels), desat=None)

            fig = plt.figure()
            fig.subplots_adjust(hspace=1, wspace=1)
            for i in range(1, 21):
                plt.subplot(4, 5, i)
                plt.pie(genre_ratings[names[i-1]], colors=colours, radius=1.8, autopct='%0.1f%%',pctdistance=1.2)
                fig.set_size_inches(20, 16)
                plt.title(names[i-1], pad=58, fontsize=14)
            plt.legend(labels, title='Rating', fancybox=True, loc=6, bbox_to_anchor=(1.8, 6.5))
            st.pyplot()

            st.markdown('Insights on visualization', unsafe_allow_html=True)

        if variable_selection == "Ratings":
            # Examine movie ratings from all users
            plt.figure(figsize=(6,4))
            sns.countplot(train['rating'], palette = 'viridis')
            plt.title('Distribution of ratings from all users')
            plt.xlabel('Rating')
            plt.ylabel('Count')
            st.pyplot()

            st.markdown('From the plot above it is evident that a lot of users gave the movies a rating of 4, 38.89% of them to be precise. It can also be seen that the ratings are left skewed, whiich suggests that most of the movies have high ratings and also that the mean is lower than the mode.  ', unsafe_allow_html=True)

            # Five number summary
            st.write("#### Five number summary and boxplot")

            summary = train['rating'].describe(include='all')
            st.write(summary)

            # Box plot
            plt.boxplot(train['rating'])
            plt.ylabel("Rating")
            plt.xlabel("movies")
            st.pyplot()

            st.markdown('On average a user is most likely to give a movie a rating of 3.5257. The lowest rating given to a movie is 0.5, which is visible from the boxplot and that it is an outlier, meaning that it is an event that is less likely to occur. The standard deviation of the data is low which indicates that the ratings that the users make are usually closer to the mean.<br><br> The boxplot is also confirming that the ratings are left skewed, as it is visible that the mean value is lower than the mode which is 4, as seen on the distribution plot.', unsafe_allow_html=True)

        if variable_selection == "Movies":

            # Preview the movies datframe
            st.write("Preview of movies dataframe:")
            st.write(movies.head(3))

            st.write("#### Use the selectbox below to navigate the visuals")

            options = ['Top 20 movies with highest rating', 'Top 20 movies with highest number of ratings','Top 20 movies with highest relevance','Top 10 movies with longest runtime']
            selection = st.selectbox("Choose Option", options)

            # Merge dataframes for rating analysis
            movies_train_df = pd.merge(train,movies, how='left',on='movieId')
            movies_train_df['title'] = movies_train_df['title'].str.replace('(\(\d\d\d\d\))', '')

            if selection == 'Top 20 movies with highest rating':

                    # group movies by title and rating 
                    rating_grouped = movies_train_df.groupby(['title'])[['rating']].sum()
                    high_rated = rating_grouped.nlargest(20,'rating')

                    plt.figure(figsize=(30,10))
                    plt.title('Top 20 movies with highest rating',fontsize=40)
                    colours = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.ylabel('ratings',fontsize=30)
                    plt.xticks(fontsize=25,rotation=90)
                    plt.xlabel('movies title',fontsize=30)
                    plt.yticks(fontsize=25)
                    plt.bar(high_rated.index,high_rated['rating'],linewidth=3,edgecolor=colours,color=colours)
                    plt.subplots_adjust(bottom=0.5)#,height=0.8)
                    st.pyplot()

            if selection == 'Top 20 movies with highest number of ratings':

                    # group movies by title and rating
                    no_ratings_df = movies_train_df.groupby('title')[['rating']].count()
                    rating_count_20 = no_ratings_df.nlargest(20,'rating')

                    # plot movies with the highest number of ratings
                    plt.figure(figsize=(30,10))
                    plt.title('Top 20 movies with highest number of ratings',fontsize=40)
                    colours = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.xticks(fontsize=25,rotation=90)
                    plt.yticks(fontsize=25)
                    plt.xlabel('movies title',fontsize=30)
                    plt.ylabel('ratings',fontsize=30)
                    plt.bar(rating_count_20.index,rating_count_20.rating,color=colours)
                    st.pyplot()

            if selection == 'Top 20 movies with highest relevance':

                    # Create a merged dataframe with g_scores and movies
                    genome_movies_df = pd.merge(g_scores,movies, how='left',on='movieId')
                    genome_train_grouped = genome_movies_df.groupby(['title'])[['relevance']].sum()
                    high_relevance = genome_train_grouped.nlargest(20,'relevance')

                    plt.figure(figsize=(30,10))
                    plt.title('Top 20 movies with highest relevance',fontsize=40)
                    colors = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.ylabel('Relevance',fontsize=30)
                    plt.xticks(fontsize=25,rotation=90)
                    plt.xlabel('Movies title',fontsize=30)
                    plt.yticks(fontsize=25)
                    plt.bar(high_relevance.index,high_relevance['relevance'],linewidth=3,edgecolor=colors,color=colors)
                    st.pyplot()


            if selection == 'Top 10 movies with longest runtime':

                    imdb_movies = pd.merge(imdb,movies, how='left',on='movieId')
                    df_runtime = imdb_movies.groupby(['title'])[['runtime']].sum()
                    long_runtime = df_runtime.nlargest(10,'runtime')

                    plt.figure(figsize=(30,10))
                    plt.title('Top 10 movies with longest runtime',fontsize=40)
                    colours = ['forestgreen','burlywood','gold','forestgreen','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.ylabel('Movie runtime (in minutes)',fontsize=30)
                    plt.xticks(fontsize=20,rotation=90)
                    plt.xlabel('Movies title',fontsize=30)
                    plt.yticks(fontsize=20)
                    plt.bar(long_runtime.index,long_runtime['runtime'],linewidth=3,edgecolor=colours,color=colours)
                    st.pyplot()

        if variable_selection == "Directors":
            directors_movies = df[['director']]  # Create dataframe to analyse director variable

            directors_movies['count'] = 1
            directors_movies = directors_movies.groupby('director').sum().sort_values(by='count', ascending=False)

            directors_rating = df[['director', 'movieId']]
            directors_rating = pd.merge(left=directors_rating, right=train, left_on='movieId', right_on='movieId')
            directors_rating.drop(['movieId', 'userId', 'timestamp'], axis=1, inplace=True)
            directors_rating = directors_rating.groupby('director').mean().sort_values(by='rating', ascending=False)

            directors = pd.merge(left=directors_rating, right=directors_movies, left_index=True, right_index=True)

            st.write("#### Use the selectbox below to navigate the visuals")

            options = ['Top 20 directors with high rated movies', 'Top 20 directors with low rated movies','Top 20 directors with the most projects','Top 20 directors with the least projects']
            selection = st.selectbox("Choose Option", options)

            if selection == 'Top 20 directors with high rated movies':
                    
                    directors = directors.sort_values(by=['rating'], ascending=False)

                    plt.bar(directors.index[0:20], height=directors['rating'][0:20], color=sns.color_palette(palette='viridis', n_colors=20))
                    plt.title("Directors with high rated movies")
                    plt.ylabel("Rating")
                    plt.xlabel("Director")
                    plt.xticks(rotation=60)
                    st.pyplot()

                    table = directors.iloc[0:20,:-1] # view as a table to read names better
                    st.write(table)

            if selection == 'Top 20 directors with the most projects':

                    directors = directors.sort_values(by=['count'], ascending=False)

                    plt.bar(directors.index[0:20], height=directors['count'][0:20], color=sns.color_palette(palette='viridis', n_colors=20))
                    plt.title("Number of movies a director worked on")
                    plt.ylabel("Number of movies directed")
                    plt.xlabel("Director")
                    plt.xticks(rotation=60)
                    st.pyplot()

                    table = directors.iloc[0:20,-1] # view as a table to read names better
                    st.write(table)

            if selection == 'Top 20 directors with low rated movies':

                    directors = directors.sort_values(by=['rating'], ascending=False)

                    plt.bar(directors.index[-20:], height=directors['rating'][-20:], color=sns.color_palette(palette='viridis', n_colors=20))                    
                    plt.title("Directors with low rated movies")
                    plt.ylabel("Rating")
                    plt.xlabel("Director") 
                    plt.xticks(rotation=60)
                    st.pyplot()

                    table = directors.iloc[-20:,:-1] # view as a table to read names better
                    st.write(table)

            if selection == 'Top 20 directors with the least projects':

                    directors = directors.sort_values(by=['count'], ascending=False)

                    plt.bar(directors.index[-20:], height=directors['count'][-20:], color=sns.color_palette(palette='viridis', n_colors=20))                    
                    plt.title("Number of movies a director worked on")
                    plt.ylabel("Number of movies directed")
                    plt.xlabel("Director")
                    plt.xticks(rotation=60)
                    st.pyplot()

                    table = directors.iloc[-20:,-1] # view as a table to read names better
                    st.write(table)
    

    st.sidebar.title("About")
    st.sidebar.info(
        """ 
        This app is maintained by EDSA students.
        It serves as a project for an unsupervised machine learning sprint.
        
    
        **Authors:**\n
        Caryn Pialat\n
        Kganedi Magolo\n
        Lesego Bhebe\n
        Nombulelo Msibi\n
        Tshokelo Tumelo Mokubi\n
        Tuduetso Mmokwa\n
    
    """
    )
if __name__ == '__main__':
    main()
