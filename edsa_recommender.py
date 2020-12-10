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

# Import seaborn library
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# To create interactive plots
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import plotly.express as px


# Data handling dependencies
import pandas as pd
import numpy as np
import codecs

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Importing data
movies = pd.read_csv('resources/data/movies.csv')
train = pd.read_csv('resources/data/ratings.csv')
df_imdb = pd.read_csv('resources/data/imdb_data.csv')

# Merging the train and the movies
df_merge1 = train.merge(movies, on = 'movieId')

from datetime import datetime
# Convert timestamp to year column representing the year the rating was made on merged dataframe
df_merge1['rating_year'] = df_merge1['timestamp'].apply(lambda timestamp: datetime.fromtimestamp(timestamp).year)
df_merge1.drop('timestamp', axis=1, inplace=True)

# -------------- Create a Figure that shows us that shows us how the Ratigs are distriuted. ----------------# 
# Get the data
data = df_merge1['rating'].value_counts().sort_index(ascending=False)

ratings_df = pd.DataFrame()
ratings_df['Mean_Rating'] = df_merge1.groupby('title')['rating'].mean().values
ratings_df['Num_Ratings'] = df_merge1.groupby('title')['rating'].count().values

genre_df = pd.DataFrame(df_merge1['genres'].str.split('|').tolist(), index=df_merge1['movieId']).stack()
genre_df = genre_df.reset_index([0, 'movieId'])
genre_df.columns = ['movieId', 'Genre']

def make_bar_chart(dataset, attribute, bar_color='#3498db', edge_color='#2980b9', title='Title', xlab='X', ylab='Y', sort_index=False):
    if sort_index == False:
        xs = dataset[attribute].value_counts().index
        ys = dataset[attribute].value_counts().values
    else:
        xs = dataset[attribute].value_counts().sort_index().index
        ys = dataset[attribute].value_counts().sort_index().values
        
    
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(title, fontsize=24, pad=20)
    ax.set_xlabel(xlab, fontsize=16, labelpad=20)
    ax.set_ylabel(ylab, fontsize=16, labelpad=20)
    
    plt.bar(x=xs, height=ys, color=bar_color, edgecolor=edge_color, linewidth=2)
    plt.xticks(rotation=45)
    
 # Merging the merge data earlier on with the df_imbd
df_merge3 = df_merge1.merge(df_imdb, on = "movieId" )   

num_ratings = pd.DataFrame(df_merge3.groupby('movieId').count()['rating']).reset_index()
df_merge3 = pd.merge(left=df_merge3, right=num_ratings, on='movieId')
df_merge3.rename(columns={'rating_x': 'rating', 'rating_y': 'numRatings'}, inplace=True)

# pre_process the budget column

# remove commas
df_merge3['budget'] = df_merge3['budget'].str.replace(',', '')
# remove currency signs like "$" and "GBP"
df_merge3['budget'] = df_merge3['budget'].str.extract('(\d+)', expand=False)
#convert the feature into a float
df_merge3['budget'] = df_merge3['budget'].astype(float)
#remove nan values and replacing with 0
df_merge3['budget'] = df_merge3['budget'].replace(np.nan,0)
#convert the feature into an integer
df_merge3['budget'] = df_merge3['budget'].astype(int)

df_merge3['release_year'] = df_merge3.title.str.extract('(\(\d\d\d\d\))', expand=False)
df_merge3['release_year'] = df_merge3.release_year.str.extract('(\d\d\d\d)', expand=False)

data_1= df_merge3.drop_duplicates('movieId')

# Movies published by year:

years = []

for title in df_merge3['title']:
    year_subset = title[-5:-1]
    try: years.append(int(year_subset))
    except: years.append(9999)
        
df_merge3['moviePubYear'] = years
print('The Number of Movies Published each year:',len(df_merge3[df_merge3['moviePubYear'] == 9999]))

def make_histogram(dataset, attribute, bins=25, bar_color='#3498db', edge_color='#2980b9', title='Title', xlab='X', ylab='Y', sort_index=False):
    if attribute == 'moviePubYear':
        dataset = dataset[dataset['moviePubYear'] != 9999]
        
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(title, fontsize=24, pad=20)
    ax.set_xlabel(xlab, fontsize=16, labelpad=20)
    #ax.set_yticklabels([yticklabels(item, 'M') for item in ax.get_yticks()])
    ax.set_ylabel(ylab, fontsize=16, labelpad=20)
    
    plt.hist(dataset[attribute], bins=bins, color=bar_color, ec=edge_color, linewidth=2)
    
    plt.xticks(rotation=45)



