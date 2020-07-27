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
from PIL import Image,ImageFilter,ImageEnhance
import os


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
rating = 'resources/data/ratings.csv'
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","Recommender System","View EDA",
                    "Solution Overview", "Meet The Rollicks"]

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
                        top_recommendations = collab_model(movie_list=fav_movies,
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
                        top_recommendations = content_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------

    st.sidebar.info('Click dropdown above to begin :popcorn:')
    if page_selection == "Solution Overview":
        html_temp = """
        <h1 style="font-size: 30px;margin-bottom: 10px;text-align: center;">Solution Overview</h1>
        <div style="background-color:;padding:10px">
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)

        st.markdown("""
            ### Why a moive recommendation engine?
            + Users often struggle to find suitable movies due to the increasing amount of movie variation. As a result, recommender systems are useful for helping customers choose their preferred movies with the existing features. Recommender systems are an essential feature in our digital world, as users are often overwhelmed by choice and need help finding what they're looking for and are amongst the most popular applications of unsupervised learning. This following is an unsupervised machine learning project which seeks to predict the rating that a user will rate for a movie they have not yet viewed based on historical preferences.
            ### Model Evaluation
            + To verify the quality of the recommender system, we adopted the root of mean squared error (RMSE) as our evaluation metric. RSME is used to measure the differences between the model predicted values and the test dataset observed values. Technically it's the square root of the average of the squares of the errors. The lower it is, the better the model will be.
            ### Collaborative Based Filtering: Singular Value Decomposition (SVD)
            + Most collaborative recommender systems perform poorly when dimensions in data increases this is often referred to as the “curse of dimensionality”. There are many dimensionality reduction algorithms such as principal component analysis (PCA) and linear discriminant analysis (LDA), but in this project, SVD algorithm was used. SVD is a well-known matrix factorization method. At a high level, SVD is an algorithm that decomposes a matrix 𝐴A into the best lower rank (i.e. smaller/simpler) approximation of the original matrix 𝐴A. For more information on SVD in recommender systems. Mathematically, it decomposes A into a two unitary matrices and a diagonal matrix.
            """)
        st.image('resources/imgs/collaborative.png',use_column_width=True)
        st.markdown("""
            ### Content Based Filtering
            + Content here refers to the content or attributes of the products or item of interest. So, the idea in content-based filtering is to tag products using certain keywords, understand what the user likes, look up those keywords in the database and recommend different products with the same attributes.
            + However in this notebook what we do is to try and figure if a certain user is going to like a certain movie, and whether or not they like it is gauged on the rating the would give the movie from 0 (dislike the movie) to 5 (highly liking the movie) based on movie meta-data data like cast, director and keywords.
            + So We altermately want to predict rating of a movie based on its contents, basically appraoching this like we would a classification problem. With that in mind the idea we had is to extract all meta-data from the dataset and and merge everything to to data-frames, one containing movieId, megered meta-data and weighted-rating for each movie in the the train dataset and the other movieId and merged meta-data for each movie in the test dataset.
            """)
        st.image('resources/imgs/1_O_GU8xLVlFx8WweIzKNCNw.png',use_column_width=True)
   ##   st.markdown(open('resources/Solution_Overview.md').read())


    
    # Landing Page
    if page_selection == "Welcome":
        st.image('resources/imgs/our_logo.png',use_column_width=True)
        html_temp = """
        <div style="background-color:;padding:10px">
        <h3 style="color:#16284c;text-align:center;">Welcome to Rollick, A Machine-Learning Movie Recommender Engine. Our platform helps you find movies you will like using a recommendation ML model through rated movies to build a custom taste profile, then recommends other movies for you to watch based on preselections.</h3>
        </div>""" 
        st.image('resources/imgs/rollick_mascot.png',use_column_width=True)
        st.markdown(html_temp,unsafe_allow_html=True)


    # Exploratory Data Analysis Page
    if page_selection == "View EDA":
        html_temp = """
        <div style="background-color:;padding:10px">
        <h1 style="font-size: 30px;margin-bottom: 10px;text-align: center;">Exploratory Data Analysis</h1>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)

        st.write("### Training data for the model and visualisations to obtain insights") 
        st.write('')

        @st.cache(persist=True)
        def explore_data(dataset):
            df = pd.read_csv(os.path.join(dataset))
            return df 

        # Load Our Dataset
        data = explore_data(rating)

        # Show Entire Dataframe
        tab = ['Visual Data & Observations', 'View Raw Data']
      ##  selection_info = st.selectbox("Select page", tab)
        selection_info = st.radio(label="Select Below", options=tab)
        
        if selection_info == "Visual Data & Observations":
            if st.checkbox("User Ratings"):
                st.markdown("""
            ### Observations
            + Movie that was rated the most by users is "Great Performances" Cats (1998) with the rating of 2.0, this can also tells us that the movie is being watched by most of the users as they have given it a rating.
            + Having that in mind we can draw some insights that the movie is most prefered compared to #Female Pleasure (2018) which is rated 4.0 by only a single user.
            + Some movies are rated high but only by a single user.
            + The joint plot shows that one user may give a high single rating for that movie by looking at number of rating.
            """)
                st.image('resources/imgs/Webp.net-resizeimage.png',use_column_width=False)

                st.image('resources/imgs/Webp.net-resizeimage (2).png',use_column_width=False)

            elif st.checkbox("Ratings Per Genre"):
                st.markdown("""
            ### Observations
            + The top 3 most popular movie genres in terms of ratings are Drama, Comedy and Action respectively, with documentary being the least popular genre.
            + We can also tell that on our genre dataset some movie genres were not recorded,of which it maybe due to while rating the user forgot to pick the genre of that movie.
            """)       
                st.image('resources/imgs/genre.png',use_column_width=True)

                st.markdown("""
            ### Observations
            + The top 3 genre are Drama ,Comedy and Thriller when looking at keyword occurance.Which tell us that these are the most prefered genres as those words still include the most rated genre.
            + Word like Romance and Action still looked to be bold or emphasised which shows that these genres are still amoungst the top viewed genres taking into account some movie genres are not liststed.Which shows that users still prefer to watch such movies.
            + The least viewed genre is Western and War ,which is displayed by the size of each word.
            """)
                st.image('resources/imgs/erwwsf.png',use_column_width=True)

            elif st.checkbox("Movie Release Distribution"):
                st.markdown("""
            ### Observations
            + Although the train dataset does not represent the entire ccollection of movies released since the making of movies, it gives an indication of how the movies were released.
            + The gradual increase in movie releases from the early 1900s onwards with a sharp rise from early 2000s.
            """)       
                st.image('resources/imgs/Movie Release.png',use_column_width=True)

        if selection_info == "View Raw Data":
            st.markdown("""
            ### Train Data Set
            Below is the dataset we used to train our model in a csv file format.

            """)
            st.dataframe(data)

    

