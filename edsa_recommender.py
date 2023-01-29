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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
import imaplib
from PIL import Image



# Data handling dependencies
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies = pd.read_csv('resources/data/movies.csv')
ratings = pd.read_csv('resources/data/ratings.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Explore Our App"]
    
    #with st.sidebar:
    #    selection = option_menu("Main Menu", ["Home", "About Us", "Information", "Contact Us"], 
    #    icons=['house', 'people','graph-up-arrow','info-circle','envelope'], menu_icon="cast", default_index=0)
    
    #selected2 = option_menu(None, ["Home","Solution Overview", "Information","About Us","Contact Us"], 
    #icons=['house', 'people', "list-task", 'info-circle'], 
    #menu_icon="cast", default_index=0, orientation="horizontal")


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

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    if page_selection == "Explore Our App":

        selected2 = option_menu(None, ["Home","Solution Overview", "Visualizations","About Us","Contact Us"], 
        icons=['house', 'people', "graph-up-arrow", 'info-circle','telephone'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    
        if selected2 == "Solution Overview":
            st.title("Solution Overview")
            st.write("We will descibe our winning approaches on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

        # Building the "Home" page
        if selected2 == "Home":
            st.markdown('<div style="text-align: center; color:White; font-weight: bold; font-size: 40px;">IntelliTech</br></br></div>', unsafe_allow_html=True)

            # Creating columns to centre the logo and text
            col1, col2, col3 = st.columns([1,6,1])

            with col1:
                st.write("")

            with col2:
                st.image("resources/imgs/intelitech.png")
                st.write("")   # creating a space between image and text
                st.write("")   # creating a space between image and text

                st.markdown("Companies using machine learning understand that business growth requires continuous innovation. \
                At IntelliTech, we provide accurate and robust solutions that help movie companies succeed, by using \
                intelligent algorithms to help viewers find great movies from tens of thousands of options.   \
                \
                ")

                st.markdown('We are a company that creates movie recommender systems and web applications \
                        for businesses.\
                        Most of what we do revolves around the full Data Science Life Cycle:   \
                        ')
                st.markdown(f"""
                    - Data Collection
                    - Data Cleaning
                    - Exploratory Data Analysis
                    - Model Building
                    - Model Deployment
                    """)
                st.markdown(" \n \n Hope over to the next page to learn more...")

            with col3:
                st.write("")
            #st.image('resources/imgs/intelitech.png',use_column_width=True)

            #st.image('resources/imgs/Image_header.png',use_column_width=True)
        
        # Building the "Solution Overview" page
        if selected2 == "Solution Overview":
            # Using Tabs
            tab1, tab2 = st.tabs(["Content-based Recommender System", "Collaborative-based Recommender System"]) 
            with tab1:
                st.info("Content-Based Recommender")
                st.markdown(" This recommender system suggests similar items based on \
                a particular item. It uses item metadata, such as genre, \
                director, description, actors, etc. for movies, to make recommendations.\
             \n \n **Why do we do content-based filtering?**      \n \
             We do content-based \
            filtering to get a similarity between different items so that another similar item can be recommended.\
            \
            In this recommender system the content of the movie (`genres`, `plot_keywords`, \
            `title_cast`, and `title`) is used to find its similarity with other movies. \
            Then the movies that are most likely to be similar are recommended to the user. \
            \
            \n \n Hope over to the next tab to learn more about the Collaborative-based approach! \
            ")
            
            with tab2:
                st.info("Collaborative-Based Recommender")
                st.write(
                """
                With the collaborative-based approach, we can filter out items that a user might like on the basis of reactions by similar users. \
                This provides a more personal touch to your recommended movies!

                With the collaborative-based recommender system, we make use of a trained SVD model \
                to make predictions.

                The SVD model selected showed high performance over the others.
                 

                Hope over to the next page to see some visualizations! 
                """
                )
                #image3 = Image.open("resources/imgs/Sentiment-notebook-picture.jpg")
                #st.image(image3)
            #with tab3:
                #image5 = Image.open("resources/imgs/team-picture.png")
                #st.image(image5)

        if selected2 == "Visualizations":
            #st.subheader("Climate change tweet classification")
            #st.info("Content-Based Recommender")
            
            st.info("Here, you have the option of viewing some visualizations of the \
                        data.  \
            ")

            if st.checkbox("Show ratings plot"):
                st.info("A Bar Graph Showing The Number Of Ratings")		
                #st.markdown("A Bar Graph showing the number of ratings")
                st.bar_chart(data=ratings["rating"].value_counts(), x=None, y=None, width=220, height=520, use_container_width=True)


            if st.checkbox("Show genres plot"):
                # Create dataframe containing only the movieId and genres
                movies_genres_split = pd.DataFrame(movies[['movieId', 'genres']],columns=['movieId', 'genres'])

                # Splitting the genres seperated by "|". Movie-genre combinations are stored as a list
                movies_genres_split.genres = movies_genres_split.genres.apply(lambda x: x.split('|'))

                # Creating the expanded dataframe where each movie-genre combination is in a seperate row
                movies_genres_split = pd.DataFrame([(x.movieId, d) for x in movies_genres_split.itertuples() for d in x.genres],
                                columns=['movieId', 'genres'])

                st.info("A Bar Graph Showing The Number Of Movies In Each Genre.")

                st.bar_chart(data=movies_genres_split, x='genres', y=None, width=220, height=520, use_container_width=True)

    # Building out the "About Us" page
        if selected2 == "About Us":
            # This is our company logo
            #st.image("resources/imgs/LeafLogo.png", caption='Our company logo')
            
            image = Image.open("resources/imgs/unsup.png")
            st.image(image)
            # Centering the logo image
            col1, col2, col3 = st.columns([1,6,1])

            with col1:
                st.write("")

            #with col2:
                #st.image("resources/imgs/LeafLogo.png")

            with col3:
                st.write("")

            # You can read a markdown file from supporting resources folder
            #st.title("Who Are We?")
            st.markdown("")
            st.markdown("")

            st.markdown('<div style="text-align: center; color:White; font-weight: bold; font-size: 20px;">Who Are We?</br></br></div>', unsafe_allow_html=True)

            st.markdown('We are a team of young Data Scientists. The skills within this amazing team range from degrees obtained in Computer Science,  \
                        Marketing, Biomedical Sciences, and IT. \
                        With such a diverse team, you are surely in good hands!   \
                        ')
            
        # Building the "Contact Us" page
        if selected2 == "Contact Us":
            # Building out the contact page
            with st.form("form1", clear_on_submit=True):
                st.subheader("Get in touch with us")
                name = st.text_input("Enter full name")
                email = st.text_input("Enter email")
                message = st.text_area("Message")

                # Set up the email server
                #server = smtplib.SMTP('smtp.gmail.com', 587)
                #server.starttls()
                #server.login("intellitech.movierecommender@gmail.com", "Intellitech$$6")
                
                submit = st.form_submit_button("Submit Form")
                if submit:
                    st.write("Your form has been submitted and we will be in touch 🙂")
                
            
            # Send the email when the user clicks the submit button
            #if st.button("Submit"):
            #    server.sendmail("intellitech.movierecommender@gmail.com", email, message)
            #    st.success("Email sent!")
            
            # Set up the form
            #name = st.text_input("Enter your name")
            #email = st.text_input("Enter your email address")
            #message = st.text_area("Enter your message")

            # Connect to the IMAP server
            #imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
            #imap_server.login("your_email@gmail.com", "your_password")

            # Search for the email address in the INBOX
            #status, messages = imap_server.select("INBOX")
            #status, data = imap_server.search(None, f'FROM "{email}"')
            #submit = st.form_submit_button("Submit Form")

            # Send the email when the user clicks the submit button
            #if st.button("Submit"):
            #    if int(data[0]) > 0:
                    # Email address is found
                    # Send email using the SMTP server
            #        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            #        smtp_server.starttls()
            #        smtp_server.login("intellitech.movierecommender@gmail.com", "Intellitech$$6")
            #        smtp_server.sendmail("intellitech.movierecommender@gmail.com", email, message)
            #        smtp_server.quit()
            #        st.success("Email sent!")
            #    else:
            #        st.error("Email not found.")





if __name__ == '__main__':
    main()
