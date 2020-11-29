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

path_to_s3 = ('../unsupervised_data/')

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
    page_options = ["Introduction", "Exploratory Data Analysis", "Recommender System", "Solution Overview"]

###########################################################################################
################################ MODEL ####################################################
###########################################################################################

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Select Page", page_options)
    if page_selection == "Recommender System":
        title_list = dl.load_movie_titles('../unsupervised_data/unsupervised_movie_data/movies.csv')
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        # movie_list = pd.merge(train_df, title_list, on = 'movieId', how ='left').groupby('title')['ratings'].mean()
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

###########################################################################################
################################ Solution Overview ########################################
###########################################################################################

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.markdown(open('resources/markdown/solution.md').read(), unsafe_allow_html=True)
        st.image('resources/imgs/models.png')

###########################################################################################
################################ EDA ######################################################
###########################################################################################

    # ------------- EDA -------------------------------------------
    if page_selection == "Exploratory Data Analysis":
        #st.sidebar.markdown(open('resources/markdown/eda/eda_info.md').read(), unsafe_allow_html=True)

        page_options_eda = ["User Interactions", "Movies", "Genres", "Directors"]
        page_selection_eda = st.selectbox("Select Feature", page_options_eda)
        if page_selection_eda == "User Interactions":
            st.sidebar.markdown(open('resources/markdown/eda/userint.md').read(), unsafe_allow_html=True)

        # Most Active
            st.subheader("Most Active Users")
            train_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/train.csv', index=None)
            top_user = st.checkbox('Include top user',value=False)

            ## include top user
            if top_user == True:
                ratings = train_df
            else:
                ratings = train_df[train_df['userId']!=72315]

            ## choose top k
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
            eda.mean_ratings_scatter(ratings, color ='#4D17A0')
            plt.title('Mean user ratings by number of ratings given')
            plt.tight_layout()
            st.pyplot()
            st.write('It doesnot seem to be a relationship. As the number of ratings and how a user rates a movie do not show any correlation.')

            st.write('Q: Is there a relationship between the number of ratings a movie has and how highly it is rated?')
            eda.mean_ratings_scatter(ratings, column ='movieId')
            plt.title('Mean movie rating by number of ratings received')
            plt.tight_layout()
            st.pyplot()
            st.write('This time we do see a relationship, The more ratings a movie has, the more highly it is likely to be rated. This confirms our intuitive understanding that the more highly recommended a movie is, the more likely it is to be well received by the user.')

        if page_selection_eda == "Movies":
            st.sidebar.markdown(open('resources/markdown/eda/movies.md').read(), unsafe_allow_html=True)
            counts = st.number_input('Choose min ratings', min_value=0, max_value=15000, value = 10000, step=1000)
            ns= st.number_input('Choose n movies', min_value=5, max_value=20, value=10,step=5)
            st.subheader('Best and Worst Movies by Genre')
            eda.plot_ratings(count=counts, n=ns, color='#4D17A0', best=True, method='mean')
            #plt.tight_layout()
            st.pyplot()
            st.write('By filtering movies with less than 10000 ratings, we find that the most popular movies are unsurprising titles. The Shawshank Redemption and The Godfather unsurprisingly top the list. What is interesting is that Movies made post 2000 do not feature often. Do users have a preference to Older movies?')

            eda.plot_ratings(count=counts, n=ns, color='#4DA017', best=False, method='mean')
            #plt.tight_layout()
            st.pyplot()
            st.write('Obviously, users did not like Battlefield too much and with 1200 ratings, they really wanted it to be known. It is interesting how many sequels appear in the list')


        if page_selection_eda == "Directors":
            st.sidebar.markdown(open('resources/markdown/eda/directors.md').read(), unsafe_allow_html=True)
            imdb_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/imdb_data.csv', index=None)
            #st.write('Some movies do not have a director listed. once again, the IMDB API can be used to retrieve this data')
            directors=eda.count_directors(imdb_df)

            #county = st.number_input('Choose min directors', min_value=0, max_value=15000, value = 10000, step=1000)
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
            st.write('Akira Toriyama is the Manga artist behind the Dragon Ball franchise. Dragonball is important to Anime communities because it popularized anime in the west. However, despite its loyal fan base, it remains far from being the best anime.')


        # if page_selection_eda == "Cast":
        #     st.write('best and worst cast, word clouds')

        # if page_selection_eda == "Plot Keywords":
        #     st.write('best and worst plots, word clouds')

        if page_selection_eda == "Genres":
            st.sidebar.markdown(open('resources/markdown/eda/genres.md').read(), unsafe_allow_html=True)
            st.subheader('Genre Distribution')
            movies_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/movies.csv', index=None)
            genres= eda.feature_frequency(movies_df, 'genres')
            #st.write('write something here')

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