# The team page.
    if page_selection == "Meet The Rollicks":
        html_temp = """
			"""
        st.sidebar.markdown(html_temp)
        cl = """
				<div style="margin-top: 50px;">
					<h1 style="font-size: 30px;margin-bottom: 60px;text-align: center;">Meet The Rollicks</h1>
					<div style="  display:flex;justify-content: center;width: auto;text-align: center;flex-wrap: wrap;">
						<div style="background: #f0f2f6;border-radius: 5%;margin: 5px;margin-bottom: 50px;width: 300px;padding: 20px;line-height: 20px;color: #8e8b8b;position: relative;">
						<div style="position: absolute;top: -50px;left: 50%;transform: translateX(-50%);width: 100px;height: 100px;border-radius: 50%;background: #acaeb0;">
							<img src="https://ca.slack-edge.com/TSHE6M7T9-USM78CA85-16e0da239ced-512" alt="Team_image" style="width: 100px;height: 100px;padding: 5px;border-radius: 50%">
						</div>
						<h3 style="color: black;font-family: "Comic Sans MS", cursive, sans-serif;font-size: 26px;margin-top: 50px;">Ritshidze Nethenzheni</h3>
						<p style="color: #6770c2;margin: 12px 0;font-size: 17px;text-transform: uppercase;">Data Scientist/Project Lead</p>
						<div style="justify-content: center;margin-left: auto;margin-right: auto;">
						<ul>
  							<li style="display:inline;">
								<a href="#"><img border="0" alt="Twitter" src="https://image.flaticon.com/icons/svg/1384/1384017.svg" width="25" height="25"></a>  
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
							</li>
						</ul>
						</div>
						</div>
											<div style="background: #f0f2f6;border-radius: 5%;margin: 5px;margin-bottom: 50px;width: 300px;padding: 20px;line-height: 20px;color: #8e8b8b;position: sticky;">
						<div style="position: absolute;top: -50px;left: 50%;transform: translateX(-50%);width: 100px;height: 100px;border-radius: 50%;background: #acaeb0;">
							<img src="https://media-exp1.licdn.com/dms/image/C4D03AQGMOiDJlhjN-A/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=iWkS-BElbv8USxyWkGveRTZFJzRdWGpH1pgwUSNetvI" alt="Team_image" style="width: 100px;height: 100px;padding: 5px;border-radius: 50%">
						</div>
						<h3 style="color: black;font-family: "Comic Sans MS", cursive, sans-serif;font-size: 26px;margin-top: 50px;">Mandla Solomon</h3>
						<p style="color: #6770c2;margin: 12px 0;font-size: 17px;text-transform: uppercase;">ML Engineer</p>
						<div style="justify-content: center;margin-left: auto;margin-right: auto;">
						<ul>
  							<li style="display:inline;">
								<a href="#"><img border="0" alt="Twitter" src="https://image.flaticon.com/icons/svg/1384/1384017.svg" width="25" height="25"></a>  
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
							</li>
						</ul>
						</div>
						</div>
												<div style="background: #f0f2f6;border-radius: 5%;margin: 5px;margin-bottom: 50px;width: 300px;padding: 20px;line-height: 20px;color: #8e8b8b;position: relative;">
						<div style="position: absolute;top: -50px;left: 50%;transform: translateX(-50%);width: 100px;height: 100px;border-radius: 50%;background: #acaeb0;">
							<img src="https://media-exp1.licdn.com/dms/image/C5603AQEEzz8gjEkK1w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=k9xAqxxsU9qQ2JUHZB6TH6HdK9duyUgi7FCWX6CfYUc" alt="Team_image" style="width: 100px;height: 100px;padding: 5px;border-radius: 50%">
						</div>
						<h3 style="color: black;font-family: "Comic Sans MS", cursive, sans-serif;font-size: 26px;margin-top: 50px;">Bongani Msimanaga</h3>
						<p style="color: #6770c2;margin: 12px 0;font-size: 17px;text-transform: uppercase;">Data Engineer</p>
						<div style="justify-content: center;position: relative;">
						<ul>
  							<li style="display:inline;">
								<a href="#"><img border="0" alt="Twitter" src="https://image.flaticon.com/icons/svg/1384/1384017.svg" width="25" height="25"></a>  
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
							</li>
						</ul>
						</div>
						</div>
												<div style="background: #f0f2f6;border-radius: 5%;margin: 5px;margin-bottom: 50px;width: 300px;padding: 20px;line-height: 20px;color: #8e8b8b;position: relative;">
						<div style="position: absolute;top: -50px;left: 50%;transform: translateX(-50%);width: 100px;height: 100px;border-radius: 50%;background: #acaeb0;">
							<img src="https://media-exp1.licdn.com/dms/image/C4E03AQGLQHxMNcVgLQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=sIG5IeSFmZgFcI2KLlBFjrSQn62Zsb4i_YBcKu_0fbY" alt="Team_image" style="width: 100px;height: 100px;padding: 5px;border-radius: 50%">
						</div>
						<h3 style="color: black;font-family: "Comic Sans MS", cursive, sans-serif;font-size: 26px;margin-top: 50px;">Chris Mahlangu</h3>
						<p style="color: #6770c2;margin: 12px 0;font-size: 17px;text-transform: uppercase;">Data Scientist</p>
						<div style="justify-content: center;position: relative;">
						<ul>
  							<li style="display:inline;">
								<a href="#"><img border="0" alt="Twitter" src="https://image.flaticon.com/icons/svg/1384/1384017.svg" width="25" height="25"></a>  
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
							</li>
						</ul>
						</div>
						</div>
												<div style="background: #f0f2f6;border-radius: 5%;margin: 5px;margin-bottom: 50px;width: 300px;padding: 20px;line-height: 20px;color: #8e8b8b;position: relative;">
						<div style="position: absolute;top: -50px;left: 50%;transform: translateX(-50%);width: 100px;height: 100px;border-radius: 50%;background: #acaeb0;">
							<img src="https://ca.slack-edge.com/TSHE6M7T9-USB324Y81-fbaf5dc6b1b0-512" alt="Team_image" style="width: 100px;height: 100px;padding: 5px;border-radius: 50%">
						</div>
						<h3 style="color: black;font-family: "Comic Sans MS", cursive, sans-serif;font-size: 26px;margin-top: 50px;">Evans Marema</h3>
						<p style="color: #6770c2;margin: 12px 0;font-size: 17px;text-transform: uppercase;">Data Scientist</p>
						<div style="justify-content: center;position: relative;">
						<ul>
  							<li style="display:inline;">
								<a href="#"><img border="0" alt="Twitter" src="https://image.flaticon.com/icons/svg/1384/1384017.svg" width="25" height="25"></a>  
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
							</li>
  							<li style="display:inline;">
							  	<a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
							</li>
						</ul>
						</div>
						</div>
					</div>
				</div>
			"""
        st.markdown(cl, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