# ------------------------------ CODE FOR THE FIGURES ENDS HERE ------------------------------------# 

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","EDA", "Solution Overview", "About Us"]

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
    if page_selection == "EDA":
        st.header("Movie Recommender System Datasets explorer")
        st.markdown(""" This dataset shown below was extracted from set of data available from a kaggle competition obtained from the link https://www.kaggle.com/c/edsa-recommender-system-predict/data""")
        st.sidebar.header("Configuration")
        st.sidebar.subheader("Available Visuals obtained from the segmented sections below:")
        all_cols = df_merge1.columns.values
        numeric_cols = df_merge1.columns.values
        obj_cols = df_merge1.columns.values

        if st.sidebar.checkbox("Data preview", True):
            
            st.subheader("Data preview")
            st.markdown(f"Shape of dataset : {df_merge3.shape[0]} rows, {df_merge3.shape[1]} columns")
            if st.checkbox("Data types"):
                st.dataframe(df_merge3.dtypes)
            if st.checkbox("Pandas Summary"):
                st.write(df_merge1.describe())
            cols_to_style = st.multiselect(
                "Choose numeric columns to apply BG gradient", numeric_cols
                )
            st.dataframe(df_merge3.head(50).style.background_gradient(subset=cols_to_style, cmap="BuGn"))
            st.markdown("---")
        #st.markdown("<h1 style='text-align: center; color: black;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
        st.markdown("""The Data Visualisation done on this page was extracted from the a kaggle notebook which can be found from the link: 
            https://www.kaggle.com/kundaninetshiongolwe/team-5-recommenders""")



        if st.sidebar.checkbox("Visuals on Ratings"):
            if st.checkbox("Ratings count by year"):
                fig, ax = plt.subplots(1, 1, figsize = (12, 6))
                ax1 = df_merge1.groupby('rating_year')['rating'].count().plot(kind='bar', title='Ratings by year')
                st.write(fig)


            if st.checkbox("How ratings are distributed: histogram"):
                f = px.histogram(df_merge1["rating"], x="rating", nbins=10, title="The Distribution of the Movie Ratings")
                f.update_xaxes(title="Ratings")
                f.update_yaxes(title="Number of Movies per rating")
                st.plotly_chart(f)
            if st.checkbox("How ratings are distributed: scatter plot"):
                fig, ax = plt.subplots(figsize=(14, 7))
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.set_title('Rating vs. Number of Ratings', fontsize=24, pad=20)
                ax.set_xlabel('Rating', fontsize=16, labelpad=20)
                ax.set_ylabel('Number of Ratings', fontsize=16, labelpad=20)

                plt.scatter(ratings_df['Mean_Rating'], ratings_df['Num_Ratings'], alpha=0.5, color='green')
                st.pyplot(fig)

        if st.sidebar.checkbox("Visuals on Genres"):
            st.info("The number of movie per genre")
            fig=make_bar_chart(genre_df, 'Genre', title='Most Popular Movie Genres', xlab='Genre', ylab='Counts')
            st.pyplot(fig)

        if st.sidebar.checkbox("Movie published"):
            st.info("Movies published by year")
            st.pyplot(make_histogram(df_merge3, 'moviePubYear', title='Movies Published per Year', xlab='Year', ylab='Counts'))


    st.sidebar.header("About")
    st.sidebar.text("Team name : Team_5_EDSAJuly2020")
    st.sidebar.text(
        "Code : https://github.com/Thami-ex/unsupervised-predict-streamlit-template"
    )
    		
			


    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

        st.markdown("""A `Recommender System (RS)` is no doubt one of the most obvious ways in which companies are enhancing the user
            experience in the platform that they provide their customers services. Companies Like Facebook, Netflix, Amazon, and Youtube
            are using RS to do so. More likely, these companies and other companies that are implementing the RS are doing 
            so in introducing machine learning into these companies. There are a 3 available approaches into building a recommender system. 
            As part of this project we explore two of these which were the `Content Based Filtering (CBF)` and `Collaborative Filtering (CF)` algorithm.

            """)

        st.markdown("**Collaborative Filtering (CF)**")
        st.markdown("""This recommender engine was easy to implement in this work as it provides us with the recommendation of the 10 movies
            easily as compared to the other approach. On the other hand, the CF is one of the most popular implemented recommender 
            engines and it is based on the assumption that the people were in agreement in the past and there us a high chance that they
            in agreement in the future. An example indicating what is meant by the statement about agreement is considering that a friend
            and the other friend have probably liked identical range of books in the past. Because the friend has now read new books that the other has
            not read there is a high chance that the other friend will enjoy and probably like those same books. This logic describes what
            is known as `user-based` collaborative filtering which was implemented in this application. """)

    if page_selection == "About Us":
        st.markdown("<h1 style='text-align: center; color: black;'>About Us</h1>", unsafe_allow_html=True)
        image = Image.open("about_.png")
        st.image(image, use_column_width=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()