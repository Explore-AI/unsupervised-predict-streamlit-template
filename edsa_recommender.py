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
    
    page_options = ["Home","Recommender System","Solution Overview", 'About us', "FAQ"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    st.sidebar.image('resources/imgs/4.png',use_column_width=False)
    st.sidebar.subheader("Movie Recommender Engine 💡")
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        c1, c2 = st.columns([1, 2])
        with c1:

            st.image(
                "resources/imgs/logo.png",
                width=250,)
        with c2:
            st.title("Movie Recommender Engine 💡")
        # We need to set up session state via st.session_state so that app interactions don't reset the app.
        if not "valid_inputs_received" in st.session_state:
            st.session_state["valid_inputs_received"] = False
        st.write('# ')
        st.write("### let's Get You started! Get Your Recommendations Below")
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
        st.title("Solution Overview")
        st.write("We the FSC_TECH company data science company offers solutions that leverage data analytics, machine learning,")
        st.write(" and artificial intelligence to solve complex problems, also recommend and provide valuable insights to clients. ")
        st.write("Here's a detailed overview of the various components and processes involved in the operations of FSC_TECH company:")
        st.write("A: Problem Identification and Consultation")
        st.write("B: Data Acquisition and Integration")
        st.write("C: Exploratory Data Analysis (EDA)")
        st.write("D: Feature Engineering")
        st.write("E: Model Development")
        st.write("F: Model Evaluation and Validation")
        st.write("G: Deployment and Integration")
        st.write("H: Continuous Monitoring and Maintenance")
        st.write("I: Reporting and Visualization")
        st.write("J: Ongoing Support and Collaboration")

    if page_selection == "Home":
        st.image('resources/imgs/logo.png',use_column_width=True)
        st.title("Home")
        st.write("FSC_TECH company are into building recommendation system for companies and also offers the best services for our clients.")
        
#         with st.expander("Click here to view the raw data"):
#             st.dataframe(filtered_df)
        
        
    # Building out the About Us page
    if page_selection == "About us":
        st.info("FSC_TECH company")
        st.write("FSC_TECH company provides data and analytics solutions that enable clients to gain valuable insights from their data, make informed decisions in a timely manner, and consistently stay ahead of the competition.")

        st.info("Our Vision:")
        st.write("To be the lead Tech Solution Plug")

        st.info("Meet the team")
        image_width = 150
        column_11, column_12 = st.columns([2, 2])
        with column_11:
            st.markdown("Fumani Thibela")
            st.image(
                "resources/imgs/Fumani.jpeg", width=image_width
            )
        with column_12:
            st.markdown("Confidence")
            st.image("resources/imgs/Confidence.jpeg", width=image_width)

        column_11, column_12 = st.columns([2, 2])
        with column_11:
            st.markdown("Stephen")
            st.image("resources/imgs/Stephen.jpeg", width=image_width)
        with column_12:
            st.markdown("Joshua")
        st.image("resources/imgs/Joshua.jpeg", width=image_width)
#         Fumani = st.image('resources/imgs/Fumani.JPEG')
#         Fumani1 = Fumani.size((50, 55))
#         Confidence = st.image('resources/imgs/Confidence.JPEG')
#         Confidence1 = Confidence.resize((50, 55))
#         Joshua = st.image('resources/imgs/Joshua.JPEG')
#         Joshua1 = Joshua.resize((50, 55))
#         Stephen = st.image('resources/imgs/Stephen.JPEG')
#         Stephen1 = Stephen.resize((50, 55))
#         #Collete = Image.open('resources/imgs/Collete.PNG')
#         C#ollete1 = Collete.resize((150, 155))

#         col1, col2, col3, col4 = st.columns(4)
#         with col2:
#             st.image(Fumani1, width=50, caption="Fumani: Team Lead")
#         with col3:
#             st.image(Confidence1, width=50, caption="Confidence: Technical Lead")

#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.image(Stephen1, width=50, caption="Stephen: Project Manager")
#         with col2:
#             st.image(Joshua1, width=50, caption="Joshua: Data Scientist")

        #with col3:
           # st.image(Collete1, width=150, caption="Collete: Data Scientist")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    # Building out the FAQ page
    if page_selection == "FAQ":
        c1, c2 = st.columns([1, 2])
        with c1:

            st.image(
                "resources/imgs/logo.png",
                width=250,)
        with c2:
            st.title("Frequently Asked Questions")
        #st.title("")
        st.write("")

if __name__ == '__main__':
    main()
