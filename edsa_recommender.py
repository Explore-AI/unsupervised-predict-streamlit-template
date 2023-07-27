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
import scipy as sp

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Explorer","Solution Overview","Contact Us"]
    st.sidebar.image('resources/imgs/flix.png',use_column_width=True)
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose App Mode", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        st.write('# Movie Recommender Engine')
        # Recommender System algorithm selection
        sys = st.radio("### Select an algorithm",
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
    st.markdown(#Recommender background
         f"""
         <style>
         .stApp {{
             background: url("https://openthemagazine.com/wp-content/uploads/2019/10/JOker.jpg?raw=true");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    if page_selection == "Solution Overview":

        st.title("Solution Overview")
        st.write("### Explore the business and technical aspects of our solution")
        tab1,tab2 = st.tabs(["Business","Technical"])
        with tab1:
    
            st.write("""To build an effective recommendation algorithm, we need access to a vast amount 
                     of user data, including historical movie preferences, ratings, and interactions. 
                     The business aspect involves setting up mechanisms to collect, store, and manage 
                     this data securely and ethically. The success of the app relies on providing a 
                     seamless and engaging user experience. The algorithm should integrate seamlessly 
                     with the app's interface, ensuring that movie recommendations are prominently displayed 
                     and easily accessible to users. As the user base grows, the algorithm should be scalable 
                     to handle increasing data and user interactions efficiently. The business needs to plan
                      for server infrastructure and data processing capabilities that can handle this growth. 
                     Given the sensitivity of user data, ensuring strict data privacy and security measures 
                     will be a top priority.""")

            #st.image ("resources/imgs/flix.png")

        with tab2:

            st.write("""The technical solution involves integrating data from multiple sources, 
                     including the MovieLens dataset and movie content data from IMDb. This may require data 
                     preprocessing and alignment to create a unified dataset.
                     """)
            st.write(" ")         
            st.write(""" 
                     The data must undergo thorough cleaning to handle missing values, outliers, and 
                     inconsistencies that could adversely affect the accuracy of the recommendation 
                     algorithm. Extracting relevant features from the data is crucial for content-based 
                     filtering. Features such as movie genre, cast, director, and release year will be used 
                     to create user profiles and movie representations.
                     """)
            st.write(" ")
            st.write("""Implementing collaborative filtering 
                     techniques, such as user-based or item-based filtering, will help identify similar users 
                     and movies to make accurate predictions. Utilizing content-based filtering, the algorithm
                      will match user preferences with movie attributes to recommend similar movies that the 
                     user has not yet viewed.
                     """)  
            st.write(" ")
            st.write("""The selected models will be trained using historical user ratings 
                     and movie attributes. The technical team will fine-tune the models to achieve the highest 
                     predictive accuracy. To support scalability and performance, the technical solution may 
                     involve cloud-based infrastructure, such as AWS or Google Cloud, to handle data storage, 
                     processing, and user interactions.""")                      
 

            

        

    
    st.markdown( # Explorer background
         f"""
         <style>
         .stApp {{
             background: url("https://openthemagazine.com/wp-content/uploads/2019/10/JOker.jpg?raw=true");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    if page_selection == "Explorer":
        # Header contents
        #st.image('resources/imgs/Image_header.png',use_column_width=True)
        st.title('Explorer')
        st.write('### Explore movies in associate streaming platforms')
        tab1,tab3 = st.tabs(["Custom Pix","Coming Soon"])

        with tab1:
            st.write('### Pick Filters')
            
            sys2 = st.radio("Filters",
                        ("Genre",
                            "Cast Member","Release Date"))
            if sys2 == "Genre":
                movie_1 = st.selectbox('Genre',('All','Action','Comedy','Drama','Romance','Thriller'))
                if movie_1 != 'Action':
                    # Perform actions or show output based on the selected genre
                    # Display 10 drama movies
                    st.write(f"Movies in the genre: {movie_1}")
                # Create a button to redirect user to another website
                button_clicked = st.button("Visit Associate Streaming Platform")
        
                if button_clicked:
                    # Define the URL based on the selected cast member
                    imdb_url = get_imdb_url(movie_2)
                    
                    if imdb_url:
                        # Redirect the user to the IMDb page
                        st.markdown(f"<a href='{imdb_url}' target='_blank'>Go to IMDb</a>", unsafe_allow_html=True)
                    else:
                        st.write("IMDb URL not available")
            if sys2 == "Cast Member":
                movie_2 = st.selectbox('Cast Member',('Denzel Washington','Tom Hardy','Will Smith','Jackie Chan','Bruce Lee','Luhle Shumi','Martin Lawrence','Martin Briestol'))
                st.write(f"Movies by: {movie_2}")
                # Create a button to redirect user to another website
                button_clicked = st.button("Visit Associate Streaming Platform")
        
                if button_clicked:
                    # Define the URL based on the selected cast member
                    imdb_url = get_imdb_url(movie_2)
                    
                    if imdb_url:
                        # Redirect the user to the IMDb page
                        st.markdown(f"<a href='{imdb_url}' target='_blank'>Go to IMDb</a>", unsafe_allow_html=True)
                    else:
                        st.write("IMDb URL not available")
            if sys2 == "Release Date":
                movie_3 = st.selectbox('Release Date',('2019','2018','2016-2017','2010-2015','2001-2009','1994-2000'))
                st.write(f"Movies relesed during: {movie_3}")
                # Create a button to redirect user to another website
                button_clicked = st.button("Visit Associate Streaming Platform")
        
                if button_clicked:
                    # Define the URL based on the selected cast member
                    imdb_url = get_imdb_url(movie_2)
                    
                    if imdb_url:
                        # Redirect the user to the IMDb page
                        st.markdown(f"<a href='{imdb_url}' target='_blank'>Go to IMDb</a>", unsafe_allow_html=True)
                    else:
                        st.write("IMDb URL not available")
        with tab3:
            # Update the URL params to trigger a redirect
            st.experimental_set_query_params(redirect=True)
            st.write("Redirecting...")


    if page_selection == "Contact Us":
        st.title('Contact Us')
        st.write("Please fill out the form below to get in touch with us.")
    
        # Display input fields
        # Display input fields
        name_placeholder = st.empty()
        name = name_placeholder.text_input("Your Name")
    
        email_placeholder = st.empty()
        email = email_placeholder.text_input("Your Email")
    
        message_placeholder = st.empty()
        message = message_placeholder.text_area("Message")
    
        # Submit button
        if st.button("Submit"):
            # Process the form data here (e.g., send an email, store in a database)
        
            # Display a success message
            st.success("Thank you for reaching out! We will get back to you soon.")
        
            # Reset input fields
            name_placeholder.text_input("Your Name", value="", key="reset_name")
            email_placeholder.text_input("Your Email", value="", key="reset_email")
            message_placeholder.text_area("Message", value="", key="reset_message")

def get_imdb_url(cast_member):
    # Placeholder function to get IMDb URL based on the cast member
    # Replace this with your own logic to generate the correct IMDb URL
    
    imdb_urls = {
        'Denzel Washington': 'https://www.imdb.com/name/nm0000243/',
        'Tom Hardy': 'https://www.imdb.com/name/nm0362766/',
        'Will Smith': 'https://www.imdb.com/name/nm0000226/',
        'Jackie Chan': 'https://www.imdb.com/name/nm0000329/'
        }            
            








    
    


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
