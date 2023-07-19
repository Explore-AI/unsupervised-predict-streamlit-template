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
import streamlit.components.v1 as components
import base64
import os

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
 
font_css = """
            <style>
            div[data-baseweb="tab-list"] {
                background:rgba(246, 246, 246, 0.4);
                padding: 0 5px 0 5px;
                border-radius: 5px;
            }
            
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
              font-size: 18px;
            }
            
            button[data-baseweb="tab"] {
                background: transparent
            }
            
            button[data-baseweb="tab"]:hover {
                background: rgba(230, 230, 230, 0.4);
                color: rgb(255, 255, 255)
            }
            
            div[data-baseweb="tab-highlight"] {
                background: rgba(230, 230, 230, 0.4);
                color: rgb(255, 255, 255)
            }
            
            button[data-baseweb="tab"]:active {
                background: rgba(230, 230, 230, 0.4);
                color: rgb(255, 255, 255)
            }
            
            div[data-testid="stExpander"] {
                background:rgba(246, 246, 246, 0.4);
                border-radius: 5px;
                box-shadow: 2px 2px;
            }

            </style>
            """
st.markdown(font_css, unsafe_allow_html=True) 

# App declaration
def main():

    def add_bg_from_local(image_path):
        # Get the absolute path of the image file
        image_file = os.path.join('resources', image_path)

        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read())

        st.markdown(
            f"""
            <style>
                .stApp {{
                    background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                    background-size: cover
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

    add_bg_from_local('imgs/istockphoto.jpg')








    with st.sidebar:
        st.image("resources/imgs/Flix.png", width=200)
    st.sidebar.title("Movie Recommendation System")
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Analysis", "About Us","FlixWhiz Info", "Feedback"]

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
        
         
        
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------

    


    if page_selection == "Feedback":

        st.image('resources/imgs/Feedback.jpg', width = 300)
    
       
        # Creating a text box for user input
        feedback_text = st.text_area("","Type Here:")

        if st.button("Submit Feedback"):
            st.info("Feedback Submitted...")
            feedback_text = 'Type Here'

    if page_selection == "Home":

  
      st.title("The ultimate app for EVERY movie enthusiasts")
      st.write("")
      st.image('resources/imgs/red-white-bucket.jpg',use_column_width=True)
      st.write("")
      st.write("FlixWhiz is the perfect app for all your movie recommendations. It gives you the freedom of choosing the perfect movie to watch without wrecking your brain. Input your 3 favourite movies and viola!!")
      st.title("Plenty Movies For Everyone To Enjoy Anywhere, Anytime")


    # Building out the about us page
    if page_selection == "About Us":

        #st.markdown(font_css, unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["Bits And Bytes Data Solutions", "Testimonials", "Contact Us", "The Team"])

        with tab1:
            st.write("")
            st.image('resources/imgs/Logo.jpg',width=300)
            st.write("")
            st.write("Welcome to FlixWhiz, the ultimate destination for movie enthusiasts. Our passion lies in providing personalized movie recommendations that cater to your unique tastes and preferences. With our advanced recommendation algorithms, we analyze your favorite movies, genres, and more to curate a tailored selection of films just for you.")
            st.write("At FlixWhiz, we have a dedicated team of movie lovers and data scientists who are committed to enhancing your movie-watching experience. We continuously update our extensive movie database, refine our algorithms, and incorporate user feedback to ensure that our recommendations are accurate and satisfying.")
            st.write("Discovering the perfect movie has never been easier. Whether you're in the mood for action, romance, comedy, or any other genre, FlixWhiz is here to guide you. Join us on this cinematic journey and let FlixWhiz be your trusted companion for finding the next great film to enjoy.")


        with tab2: 
            st.write("")
            st.image('resources/imgs/Test.jpg',width=300)
            st.write("")

            col8, col9 = st.columns(2)
            with col8:
                st.markdown("\"As a movie enthusiast, FlixWhiz is my go-to platform for finding new films to watch. The recommendations are always on point, and I appreciate the variety of genres and options available. It's like having my own personal movie curator!\" - Sarah White")
             
            with col9:
                st.markdown("\"I've tried other movie recommendation platforms, but none come close to FlixWhiz. The accuracy of their recommendations is impressive, and the quality of the movies suggested is consistently high. I've discovered some of my all-time favorite films through this app.\" - Mpho Maremane")

            st.write("")
            col10, col11 = st.columns(2)
            with col10:
                st.markdown("\"FlixWhiz has revolutionized the way I discover movies. The personalized recommendations are spot-on, and I've discovered so many hidden gems that I wouldn't have found otherwise. Highly recommended!\" - John Schoeman")

            with col11:
                st.markdown("\"I love how easy and user-friendly FlixWhiz is. The interface is clean and intuitive, and the recommendations are tailored to my preferences. It's like having a virtual movie buddy who knows exactly what I'll enjoy!\" - Michael Reid")

        with tab3:

            col12, col13 = st.columns(2)
            with col12:
                # Contact Us Section
                st.title("Contact Us")

                # Input fields for name, email, and message
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Message")

                # Submit button
                if st.button("Submit"):
                   # Process the form data
                   # You can add your own logic here, such as sending an email or storing the data in a database
                   st.success("Thank you for your message! We will get back to you soon.")
            
                st.write("")
            
        with tab4:
            #st.write("# MEET THE TEAM")
            st.markdown("<p style='text-align: center; font-size: 80px; font-family: cursive; font-weight: bold; '>MEET THE TEAM</p>", unsafe_allow_html=True)
            #st.image('resources/imgs/meet-team.jpg') 
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            with st.container():
                st.write("<p style='text-align: center; font-size: 50px; '>The Notebook Team</p>", unsafe_allow_html=True)
				
                with st.container():
                    
                    col1, col2, col3 = st.columns(3)
				
                with col1:
                    #st.header("Rinae Luvhani")
                    st.image('resources/imgs/W.png')
                    st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Rinae Surname</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Occupation: Data scientist</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  Your Place or Mine</p>", unsafe_allow_html=True)
					
                with col2:
                    #st.header("Nassau Carstens")
                    st.image('resources/imgs/M.png')
                    st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Nassau Surname</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Occupation: Data Engineer</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  Apocalypse Now</p>", unsafe_allow_html=True)
						
                with col3:
                    #st.header("Bonolo Surname")
                    st.image('resources/imgs/M.png')
                    st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Bonolo Surname</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Occupation: Researcher</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  </p>", unsafe_allow_html=True)
                    st.write("")
                    st.write("")
                    
                            
                with st.container():
                    st.write("<p style='text-align: center; font-size: 50px; '>The Strealit Team</p>", unsafe_allow_html=True)
                    
                    with st.container():
                    
                        col1, col2, col3 = st.columns(3)
				
                with col1:
                    #st.header("Matsawela Phiri")
                    st.image('resources/imgs/W.png')
                    st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Matsawela Phiri</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Occupation: Full Stack Developer</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  I still believe</p>", unsafe_allow_html=True)
					
                    with col2:
                        #st.header("Mmabatho Mojapelo")
                        st.image('resources/imgs/w.png')
                        st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Mmabatho Mojapelo</p>", unsafe_allow_html=True)
                        st.write("<p style='text-align: center; font-size: 12px; '>Occupation: UX/UI Designer</p>", unsafe_allow_html=True)
                        st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  </p>", unsafe_allow_html=True)
                        
						
                        with col3:
                            #st.header("Matlala Nyama")
                            st.image('resources/imgs/W.png')
                            st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Matlala Nyama</p>", unsafe_allow_html=True)
                            st.write("<p style='text-align: center; font-size: 12px; '>Occupation: DevOps Engineer</p>", unsafe_allow_html=True)
                            st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  </p>", unsafe_allow_html=True)
                            st.write("")
                            st.write("")

                with st.container():
                    st.write("<p style='text-align: center; font-size: 50px; '>Project Management Team</p>", unsafe_allow_html=True)
                    
                    with st.container():
                    
                        col1, col2, col3 = st.columns(3)
				
                with col2:
                    #st.header("Temishka Pillay")
                    st.image('resources/imgs/W.png') 
                    st.write("<p style='text-align: center; font-size: 20px; font-family: cursive; '>Temishka Surname</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Occupation: Project Manager</p>", unsafe_allow_html=True)
                    st.write("<p style='text-align: center; font-size: 12px; '>Current Favorite Movie:  </p>", unsafe_allow_html=True)           


            with col13:
                st.title("Contact Details")
                st.write("Office Line : (+27) 43 656 9800")
                st.write("Emergency Line : (+27) 43 656 9000")
                st.write("Email Address : info@bitsandbytes.co.za")
                st.image("resources/imgs/Logo.jpg", width=300)

    if page_selection == "FlixWhiz Info":
        st.write("")






    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
      main()