###########################################################################################
################################ Introduction #############################################
###########################################################################################

    if page_selection == "Introduction":
        st.sidebar.markdown(open('resources/markdown/introduction/contrib.md').read(), unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Team RM4 TheFlixters</h1>", unsafe_allow_html=True)
        st.image('resources/imgs/banner.png',use_column_width=True)
        #st.sidebar.markdown(open('resources/markdown/introduction/info.md').read(), unsafe_allow_html=True)
        info_pages = ["Select Option", "General Information", "Contributors"]
        info_page_selection = st.selectbox("", info_pages)

        if info_page_selection == "Select Option":
            st.info("Welcome! Select an option from the menu above to get started.")

        if info_page_selection == "General Information":
            st.info("Read more about the project and the data that was used to solve the problem at hand.")
            #st.sidebar.markdown(open('resources/markdown/introduction/general_information/gen_conts.md').read(), unsafe_allow_html=True)
            st.markdown(open('resources/markdown/introduction/general_information/intro.md').read(), unsafe_allow_html=True)

            definitions = st.checkbox("Show definitions")
            see_raw = st.checkbox("Show data")

            if definitions:
                st.write(open('resources/markdown/introduction/general_information/data_def.md', encoding='utf8').read(), unsafe_allow_html=True)
            if see_raw:
                st.write(dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/train.csv', index='userId').head(10))
                st.write(dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/movies.csv',index='movieId').head(10))

        if info_page_selection == "Contributors":
            st.info("Meet the amazing team members that contributed to this project.")
            # st.markdown("<h1 style='text-align: center;'>Contributors</h1>", unsafe_allow_html=True)
            # st.markdown("\n\n")

            ### IN ALPHABETICAL ORDER ###
            # Bulelani
            st.markdown("<h3 style='text-align: center;'>Bulelani Nkosi</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Streamlit App Coordinator | Data Analyst</p>", unsafe_allow_html=True)
            st.image('resources/imgs/Bulelani.jpg', width=120)
            st.markdown("<a href='https://www.linkedin.com/in/bulelanin' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/BNkosi' target='_blank'>GitHub</a>", unsafe_allow_html=True)

            # Lizette
            st.markdown("<h3 style='text-align: center;'>Lizette Loubser</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Notebook Coordinator | ML Engineer</p>", unsafe_allow_html=True)
            st.image('resources/imgs/Lizette.jpg', width=120)
            st.markdown("<a href='http://www.linkedin.com/in/lizette-loubser' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/Lizette95' target='_blank'>GitHub</a>", unsafe_allow_html=True)

            # Neli
            st.markdown("<h3 style='text-align: center;'>Nelisiwe Mabanga</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Data Journalist | Analyst</p>", unsafe_allow_html=True)
            st.image('resources/imgs/nelly.jpeg', width=120)
            st.markdown("<a href='https://www.linkedin.com/in/nelisiwe-mabanga-8bb409106/' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/Phiwe-Mabanga' target='_blank'>GitHub</a>", unsafe_allow_html=True)

            # Nolu
            st.markdown("<h3 style='text-align: center;'>Noluthando Khumalo</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Streamlit App Designer</p>", unsafe_allow_html=True)
            st.image('resources/imgs/Thando.jpg', width=120)
            st.markdown("<a href='https://www.linkedin.com/in/noluthando-khumalo-3870ab191/' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/ThandoKhumalo' target='_blank'>GitHub</a>", unsafe_allow_html=True)

            # Nompilo
            st.markdown("<h3 style='text-align: center;'>Nompilo Nhlabathi</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Streamlit App Designer</p>", unsafe_allow_html=True)
            st.image('resources/imgs/Nompilo.png', width=120)
            st.markdown("<a href='http://www.linkedin.com/in/nompilo-nhlabathi-2701791b2' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/mapilos' target='_blank'>GitHub</a>", unsafe_allow_html=True)

            # Sizwe
            st.markdown("<h3 style='text-align: center;'>Sizwe Bhembe</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Notebook Assistant</p>", unsafe_allow_html=True)
            st.image('resources/imgs/Sizwe.jpg', width=120)
            st.markdown("<a href='https://www.linkedin.com/in/sizwe-bhembe-372880101' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
            st.markdown("<a href='https://github.com/sjbhembe' target='_blank'>GitHub</a>", unsafe_allow_html=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

if __name__ == '__main__':
    main()
