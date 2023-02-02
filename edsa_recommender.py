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

    def add_bg_from_url(): ## The main background added

        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://pixabay.com/illustrations/north-star-stars-night-night-sky-2869817/");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    add_bg_from_url()  

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Why Starlink","Movie selector","About us","Contact us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### Connecting you to the stars')
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
    if page_selection == "Why Starlink":
        st.title("Why Starlink")
        st.write ("Starlink approaches problems in a systematic manner, carefully executing each step\
                   along the way in  order to extract the maximum amount of information from data.our\
                   team uses various statistical methods and technological tools used to make sense of\
                   and model data. Our employees boast domain knowledge that makes it easy to apply the\
                   right methods to extract valuable insights as well as the right methods to judge the\
                   performance of our models properly.")

    if page_selection == "Movie selector":

        def add_bg_from_url():
         st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1475274047050-1d0c0975c63e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2072&q=80.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

        add_bg_from_url() 

        st.subheader("Movie Filter")

        st.write("This section is based of you using the presented filter base to generate a list of movies:")               
        movie_gallery = "https://images.unsplash.com/photo-1581905764498-f1b60bae941a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=464&q=80.open('sunrise.jpg')"
        st.image(movie_gallery, caption='movie gallery')


        st.subheader("Please select your favourite genres: ")
        selected_genres = st.multiselect(
          'Please select your favourite genres:',
          ['action','adventure','comedy','drama','fantasy','horror','musicals','mystery'])
            
            
        

        st.write('You selected:', selected_genres)


        st.subheader("Please select the desired length of the movie: ") ## I would have to add the Movie.csv

        start_len = 0     
        start_len, end_len = st.select_slider(
        'Select the length of the movie: ',
         options=['0', '30', '60', '90', '120', '150', '180'],
         value=('0', '90'))
        st.write('You selected the length of the movies to be between ',start_len, 'minutes and', end_len,'minutes.')


        st.subheader("Please select the desired movie ratings : ")
        
        stared_option = st.selectbox(
        'Select rating of the movie: ', ## 
        ('1.0', '2.0', '3.0', '4.0', '5.0'))
        st.write('You selected:', stared_option)

        

    




        if st.button('Generate'):
            st.write('Your filtered movies')

        else:
            st.write('Please try again')





    if page_selection == "About us":

        
        def add_bg_from_url():
         st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1475274047050-1d0c0975c63e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2072&q=80.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

        add_bg_from_url() 

        st.write("This section is based of you using the presented filter base to generate a list of movies:")               
        movie_gallery = "https://images.unsplash.com/photo-1581905764498-f1b60bae941a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=464&q=80.open('sunrise.jpg')"
        st.image(movie_gallery, caption='movie gallery')


        st.title("About us")

        
        def add_bg_from_url():
         st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1475274047050-1d0c0975c63e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2072&q=80.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

        add_bg_from_url() 


        st.write("We believe that we are only as good as the impact we give.With a nationwide presence,\
                  Starlink positively impacts our client firms successses thanks to our clear vision.\
                  use of technology, clear values, and most importantly our people. Our diverse workforce\
                  comes with vast domain knowledge in variety of industries and works in unison to provide\
                  insights and postive impact to a number of companies.'unity in diversity' is our motto\
                                                                                                         \
                  With more than 5 years of hard work and commitment to making a real differnce, Starlink\
                  continues to grow while providing world-class data analytics and consulting services\
                                                                                                          \
                  Starlink is defined by our drive to make an impact that matters in the world and providing\
                  solutions to the challenges that face businesses,goverment and society at large.")          

    if page_selection == "Contact us":
        with st.container():
            st.write("---")
            st.header("We would love to hear from you")
            st.write("##")
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

        contact_form = """
        <form action="https://formsubmit.co/starlink.za@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")
if __name__ == '__main__':
    main()
