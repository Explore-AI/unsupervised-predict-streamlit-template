import streamlit as st
from PIL import Image
# Data manipulation
import pandas as pd
import numpy as np

# datetime
import datetime

# Libraries for data preparation and model building
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from surprise import Reader
from surprise.model_selection import train_test_split
from surprise import Reader
from surprise import Dataset
from surprise import SVD
from surprise.accuracy import rmse
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
# saving model
import pickle

#ignoring warnings
import warnings
warnings.filterwarnings('ignore')

#making sure that we can see all rows and cols
pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

# Header information
st.title("Movie Recommender System")
#st.write("# EXPLORE Data Science Academy Unsupervised Predict Team_14")

st.write("#")
st.image("https://149695847.v2.pressablecdn.com/wp-content/uploads/2020/11/recommender.jpg")
st.write("#")





# App declaration


    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    #page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
def main():
    About=st.sidebar.selectbox("Choose Option",("Introduction","Dataset","Literature Review","Recommender System","Solution Overview"))
    
    if About=="Introduction":
     st.write("""
## Introduction

In our daily life when we are shopping online, or looking for a movie to watch, we normally ask our friends or search for it.
 And when they recommend something that we do not like yet they enjoyed it. what a waste of time right. So what about if there 
 is a system that can understand you, and recommend for you based on your interests, that would be so cool.

The growth of the internet has resulted in an enormous amount of online data and information available to us. 
Tools like a recommender system allow us to filter the information which we want or need. Recommender systems can 
be utilized in many contexts, one of which is a playlist generator for video, movie or music services.
 Recommendation systems are becoming increasingly important in today’s extremely busy world.
  People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. 
  Therefore, the recommendation systems are important as they help them make the right choices, 
  without having to expend their cognitive resources.
 
  ## Problem statement

In today’s technology driven world, recommender systems are socially and economically critical for ensuring
that individuals are exposed to the content that is relevant to them in one way or another. One application where this is
especially true surrounds movie content recommendations; where intelligent algorithms can help viewers find great titles from 
tens of thousands of options. If customers are not exposed to a content relevant to them, may decide to look for alternatives
which may provide better content.
 
   ## Objectives

The key objective is to construct a recommendation algorithm based on content or collaborative filtering, 
capable of accurately predicting how a user will rate a movie they have not yet viewed based on their historical preferences.
""")
 #Nowadays, companies, big or small, use recommendation systems as they have become an essential part of our lives
#. Recommendetion systems are algorithms designed to recommned things to users based on different factors.
#Two types of recommendatio systems exist collaborative and content based recommender systems. Collaborative 
#based uses past item-user interactions to detect similar users or items. Content based uses additional information 
#about items or users to make a recommendation. One example is a movie recommendation system; 
#where algorithms can help users find great titles from tens of thousands of options. 
    

    if About=="Literature Review":
        st.markdown(""" ## Literature Review

What are recommender systems?

Simply put, recommender systems are the systems that are designed to recommend things to the user based on many different factors. 
These systems predict the most likely product that the users are most likely to purchase and are of interest to. Companies like Netflix, 
Amazon, etc. use recommender systems to help their users to identify the correct product or movies for them.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. 
Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user. 
Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized
list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history,
what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved 
through predictive modeling and heuristics with the data available.


Content-Based Filtering

Content-based filtering is a type of recommender system that attempts to guess what a user may like based on that user's activity. 
Content-based filtering makes recommendations by using keywords and attributes assigned to objects in a database 
(e.g., items in an online marketplace) and matching them to a user profile.

Why use content-based filtering?

i) No data from other users is required to start making recommendations
ii) Recommendations are highly relevant to the user.
iii) You avoid the “cold start” problem.

Collaborative Filtering

The idea behind collaborative filtering is to consider users’ opinions on different videos and recommend the best video 
to each user based on the user’s previous rankings and the opinion of other similar types of users.
""")   

    if About=="Dataset":
     st.write(""" ## Dataset
The dataset used is  consists of several million 5-star ratings obtained from users of the online MovieLens
 movie recommendation service. The MovieLens dataset has long been used by industry and academic researchers to improve 
 the performance of explicitly-based recommender systems.

The dataset consists of 8 CSV files:

    -genome_scores.csv - a score mapping the strength between movies and tag-related properties. Read more here
    -genome_tags.csv - user assigned tags for genome-related scores
    -imdb_data.csv - Additional movie metadata scraped from IMDB using the links.csv file.
    -links.csv - File providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs.
    -sample_submission.csv - Sample of the submission format for the hackathon.
    -tags.csv - User assigned for the movies within the dataset.
    -test.csv - The test split of the dataset. Contains user and movie IDs with no rating data.
    -train.csv - The training split of the dataset. Contains user and movie IDs with associated rating data.

""")


    if About == "Recommender System":
    
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        #movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        #movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        #movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        #fav_movies = [movie_1,movie_2,movie_3]

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
    if About == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    # create copies of the dataframes



