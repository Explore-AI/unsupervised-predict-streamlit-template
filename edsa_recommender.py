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
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(
                "resources/imgs/4.png",
                width=150,)
            
            
        with c2:
            st.title(
                "FSC_TECH company")

        st.subheader("Our Vision:")
        st.write("Our vision is to leverage cutting-edge AI and recommender algorithms to empower users with data-driven, personalized recommendations, enabling them to make informed choices effortlessly")
        image_width = 200

        st.subheader("About our company")
        st.markdown(
            "We are FSC_TECH company, a leading data science company dedicated to helping businesses unlock the power of data to drive growth, innovation, and success. With our expertise in advanced analytics, machine learning, and artificial intelligence, we provide actionable insights and data-driven solutions that empower organizations to make informed decisionsin a timely manner, improve on customer satsfaction and achieve their goals by consistently being ahead of the competition."
        )
        st.header("")
        st.subheader("Our Expertise")
        st.markdown(
            """With a team of highly skilled data scientists, machine learning engineers, and domain experts, we have the knowledge and experience to tackle complex data challenges across various industries. From predictive modeling and data visualization to natural language processing and recommendation systems, we specialize in a wide range of data science techniques and technologies."""
        )
        st.header("")
        st.subheader("The Team")

        column_11, column_12 = st.columns([2, 2])
        with column_11:
            st.markdown("Fumani Thibela")
            st.image("resources/imgs/Fumani.jpeg", width=image_width)
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
