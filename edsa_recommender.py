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
test1 = pd.read_csv('resources/data/testfrac.csv')
svdpkl = joblib.load('resources/models/SVD.pkl')
 
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

# changing background colour
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')
#@st.cache(persist=True)
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.title("Pages")
    page_selection = st.sidebar.radio(label="",options = ["Information","EDA and Insights","Recommender System","Solution Overview", "Business Pitch"])
    
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
        st.write("As movie watchers we are always looking for new movies to watch; however, it is usually a herculean task simply finding the right one to watch from the millions of movies available in the catalogue. For this reason; we created both content-based and collaborative-based recommender systems with the given dataset. The purpose of this recommendation system is to search for content that would be interesting to the user. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user.")
        st.write("In Content-based Filtering, we seek to make recommendations based on how similar the properties or features of an item are to other items, and this proved to be a challenge for our content-based recommender system. Furthermore; as a result of the lack of computing capacity, cosine transformation was only performed on a small fraction of the data. Collaborative-based filtering is the best performing recommendation system with an impressive RMSE score, which focuses around actual ratings given by users to movies, and are compared against ratings predicted by an algorithm.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


    # Build information page
    if page_selection == "Information":
        st.title('Recommender Systems')
        st.info("A recommender system is a subclass of information filtering system that seeks to predict the rating or preference a user would give to an item")
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        
        if st.button("How does the app work"):
                    app_info = open("resources/info.md").read() 
                    st.markdown(app_info,unsafe_allow_html=True) 
        
        if st.button("Data description"):
                    data_descript = open("resources/data_description.md").read()
                    st.markdown(data_descript,unsafe_allow_html=True)

        raw_data = pd.merge(left=train,right=movies, on='movieId') 
        st.subheader("Raw movies data")
        if st.checkbox('Show data'):  # data is hidden if box is unchecked
                    st.write(raw_data.head())  # will write the df to the page
    
    # Build EDA page
    if page_selection == "EDA and Insights":
        st.title('Exploratory Data Analysis and Insights')
        st.info("The main characteristics of the data are summarized and insights are drawn.")
        st.write('###  Use the sidebar to view visuals and insights for particular variables')

        # Adding to sidebar
        variable_selection = st.sidebar.radio(label="Select variable(s):",options = ["Genres","Ratings","Genres and Ratings",'Runtime',"Movies","Directors"])

        if variable_selection == "Genres":
            a = pd.melt(df_genres)
            plt.figure(figsize=(10,8))
            sns.countplot(data=a.loc[a['value'] == 1], y='variable', palette = 'viridis')
            plt.title('* Some movies are labelled with multiple genres')
            plt.suptitle('Number of movies belonging to each category', fontsize=15)
            plt.xlabel('Count')
            plt.ylabel('')
            st.pyplot()

            st.markdown("This graphs shows the number of movies in each genre, some movies are labelled with multiple genres. It is quite clear that drama is the most popular genre, with comedy falling second. Film-Noir and IMAX genres are the least popular genres.<br><br>Film noir is a style of filmmaking characterized by such elements as cynical heroes, stark lighting effects, frequent use of flashbacks, intricate plots, and an underlying existentialist philosophy.The genre was prevalent mostly in American crime dramas of the post-World War II era. This shows that Film noir is associated with some Western and war genres, therefore might share half of the movies in the western and war genres. Western and war genres seem to have a small number of movies, this shows why film noir has an even lower number.", unsafe_allow_html=True)

        if variable_selection == "Genres and Ratings":
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
                plt.pie(genre_ratings[names[i-1]], colors=colours, radius=2, autopct='%0.1f%%',pctdistance=1.2)
                fig.set_size_inches(20, 16) 
                plt.title(names[i-1], pad=58, fontsize=14)
            plt.legend(labels, title='Rating', fancybox=True, loc=6, bbox_to_anchor=(1.7,6.8))
            st.pyplot()

            st.markdown("The pie charts show the ratings associated with each genre. Based on the number of ratings attained by each genre, it can be seen that the rating of 4 has the bigger piece of the pie for all of the genres. This supports the findings on the ratings distribution graph which showed that a vast majority of the movies are rated 4. <br><br>It is also evident that the lower ratings have small percentages for all the genres.",unsafe_allow_html=True)

        if variable_selection == "Ratings":
            # Examine movie ratings from all users
            plt.figure(figsize=(6,4))
            sns.countplot(train['rating'], palette = 'viridis')
            plt.title('Distribution of ratings from all users')
            plt.xlabel('Rating')
            plt.ylabel('Count')
            st.pyplot()

            st.markdown("From the plot and table above it is evident that majority of users gave the movies a rating of 4, 26.53% of them to be precise, while the lowest rating 0.5 accounts for only 1.58% of the users.<br><br> It can also be seen that the ratings are left skewed, whiich suggests that most of the movies have high ratings and also that the mean is lower than the mode.", unsafe_allow_html=True)

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
            st.write("Preview movies dataframe:")
            st.write(movies.head(3))

            st.write("#### Use the selectbox below to navigate the visuals")

            options = ['Top 20 movies with highest rating', 'Top 20 most rated movies','Top 20 movies with highest relevance']
            selection = st.selectbox("Choose Option", options)

            # Merge dataframes for rating analysis
            movies_train_df = pd.merge(train,movies, how='left',on='movieId')
            movies_train_df['title'] = movies_train_df['title'].str.replace('(\(\d\d\d\d\))', '')

            if selection == 'Top 20 movies with highest rating':

                    # group movies by title and rating 
                    rating_grouped = movies_train_df.groupby(['title'])[['rating']].sum()
                    high_rated = rating_grouped.nlargest(20,'rating')

                    plt.figure(figsize=(30,30))
                    plt.title('Top 20 movies with highest rating',fontsize=40)
                    colours = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.ylabel('ratings',fontsize=30)
                    plt.xticks(fontsize=25,rotation=90)
                    plt.xlabel('movies title',fontsize=30)
                    plt.yticks(fontsize=25)
                    plt.bar(high_rated.index,high_rated['rating'],linewidth=3,edgecolor=colours,color=colours)
                    plt.subplots_adjust(bottom=0.7)
                    plt.xticks(rotation=60, ha='right')
                    st.pyplot()

                    st.markdown('This graph shows the top 20 highest rated movies. The(1994) Shawshank Redemption is the highest rated movie taking the number 1 spot. The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the 1982 Stephen King novella Rita Hayworth and Shawshank. Following at number 2 is the pulp fiction.The ratings are grouped based on the title the calculate the sum of the ratings to get a total.', unsafe_allow_html=True)

            if selection == 'Top 20 most rated movies':

                    # group movies by title and rating
                    no_ratings_df = movies_train_df.groupby('title')[['rating']].count()
                    rating_count_20 = no_ratings_df.nlargest(20,'rating')

                    # plot movies with the highest number of ratings
                    plt.figure(figsize=(30,30))
                    plt.title('Top 20 movies with highest number of ratings',fontsize=40)
                    colours = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.xticks(fontsize=25,rotation=90)
                    plt.yticks(fontsize=25)
                    plt.xlabel('movies title',fontsize=30)
                    plt.ylabel('ratings',fontsize=30)
                    plt.bar(rating_count_20.index,rating_count_20.rating,color=colours)
                    plt.subplots_adjust(bottom=0.7)
                    plt.xticks(rotation=60, ha='right')
                    st.pyplot()

                    st.markdown('This graph shows most rated movies. The(1994) Shawshank Redemption is the most rated movie in the dataset. If we combine these findings with the ones on the "highest rated movies" plot we can see that it is not only the most rated movie but the users are rating it very high, which can lead to the conlusion that it a satisfying movie.', unsafe_allow_html=True)

            if selection == 'Top 20 movies with highest relevance':

                    # Create a merged dataframe with g_scores and movies
                    genome_movies_df = pd.merge(g_scores,movies, how='left',on='movieId')
                    genome_train_grouped = genome_movies_df.groupby(['title'])[['relevance']].sum()
                    high_relevance = genome_train_grouped.nlargest(20,'relevance')

                    plt.figure(figsize=(30,30))
                    plt.title('Top 20 movies with highest relevance',fontsize=40)
                    colors = ['forestgreen','burlywood','gold','azure','magenta','cyan','aqua','navy','lightblue','khaki']
                    plt.ylabel('Relevance',fontsize=30)
                    plt.xticks(fontsize=25,rotation=90)
                    plt.xlabel('Movies title',fontsize=30)
                    plt.yticks(fontsize=25)
                    plt.bar(high_relevance.index,high_relevance['relevance'],linewidth=3,edgecolor=colors,color=colors)
                    plt.subplots_adjust(bottom=0.7)
                    plt.xticks(rotation=60, ha='right')
                    st.pyplot()

                    st.markdown('The above graph shows the top 20 most relevant movies. These are the movies that can connect to people and can also be recommended to new users that do not have a history in a platform', unsafe_allow_html=True)


        if variable_selection == 'Runtime':

            plt.figure(figsize=(6,4))
            plt.hist(imdb['runtime'], color = 'skyblue', edgecolor = 'black',
                     bins = int(100/5))
            plt.xlim(0,250)

            # seaborn histogram
            sns.distplot(imdb['runtime'], hist=True, kde=False, 
                        bins=int(100/5), color = 'green',
                        hist_kws={'edgecolor':'black'})
            # Add labels
            plt.title('Distribution of Movie Runtimes')
            plt.xlabel('Runtime')
            plt.ylabel('Movies')
            st.pyplot()

            # Getting the five number summary and boxplot of runtimes
            st.write("#### Five number summary and boxplot")

            summary = imdb['runtime'].describe(include='all')
            st.write(summary)

            st.markdown('The average runtime for a movie is 102.72 minutes, it can also be seen from the graph that there is a huge spike of frequency at the 100 minutes runtime. The shortest movie runs for 1 minute and the longest movie runs for 750 minutes, which suggests an anomaly with the value.', unsafe_allow_html=True)

        if variable_selection == "Directors":
            directors_movies = df[['director']]  # Create dataframe to analyse director variable

            directors_movies['count'] = 1
            directors_movies = directors_movies.groupby('director').sum().sort_values(by='count', ascending=False)

            directors_rating = df[['director', 'movieId']]
            directors_rating = pd.merge(left=directors_rating, right=train, left_on='movieId', right_on='movieId')
            directors_rating.drop(['movieId', 'userId', 'timestamp'], axis=1, inplace=True)
            directors_rating = directors_rating.groupby('director').mean().sort_values(by='rating', ascending=False)

            directors = pd.merge(left=directors_rating, right=directors_movies, left_index=True, right_index=True)

            # Sort directors dataframe by rating and count to analyse by both
            directors_rating = directors.sort_values(by=['rating'], ascending=False)
            directors_count = directors.sort_values(by=['count'], ascending=False)

            st.write("#### Use the selectbox below to navigate the visuals")

            options = ['Highest ranking directors', "Highest number of movies a director worked on","Lowest number of movies a director worked on"]
            selection = st.selectbox("Choose Option", options)

            if selection == 'Highest ranking directors':

                    # Examine performance of directors
                    # Because each director has directed different number of movies, we will calculate a weighted score for each using their mean movie rating and number of movies directed
                    directors = df[['director', 'movieId']]
                    directors = pd.merge(left=directors, right=train, left_on='movieId', right_on='movieId')
                    directors.drop(['userId', 'timestamp'], axis=1, inplace=True)
                    directors = directors.groupby('director', as_index=False).agg({'movieId': 'count', 'rating': 'mean'})
                    all_movies = directors['movieId'].sum()
                    directors['movieId'] = directors['movieId'] / all_movies * 100
                    directors['score'] = directors['movieId'] * directors['rating']
                    directors = directors.sort_values('score', ascending=False)
                    directors = directors.set_index('director')

                    # Examine top 10 rated directors
                    fig, ax = plt.subplots(figsize=(12, 9))  #(15, 10)

                    people = directors.index[:10]
                    y_pos = np.arange(len(people))

                    performance = directors['score'][:10]

                    ax.barh(y_pos, performance, align='center', color=sns.color_palette(palette='viridis', n_colors=10))
                    ax.set_yticks(y_pos)
                    ax.set_yticklabels(people)
                    ax.invert_yaxis()  # labels read top-to-bottom
                    ax.set_xlabel('Score (weighted mean rating)',fontsize=13)
                    ax.set_title('Highest ranking directors', pad=20, fontsize=30)
                    st.pyplot()

                    st.markdown('Here we examined the best directors by calculating a weighted score comprising the number of movies directed and the rating of each movie. The results indicate the Quentin Tarantino has directed the most, high rating movies in the database. This is followed by a number of authors and directors suggesting that there may be an error in the data.', unsafe_allow_html=True)

            if selection == "Highest number of movies a director worked on":

                    plt.xticks(rotation=90,fontsize=7)
                    plt.subplots_adjust(bottom=0.3)
                    plt.bar(directors_count.index[0:20], height=directors_count['count'][0:20], color=sns.color_palette(palette='viridis', n_colors=20))
                    plt.title("Highest number of movies a director worked on",fontsize=12, pad=20)
                    plt.ylabel("Number of movies directed",fontsize=8)
                    plt.xlabel("Director",fontsize=8)
                    st.pyplot()

                    st.markdown('Insights on visualization', unsafe_allow_html=True)

            if selection == "Lowest number of movies a director worked on":

                    plt.bar(directors.index[-20:], height=directors['count'][-20:],
                    color=sns.color_palette(palette='viridis', n_colors=20))
                    plt.xticks(rotation=90,fontsize=7)
                    plt.subplots_adjust(bottom=0.3)
                    plt.title("Lowest number of movies a director worked on",fontsize=12, pad=20)
                    plt.ylabel("Number of movies directed",fontsize=8)
                    plt.xlabel("Director",fontsize=8)
                    st.pyplot()

                    st.markdown('Insights on visualization', unsafe_allow_html=True)

    
    if page_selection == "Business Pitch":
                st.title('Business Proposal')
                st.write("Looking at the current and increased demand of precise and accurate movie recommender models. We have developed an application that evaluates the appetite of viewers and utilizes aggregates that would be able to satisfy your viewers. Considering that the structure of viewership from a television channel is vastly different from that of online movie hosts, in regards that the online movie viewers have the liberty to choose the film of their choice at any given time whereas on television there are restriction on choice and prefered time to watch the film.")
                st.write("Given that a high population of the world uses the internet and television to view movies,  we have structured our web app so that it would be able to render solutions and insights for both the platforms. We will observe the TV platform then followed by the online platform.")

                st.write('### 1. Television Platform')
                st.write('The limitation of choice on TV has led us to use world aggregates to determine the top movies that would mesmerize the clients. First we will observe the top rated genres world wide: below are pie charts showing each genre and their respective ratings.')


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
                        plt.pie(genre_ratings[names[i-1]], colors=colours, radius=2, autopct='%0.1f%%',pctdistance=1.2)
                        fig.set_size_inches(20, 16) 
                        plt.title(names[i-1], pad=58, fontsize=14)
                plt.legend(labels, title='Rating', fancybox=True, loc=6, bbox_to_anchor=(1.7,6.8))
                st.pyplot()

                st.write('Now that we have the top genres we could filter out movies and get the top movies of the top genres and thus base our movie playlist from that perspective.')

                st.write('### 2. Online Movie Platform')
                st.write('When approaching the internet platform we will apply some of the most popular and proven recommender algorithms to make catered recommendations for each individual. The application is based primarily on the concept shown on the Recommender System page, where a content and a collaborative model were used to make movie predictions. The following is an example of results produced for a specific user in our dataset. Below you can see a table showing the top 10 movies recommended for user no. 777.')
                userx = pd.read_csv('resources/data/userec.csv')
                st.write(userx['title'][:10])


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