if __name__ == '__main__':
    main()                 
Data_preprocessing=st.container()
Exploratory_Data_Analysis=st.container()

#with Data_preprocessing:
 #   st.write("## Data preprocessing")

  #  st.text("""Data preprocessing is a technique that involves taking in raw data and transforming it into a understandable 
   # format and useful. The technique includes data cleaning, intergration, transformation, reduction and discretization. 
    #The data preprocessing plan will include the following processes:

   #     i) Data cleaning
    #    ii) Table merging process
    #    iii) Dealing with missing values
        
     #   Data cleaning
     #   Data cleaning is important because it improves your data quality and in doing so, increases overall productivity.
     #   When you clean your data, all outdated or incorrect information is gone, leaving you with the highest quality information. 
     #   We aim to determine inaccurate, incomplete, or unreasonable data and then improve quality by correcting detected errors
      #  and omissions.

       # """)   


#Loading the dataset

# imdb
imdb_df = pd.read_csv("C:/Users/1375744/Desktop/streamlit/data/imdb_data.csv")

# movies
movies_df = pd.read_csv("C:/Users/1375744/Desktop/streamlit/data/movies.csv")

#tags_df = pd.read_csv('')

# train 
train = pd.read_csv("C:/Users/1375744/Desktop/streamlit/data/train.csv")

# test
test = pd.read_csv("C:/Users/1375744/Desktop/streamlit/data/test.csv")

# create copies of the dataframes

imdb_df = imdb_df.copy()
movies_df = movies_df.copy()
train_df = train.copy()
test_df = test.copy()

# merging dataframe
train_df = pd.merge(movies_df, imdb_df, on = 'movieId')
# Percentage of missing values
#(train_df.isnull().sum()/len(train_df))*100

# change data types
train_df['genres'] = train_df.genres.astype(str)
train_df['title_cast'] = train_df.title_cast.astype(str)
train_df['director'] = train_df.director.astype(str)
train_df['plot_keywords'] = train_df.plot_keywords.astype(str)



# Every genre is separated by a | 
train_df['genres'] = train_df['genres'].map(lambda x: x.lower().split('|'))

# Every title cast is separated by a | so we simply have to call the split function on | and separate them by ,
train_df['title_cast'] = train_df['title_cast'].str.split('|')

# And we will do the same thing for the plot keywords
train_df['plot_keywords'] = train_df['plot_keywords'].str.split('|')

def string_function(x):
    """combines name and surname into one name
    and return results as one name.
    
    if no name exists returns a space"""
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''
cols = ['title_cast','director']

for col in cols:
    train_df[col] = train_df[col].apply(string_function)      

st.write("#")
with Exploratory_Data_Analysis:
    st.write("## Exploratory Data Analysis")



#extracting released year
movies = movies_df.copy()
movies['release_year']=movies['title'].str[-5:-1] 
#spliting the genres into a list
movies['genres']=movies['genres'].str.split('|') 
#concatinate ratings with movies dataframe
movies.dropna() 

#spliting the title cast into a list
imdb = imdb_df.copy()
imdb['title_cast']=imdb['title_cast'].str.split('|') 

train_eda = train_df.copy()
con = pd.concat([train_df[:1000],movies], axis=1)

df= pd.concat([imdb,con], axis=1)
df.dropna(inplace=True)

# Merging the tarin  and movies data
data = pd.merge(train, movies, on='movieId')

#creating mean ratings data
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())


#creating number of ratings data
ratings['number_of_ratings'] = data.groupby('title')['rating'].count()

st.image("https://github.com/kwanda2426/unsupervised-predict-streamlit-template/blob/3368384354d1e121cda41fd38ee9636fd0dfd5e8/Capture.JPG")

