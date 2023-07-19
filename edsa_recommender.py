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
        #st.title("Solution Overview")
        #st.write("Describe your winning approach on this page")
        
        #st.title("The ReelDeal")
        #st.header('This is a header')
        
        st.header('Problem Statement')
        st. write('''Recommender systems have become crucial in today's technology-driven world, enabling individuals to make informed choices about the content they engage with regularly. Movie content recommendations are particularly important in this regard, as intelligent algorithms can assist viewers in discovering great titles from a vast selection of options.''')
        
        with st.expander("**Business Value**"):
            st.write('**Enhanced User Experience:**')
            st.write('''Recommender systems enhance the user experience by providing personalized recommendations tailored to individual preferences. By suggesting relevant and interesting movies, users are more likely to engage with the platform and discover content they enjoy. This leads to increased user satisfaction and a higher likelihood of repeat visits.''')
            st.divider()
            st.write('**Increased User Engagement:**')
            st.write('''A well-designed recommender system increases user engagement by capturing and understanding user preferences. By analyzing historical data, the system can identify patterns, preferences, and user behavior, thereby presenting users with movies that align with their interests. Increased user engagement translates to longer session durations, more frequent visits, and higher user retention rates.''')
            st.divider()
            st.write('**Improved Customer Satisfaction:**')
            st.write('''Recommender systems help users discover movies they are likely to enjoy but might have otherwise missed. By providing accurate and relevant recommendations, users feel satisfied and perceive the platform as valuable. This satisfaction leads to positive word-of-mouth recommendations, increased customer loyalty, and reduced churn rates.''')
            st.divider()
            st.write('**Revenue Generation:**')
            st.write('''A well-executed recommender system can have a significant impact on revenue generation. By showcasing relevant movie recommendations, users are more likely to engage with the platform, leading to increased content consumption and potential revenue streams such as subscriptions, rentals, or advertising. Additionally, recommender systems can leverage personalized recommendations to upsell or cross-sell related products or services, further increasing revenue opportunities.''')
            st.divider()
            st.write('**Data-Driven Decision Making:**')
            st.write('''Building a recommender system requires collecting and analyzing vast amounts of user data. This data can provide valuable insights into user preferences, trends, and behavior, enabling data-driven decision making for content acquisition, production, and marketing strategies. By leveraging the knowledge gained from the recommender system, platforms can make informed decisions to optimize their movie catalog and marketing efforts.''')
            st.divider()
            st.write('**Competitive Advantage:**')
            st.write('''In today's competitive landscape, a well-implemented recommender system can serve as a differentiating factor for platforms. By providing accurate and personalized recommendations, platforms can attract new users and retain existing ones, positioning themselves as leaders in the industry. This competitive advantage can result in increased market share, brand recognition, and growth opportunities.''')
        st.header('Solution')
        st.write('''"The ReelDeal" - Your Ultimate Movie Recommender App!

Are you tired of endlessly scrolling through streaming platforms, trying to find the perfect movie to watch? Look no further! The ReelDeal is here to revolutionize your movie-watching experience with its advanced recommendation system that caters for collaborative filtering and content filtering techniques.''')
        
        tab1, tab2 = st.tabs(["Content Filtering", "Colaborative Filtering"])

        with tab1:
            st.header("Content Filtering")
            st.write('''The ReelDeal utilizes content filtering, which focuses on the characteristics and attributes of movies themselves. By analyzing the content, genre, actors, directors, and other metadata associated with movies, the app can provide recommendations based on your personal preferences and interests. Whether you're a fan of action-packed blockbusters, romantic comedies, or indie dramas, The ReelDeal will suggest movies that align with your specific tastes.''')
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

        with tab2:
            st.header("Colaborative Filtering")
            st.write('''But that's not all! Collaborative filtering is a powerful algorithm that analyzes user behavior and preferences to find similarities among users. By considering the preferences of users who have similar tastes as you, The ReelDeal can suggest movies that you're likely to enjoy. It takes into account various factors, such as ratings, watch history, and movie preferences of like-minded users, to generate accurate recommendations tailored just for you.''')
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        
        st.write('''Here are some key features of The ReelDeal:''')
        with st.expander("**Key Features**"):
            st.write("")
            st.write('''Personalized Recommendations: FlickFusion understands your unique preferences and delivers personalized movie recommendations that suit your taste, making it easier for you to discover new films that you'll love.

Rating and Review System: Rate and review movies you've watched to further fine-tune the app's recommendations. You can also read reviews from other users to get insights and make informed decisions.

Watchlist: Create a personalized watchlist to keep track of movies you want to watch in the future. FlickFusion will remind you when they become available on your preferred streaming platforms.

Seamless Integration: FlickFusion integrates with popular streaming services like Netflix, Amazon Prime, Hulu, and more, allowing you to directly stream recommended movies with just a few clicks.

User Community: Connect with like-minded movie enthusiasts through the FlickFusion community. Share your thoughts, discuss movies, and get recommendations from fellow users.''')
        
        
        st.write('''The ReelDeal is the ultimate movie companion that brings the power of collaborative filtering and content filtering together, ensuring that you never run out of fantastic movies to watch. Say goodbye to endless scrolling and start enjoying personalized movie recommendations today!''')


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
