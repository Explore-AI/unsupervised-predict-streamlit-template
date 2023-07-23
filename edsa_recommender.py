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

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies_df = pd.read_csv('resources/data/rated_movies.csv')
# App declaration

def extract_year_from_title(title):
    year_start = title.find("(") + 1
    year_end = title.find(")")
    return title[year_start:year_end]


# Extract year from the title and create a new "year" column
movies_df['year'] = movies_df['title'].apply(extract_year_from_title)

# Convert the "year" column to integer type
movies_df['year'] = pd.to_numeric(movies_df['year'], errors='coerce')

def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","Movie Search","Top Rated Movies","EDA", "About Us"]

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
    # Code for "Movie Search" page
    if page_selection == "Movie Search":
        st.title("Movie Search")

        # Sidebar - Movie Search
        genre = st.sidebar.text_input('Enter a Genre (e.g., Action, Drama, Comedy):')
        title = st.sidebar.text_input('Enter a Movie Title:')
            # Function to filter movies based on user criteria
        def filter_movies(df, genre=None, title=None):
            if genre:
                df = df[df['genres'].str.contains(genre, case=False)]
            if title:
                df = df[df['title'].str.contains(title, case=False)]
            df = df.sort_values(by='rating', ascending=False)
            return df

            # Filter the movies based on user criteria
        filtered_movies = filter_movies(movies_df, genre=genre, title=title)

            # Display the filtered movie results
        st.table(filtered_movies[['title', 'genres', 'rating']])


        # -------------------------------------------------------------------

        # Code for "Top Rated Movies" page
    if page_selection == "Top Rated Movies":
        st.title('Top Rated Movies')
        num_top_rated_movies = st.slider('Number of Top Rated Movies to Display:', 5, 20, 10)

            # Function to get top-rated movies
        def get_top_rated_movies(df, num_movies=10):
            return df.nlargest(num_movies, 'rating')

        top_rated_movies = get_top_rated_movies(movies_df, num_top_rated_movies)
        st.table(top_rated_movies[['title', 'genres', 'rating']])



    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.image('resources/imgs/header_image.jpg',use_column_width=True)
        
        # Button to expand/collapse the "Movie Recommender App" subsection
        if st.button("Movie Recommender App"):
            st.write("""
        **Solution Overview: Movie Recommender App**

        Our Movie Recommender App is an intelligent system designed to help users discover their ideal movies by leveraging the power of collaborative-based and content-based filtering techniques. The primary goal of this app is to provide personalized movie recommendations based on user preferences and movie features.
        """)

        if st.button("Key Features"):
            st.write("""
        **Key Features:**

        1. **User-Friendly Interface:** The app offers a simple and intuitive user interface. Users can easily navigate through different sections, including "Recommender System," "Movie Search," and "Top Rated Movies."

        2. **Recommender System:** Our app presents two advanced recommendation algorithms: Collaborative-Based Filtering and Content-Based Filtering. Users can input their three favorite movies, and the system will generate a list of movie recommendations tailored to their unique tastes.

        3. **Movie Search:** Users have the freedom to search for specific movies or explore movies by genres. The app efficiently filters movies based on user-provided genre criteria, allowing users to quickly discover movies that match their interests.

        4. **Top Rated Movies:** Our app presents a list of top-rated movies based on user ratings or other metrics. Users can adjust the number of movies displayed to explore the best movies based on their preferences.
        """)

        if st.button("How It Works"):
            st.write("""
        **How It Works:**

        1. **Collaborative-Based Filtering:** This approach builds user-item interactions to uncover patterns in user preferences. By analyzing how similar users have rated movies, the system identifies movies that align with a user's taste. The resulting recommendations are personalized and considerate of user behavior.

        2. **Content-Based Filtering:** The content-based approach focuses on movie features such as genres and tags. By comparing movie attributes with user preferences, the app suggests movies that align with a user's previous movie choices.
        """)
    
        if st.button("Benefits"):
            st.write("""
        **Benefits:**

    1. **Personalized Recommendations:** Our app provides personalized movie recommendations, ensuring that users receive tailored suggestions based on their individual interests.

    2. **Exploration and Discovery:** Users can discover new movies outside their typical choices through the diverse recommendations generated by the app.

    3. **Enhanced Movie Search:** The movie search feature enables users to find movies based on specific genres, empowering them to explore movies relevant to their mood or interests.

        """)
                     
        st.write("""Our Movie Recommender App is committed to delivering an engaging and dynamic movie discovery experience for users. We continuously strive to improve our recommendation algorithms and user interface to ensure movie enthusiasts find their perfect watchlist with ease. Enjoy exploring the world of cinema with our smart and sophisticated movie recommender system!
    """) 
    
    

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

#--------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
    

    # Add code for "About Us" page
    if page_selection == "About Us":
        st.title("About Us")

        # Insert information about your team, project, or organization
        
        st.image('resources/imgs/meet_our_team.jpg',use_column_width=True)
        st.markdown("""
        - Ayodele Marcus: Movie Analyst
        - Toka Ramakau: Data Engineer
        - Mmatlou Matlakala: Lead Data Scientist
        - Jacinta Muindi: Machine Learning Engineer
        - Oladimeji Akanni: Data Scientist
        - Emmanuel Alabi: App Designer

        Contact us at [teames2_dreamteam@gmail.com](mailto:teames2_dreamteam@gmail.com) for inquiries.
        """)


#--------------------------------------------------------------------------------------------------
    elif page_selection == "EDA":
        st.title("Exploratory Data Analysis (EDA)")

        # Display summary statistics or any other EDA you want to show
        #st.subheader("Summary Statistics")
        #st.write(movies_df.describe())

        st.subheader("Interactive Movie Filter")

        # Sidebar - Interactive Filters
        st.sidebar.title("Filter Options")

        # Filter by Genre
        genre_filter = st.sidebar.multiselect("Filter by Genre", movies_df['genres'].unique())

        # Filter by Rating
        min_rating, max_rating = st.sidebar.slider("Filter by Rating", min_value=0.0, max_value=5.0, value=(0.0, 5.0))

        # Filter by Release Year
        #min_year, max_year = st.sidebar.slider("Filter by Release Year", min_value=int(movies_df['year'].min()), max_value=int(movies_df['year'].max()), value=(int(movies_df['year'].min()), int(movies_df['year'].max())))
        # Get the range of the release years
        min_year, max_year = int(movies_df['year'].min()), int(movies_df['year'].max())

        # Filter by Release Year
        min_year, max_year = st.sidebar.slider("Filter by Release Year", min_value=min_year, max_value=max_year, value=(min_year, max_year))
        
        # Apply filters to the DataFrame
        filtered_movies = movies_df[
            (movies_df['genres'].isin(genre_filter)) &
            (movies_df['rating'] >= min_rating) & (movies_df['rating'] <= max_rating) &
            (movies_df['year'] >= min_year) & (movies_df['year'] <= max_year)
        ]

        # Display the filtered movie results
        st.dataframe(filtered_movies)

        st.image('resources/imgs/EDA1.jpg',width=600)
        st.image('resources/imgs/EDA2.jpg',width=600)

        # You can add other EDA visualizations and analysis here

    # -------------------------------------------------------------------





if __name__ == '__main__':
    main()
