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
    page_options = ["Recommender System","Solution Overview","App Feedback"]

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
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    if page_selection == "App Feedback":
        st.title("App Feedback")
        st.write("We appreciate your valuable feedback on our app! Your insights and suggestions are crucial in helping us improve and provide you with an exceptional user experience. Please take a few moments to share your thoughts by completing this feedback form. Your input will assist us in understanding what aspects of the app are working well and where we can make enhancements or address any issues you may have encountered.")
        
        with st.form("feedback_form"):
            c_feedback = st.container()

            with c_feedback:
                col_feedback_1, col_feedback_2 = st.columns(2)
                with col_feedback_1:
                    feedback_name = st.text_input(
                        "Name",
                        placeholder='Enter',
                    )
                with col_feedback_2:
                    feedback_email = st.text_input(
                        "Email",
                        placeholder='Enter',
                    )
                col_feedback_3, col_feedback_4 = st.columns(2)
                with col_feedback_3:
                    feedback_type = st.selectbox(
                    'Category',
                    ('Defect', 'Bug', 'Feature'))
                with col_feedback_4:
                    feedback_subject = st.text_input(
                        "Subject",
                        placeholder='Enter',
                    )
                col_feedback_5, col_feedback_6 = st.columns(2)
                with col_feedback_5:
                    feedback_description = st.text_area('Description', '''''')
                with col_feedback_6:
                    tab_low, tab_medium, tab_high = st.tabs(["Low", "Medium", "High"])
                    with tab_low:
                        feedback_priority = 0
                    with tab_medium:
                        feedback_priority = 1
                    with tab_high:
                        feedback_priority = 2

                    feedback_satisfaction = st.radio(
                    "Satisfaction",
                    ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'))

                    st.write('Additional Features')
                    feedback_additional_1 = st.checkbox('UI/UX')
                    feedback_additional_2 = st.checkbox('Performance')
                    feedback_additional_3 = st.checkbox('Functionality')
                    feedback_additional_4 = st.checkbox('Other')
            submitted = st.form_submit_button("Submit Feedback")

if __name__ == '__main__':
    main()
