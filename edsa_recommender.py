"""

    Streamlit webserver-based Recommender Engine.

    Author: EDSA2301_JM3_.

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
import streamlit as st
import joblib,os
import csv
from PIL import Image, ImageDraw


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
    page_options = ["Recommender System","Solution Overview","Register Here","Who We Are","Contact Us","Feedback","Privacy and Security"]

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
        
        st.write("Prime Solutions is designed to revolutionize the way you discover and enjoy movies. We understand that choosing the perfect movie can be a daunting task, given the overwhelming number of options available. That's why we have crafted a cutting-edge solution that takes the guesswork out of movie selection and provides you with personalized recommendations that cater to your individual taste")
    
        tab1, tab2, = st.tabs (["Features", "How It Works"])
        with tab1:
            st.markdown("Personalized Movie Recommendations: Discover new movies that align perfectly with your taste, based on your top three movie choices")
    
            
            st.markdown("Extensive Movie Database: Our app has an extensive library of movies, ranging from timeless classics to the latest blockbusters, catering to every genre and taste.")

            st.markdown("User-Friendly Interface: Enjoy a seamless and intuitive user experience, making it effortless to find your ideal movie suggestions.")

            st.markdown("Rate and Review: Share your thoughts and feelings about the movies you've watched and help other users in the community find their next favorite film.")

        with tab2:
                st.markdown(" How To Use The App")
                image1 = Image.open("resources/imgs/Picture2.png")
                st.image(image1)
                
    if page_selection == "Register Here":
        st.title("Register Here")
        with st.form("form1", clear_on_submit= True):
            name= st.text_input("Enter Full Name")
            name= st.text_input("Username")
            name= st.text_input("Enter Email")
            name= st.text_input("Enter Your Password")
            name= st.text_input("Country Of Origin")
            name= st.text_input("Favourite Movie Genre")

            submit= st.form_submit_button("Register")
            
            if submit:
                st.write("Your details have been submitted successfully")
                
    if page_selection == "Who We Are":
        st.title("Who We Are")

        tab1, tab2, tab3,  = st.tabs(["About Us", "Meet The Team", "Contact details"])
        with tab1:
           st.markdown("Prime Solutions is a cutting-edge tech company dedicated to revolutionizing the movie-watching experience through personalized recommendations.")             
           st.markdown("Mission:")
           st.markdown("To empower movie enthusiasts worldwide by providing a seamless and personalized movie recommendation platform. By leveraging cutting-edge technology and an extensive movie database, we aim to simplify the process of discovering new films that resonate with each individual's unique tastes.")
           image2 = Image.open("resources/imgs/logo.jpg")
           st.image(image2)
        with tab2:
            st.markdown("Prime Solutions Team:")
    
            st.markdown("Isaac Sihlangu: CEO")
            st.markdown("Kobus Leach: COO")
            st.markdown("David Molefe: IMPLEMANTATION SPECIALIST")
            st.markdown("Masindi Phionah: DATA SCIENTIST")
            st.markdown("Seshwene Makhura: DATA ANALYST")
            st.markdown("Xichavo Ngobeni: DATA ENGINEER")
            st.markdown("Nthabiseng Madiba: SOFTWARE DEVELOPER")

        with tab3:
            st.write("We value your feedback and suggestions. If you have any questions, suggestions or ideas on how we can enhance your movie-watching experience, feel free to get in touch with us. We would love to hear from you.")
            st.markdown("Email Address: prime@solutions.org")
            st.markdown("Telephone: 011 345 0000")
            st.markdown("Website: www.primesolutions.com")

    if page_selection == "Contact Us":
        st.title("Get In Touch With Us")

        with st.form("form1", clear_on_submit= True):
            name= st.text_input("Enter Full Name")
            name= st.text_input("Enter Email")
            name= st.text_area("Your message")

            submit= st.form_submit_button("Submit Form")
            
            if submit:
                st.write("Your form has been submitted, We will be in touch with you")

    if page_selection == "Feedback":
        st.title("Rate and Review")
        movie_title = st.text_input("Did You Like The Movies We Recommended?")
        rating = st.radio("Rate The App:", options=[1, 2, 3, 4, 5], format_func=lambda x: "⭐ "*x)
        feedback = st.text_area("Provide feedback on the app:")
        if st.button("Submit"):
            # Save the user's rating and feedback to a database or file
            st.success("Rating and feedback submitted!")

    if page_selection == "Privacy and Security":
        st.title("Privacy and Security")
        st.write("At Prime Solutions, we take your privacy and security seriously. Rest assured that your movie preferences and personal data are protected and will never be shared with any third parties without your explicit consent.")

        image3 = Image.open("resources/imgs/privacy.jpg")
        st.image(image3)
    
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
