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

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Solution Overview","Our Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Home":
        st.markdown("# Welcome")

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
    if page_selection == "Solution Overview":
        cont="""
         <!-- header of website layout -->
        <div style="background-color: #fffd80;padding: 15px;text-align: center;width: 100%"> 
            <h2 style = "color:black;font-size:200%"> 
                <b>Solution Overview</b> 
            </h2> 
        </div> 
        <!-- nevigation menu of website layout -->
        <div style="overflow: hidden;background-color: #333;width: 100%"> 
            <a href = "#" style="float: left;display: block;color: white;text-align: center;padding: 14px 16px;text-decoration: none;">Home</a> 
            <a href = "#" style="float: left;display: block;color: white;text-align: center;padding: 14px 16px;text-decoration: none;">EDA</a> 
            <a href = "#" style="float: left;display: block;color: white;text-align: center;padding: 14px 16px;text-decoration: none;">Our Team</a> 
        </div> 
        <!-- Content section of website layout -->
        <div class = "row"> 
            <div style="float: left;width: 34%;padding: 15px;text-align:justify;background-color: #f0f2f6;"> 
                <h2 style="color:#f63366;text-align:center;">Column A</h2> 
                <p>Prepare for the Recruitment drive of product 
                based companies like Microsoft, Amazon, Adobe 
                etc with a free online placement preparation 
                course. The course focuses on various MCQ's 
                & Coding question likely to be asked in the 
                interviews & make your upcoming placement 
                season efficient and successful.</p> 
            </div>
            <div style="float: left;width: 33%;padding: 15px;text-align:justify;background-color: #f0f2f6;"> 
                <h2 style="color:#f63366;text-align:center;">Column A</h2> 
                <p>Prepare for the Recruitment drive of product 
                based companies like Microsoft, Amazon, Adobe 
                etc with a free online placement preparation 
                course. The course focuses on various MCQ's 
                & Coding question likely to be asked in the 
                interviews & make your upcoming placement 
                season efficient and successful.</p> 
            </div>
            <div style="float: left;width: 33%;padding: 15px;text-align:justify;background-color: #f0f2f6;"> 
                <h2 style="color:#f63366;text-align:center;">Column A</h2> 
                <p>Prepare for the Recruitment drive of product 
                based companies like Microsoft, Amazon, Adobe 
                etc with a free online placement preparation 
                course. The course focuses on various MCQ's 
                & Coding question likely to be asked in the 
                interviews & make your upcoming placement 
                season efficient and successful.</p> 
            </div>
        </div> 
        """
        st.markdown(cont, unsafe_allow_html=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "Our Team":
        team="""

	<div style="background: #f1f2f6;text-align: center;">
		<div style="max-width: 1500px;margin: auto;padding: 40px;color: #333;overflow: hidden;">
      <h2><b>Meet our Team</b></h2>
      <!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/RNT03793-2%20(2).JPG?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Rohini Jagath</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>Passionate about all things data... but she won't share popcorn at the movies.</p></div>
					<div style="margin-top: 6px;">
						<a href="#" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/pila.jpg?raw=true">
					<div style="margin: 5px;text-transform: uppercase;">Pilasande Pakkies</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>An enthusiast who loves volleyball more than any sport. A pizza lover.</p></div>
					<div style="margin-top: 6px;">
						<a href="http://www.linkedin.com/in/Pilasande-Pakkies" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/20191130_203409.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Tumisang Sentle</div>
					<div style="font-style: italic;color: #3498db;">Web Developer</div>
					<div style=";color: #f63366;"><p>A math addict. He loves listening to debates but he can't debate.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/tumisang-sentle-53100a1a5/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/60532fb212cb493f8fc0c629ef61aa1b.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Refentse Motlogelwa</div>
					<div style="font-style: italic;color: #3498db;">Data Engineer</div>
					<div style=";color: #f63366;"><p>A lover of life with good statistics background. He is also a great DJ.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/ramotse-motlogelwa-8a09358b" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C5603AQEtkA_hyaeciA/profile-displayphoto-shrink_800_800/0?e=1600300800&v=beta&t=i2wG9MJ8LyVMEYkssSfzhKKIoCCmruWTIlt92QEFT9U">
					<div style="margin: 5px;text-transform: uppercase;">Philani Mkhize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>A problem is easier when broken into smaller easier problem.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/philani-mkhize-519995149/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/IMG-2211.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Sandile Mkize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>A former side stepper from the rugby field who turned into a data scientist.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/sandile-mkize-2395b4161/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->

                """
        st.markdown(team, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
