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

# Data Visulization
import matplotlib.pyplot as plt

# Custom Libraries
from utils import data_loader as dl
from eda import eda_functions as eda
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
st.set_option('deprecation.showPyplotGlobalUse', False)
import warnings
warnings.simplefilter(action='ignore')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://e1.pxfuel.com/desktop-wallpaper/216/147/desktop-wallpaper-blue-movie-film-strip-backgrounds-for-powerpoint-powerpoint-background-movie-theme.jpg');
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);

}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url('https://e1.pxfuel.com/desktop-wallpaper/216/147/desktop-wallpaper-blue-movie-film-strip-backgrounds-for-powerpoint-powerpoint-background-movie-theme.jpg');
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

path_to_s3 = ('https://media.githubusercontent.com/media/LPTsilo/Team_ES2_Unsupervised_Predict/main/')

# Data Loading


# Loading a css stylesheet
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css("resources/css/style.css")

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = [ "Recommender System", "Introduction", "Exploratory Data Analysis", "Solution Overview"]

################################################################################
################################ MODEL #########################################
################################################################################

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Select Page", page_options)
    if page_selection == "Recommender System":
        title_list = dl.load_movie_titles('https://media.githubusercontent.com/media/LPTsilo/Team_ES2_Unsupervised_Predict/main/movies.csv')
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        # movie_list = pd.merge(df_train, title_list, on = 'movieId', how ='left').groupby('title')['ratings'].mean()
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

################################################################################
################################ Solution Overview #############################
################################################################################

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.markdown(open('resources/markdown/solution.md').read(), unsafe_allow_html=True)
        st.image('resources/imgs/models.png')

################################################################################
################################ EDA ###########################################
################################################################################

    # ------------- EDA -------------------------------------------
    if page_selection == "Exploratory Data Analysis":
        page_options_eda = ["User Interactions", "Movies", "Genres", "Directors"]
        page_selection_eda = st.selectbox("Select Feature", page_options_eda)
        if page_selection_eda == "User Interactions":
            st.sidebar.markdown(open('resources/markdown/eda/userint.md').read(), unsafe_allow_html=True)

        # Most Active
            st.subheader("Most Active Users")
            df_train = dl.load_dataframe('https://media.githubusercontent.com/media/LPTsilo/Team_ES2_Unsupervised_Predict/main/train.csv', index=None)
            top_user = st.checkbox('Include top user',value=False)

            ## include top user
            if top_user == True:
                ratings = df_train
            else:
                ratings = df_train[df_train['userId']!=72315]

            ## choose top k(select number of users rated)
            n = st.number_input('Select number of users (1-50)',min_value=5, max_value=50, step = 5, value=10)
            ratings_plot = eda.user_ratings_count(ratings, n)
            if n>=10:
                plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot()

            st.write("User 72315 has rated an extreme number of movies relative to other users. For EDA purposes, this user can be removed above to make interpretation easier.")

        # Ratings Distribution
            st.subheader('Ratings Distribution')
            eda.number_users_per_rating(ratings)
            plt.tight_layout()
            st.pyplot()
            st.write(open('resources/markdown/eda/ratings_dist.md').read(), unsafe_allow_html=True)

        # Rating v number of ratings
            st.subheader('Ratings trends')
            eda.mean_ratings_scatter(ratings, column ='movieId')
            plt.title('Mean movie rating by number of ratings received')
            plt.tight_layout()
            st.pyplot()
            st.write('it seems like The more ratings a movie has, the more highly it is likely to be rated. This confirms our intuitive understanding that the more highly rated a movie is, the more likely is that viewers will recommend the movie to each other. In other words, people generally try to avoid maing bad recommendations')

        if page_selection_eda == "Movies":
            st.sidebar.markdown(open('resources/markdown/eda/movies.md').read(), unsafe_allow_html=True)
            counts = st.number_input('Choose min ratings', min_value=0, max_value=15000, value = 10000, step=1000)
            ns= st.number_input('Choose n movies', min_value=5, max_value=20, value=10,step=5)
            st.subheader('Best and Worst Movies by Genre')
            eda.plot_ratings(count=counts, n=ns, color='#4D17A0', best=True, method='mean')
            st.pyplot()
            st.write('By filtering movies with less than 10000 ratings, we find that the most popular movies are unsurprising titles. The Shawshank Redemption and The Godfather unsurprisingly top the list. What is interesting is that Movies made post 2000 do not feature often. Do users have a preference to Older movies?')

            eda.plot_ratings(count=counts, n=ns, color='#4DA017', best=False, method='mean')
            #plt.tight_layout()
            st.pyplot()
            st.write('Obviously, users did not like Battlefield too much and with 1200 ratings, they really wanted it to be known. It is interesting how many sequels appear in the list')


        if page_selection_eda == "Directors":
            st.sidebar.markdown(open('resources/markdown/eda/directors.md').read(), unsafe_allow_html=True)
            imdb_df = dl.load_dataframe('resources/data/imdb_data.csv', index=None)

            directors=eda.count_directors(imdb_df)

            nt= st.number_input('Choose n directors', min_value=5, max_value=20, value=10,step=5)
            st.subheader('Most Common Directors')
            eda.feature_count(directors.head(nt), 'director')
            plt.title('Number of movies per director')
            plt.tight_layout()
            st.pyplot()
            st.write('Once again we need to calculate a mean rating for each director in order to determine who is the most popular')

            directors = eda.dir_mean(directors)

            st.subheader('Most popular directors')
            eda.feat_popularity(directors.head(nt), 'Director')
            plt.tight_layout()
            st.pyplot()

            st.write('Immediately, we see some very well known names, Stephen King and Quentin Tarantino are unsurprisingly top of the list. It begs the question, who are the worst rated directors?')
            st.subheader('Least popular directors')
            eda.feat_popularity(directors.tail(nt), 'Director')
            plt.tight_layout()
            st.pyplot()
            st.write('It is unfortunate to find Tyler Perry and Akira Toriyama so poorly rated. Tyler Perry is best known for his Madea series of movies. As we saw from the least popular movies, sequels do not perform well and Madea has numerous sequels.')

        if page_selection_eda == "Genres":
            st.sidebar.markdown(open('resources/markdown/eda/genres.md').read(), unsafe_allow_html=True)
            st.subheader('Genre Distribution')
            movies_df = dl.load_dataframe('resources/data/movies.csv', index=None)
            genres= eda.feature_frequency(movies_df, 'genres')

            eda.feature_count(genres.sort_values(by = 'count', ascending=False), 'genres')
            st.pyplot()
            st.write('Drama is the most frequently occuring genre in the database. Approximately 5000 movies have missing genres. We can use the IMDB and TMDB IDs together with the APIs to fill missing data. Further, IMAX is not a genre but rather a proprietary system for mass-viewings.')
            st.write('The above figure does not tell us anything about the popularity of the genres, lets calculate a mean rating and append it to the Data')
            genres['mean_rating']=eda.mean_calc(genres)
            show_data = st.checkbox('Show raw genre data?')
            if show_data:
                st.write(genres.sort_values('mean_rating', ascending=False))
            st.write('Film-Noir describes Hollywood crime dramas, particularly those that emphasize cynical attitudes and sexual motivations. The 1940s and 1950s are generally regarded as the "classic period" of American film-noir. These movies have the highest ratings but this may be as a result of its niche audence. The same logic can be applied to IMAX movies, as such, we will only include genres with a count of 500 or more.')
            eda.genre_popularity(genres.sort_values(by='mean_rating'))
            st.pyplot()
            st.write('The scores are almost evenly distributed with the exceptions of Documentaries, War, Drama, Musicals, and Romance and Thriller, Action, Sci-Fi, and Horror, which rate higher than average and below average respectively.')

################################################################################
################################ Introduction ##################################
################################################################################

    if page_selection == "Introduction":
        st.sidebar.markdown(open('resources/markdown/introduction/contrib.md').read(), unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Team ES2 Data Flex</h1>", unsafe_allow_html=True)
        st.image('resources/imgs/team_logo.jpg',use_column_width=True)
       
        info_pages = ["Select Option", "General Information"]
        info_page_selection = st.selectbox("", info_pages)

        if info_page_selection == "Select Option":
            st.info("Welcome! Select an option from the menu above to get started.")

        if info_page_selection == "General Information":
            st.info("Read more about the project and the data that was used to solve the problem at hand.")
            st.markdown(open('resources/markdown/introduction/general_information/intro.md').read(), unsafe_allow_html=True)

            definitions = st.checkbox("Show definitions")
            see_raw = st.checkbox("Show data")

            if definitions:
                st.write(open('resources/markdown/introduction/general_information/data_def.md', encoding='utf8').read(), unsafe_allow_html=True)
            if see_raw:
                st.write(dl.load_dataframe('resources/data/ratings.csv', index='userId').head(10))
                st.write(dl.load_dataframe('resources/data/movies.csv',index='movieId').head(10))

if __name__ == '__main__':
    main()
