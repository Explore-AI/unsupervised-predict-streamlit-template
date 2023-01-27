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
import PIL.Image
import os
from tkinter import Image
import matplotlib.pyplot as plt
import seaborn as sns

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgzHpXP1ybvtWDtMfb390cHIxBGrQ7WDmtcw&usqp=CAU');
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);

}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url('https://png.pngtree.com/background/20210711/original/pngtree-curled-film-movie-and-television-blue-background-picture-image_1168260.jpg');
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies = pd.read_csv('https://media.githubusercontent.com/media/LPTsilo/Team_ES2_Unsupervised_Predict/main/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    
    page_options = ["Recommender System","Solution Overview","EDA"]

    image = PIL.Image.open(os.path.join("resources/imgs/team_logo.jpg"))
    st.image(image, width=300, caption='')
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
    #image = PIL.Image.open(os.path.join("resources/imgs/team_logo.jpg"))
    #st.image(image, caption='')
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        
        st.write("Describe your winning approach on this page")

    if page_selection == "EDA":
        # Header contents
        st.title("Exploratory data Analysis")
        #st.image('resources/imgs/Image_header.png',use_column_width=True)
        st.write('## Gather additional insights')
        #Create selectbox for EDA components
        eda_options = ["Genres","Movies","Users"]
        eda_selection = st.selectbox("Select the insights to be explored", eda_options)

        #Define functions to create plots
        def plot_most_frequent(title,df,y_lab,x_lab,top,order=False):
            """
            This function plots a count plot
            """
            plt.figure(figsize=(15,10),tight_layout=True)
            sns.countplot(y=y_lab, data=df,
                        order=df[y_lab].value_counts(ascending=order)[0:top].index,palette='Blues_r')
            plt.xlabel('Count', fontsize=30)
            plt.ylabel(y_lab.capitalize(), fontsize=30)
            plt.yticks(fontsize=20)
            plt.xticks(fontsize=20)
            plt.show()

        def bar_plot_func(title,df,y_lab,x_lab,top,order=False):
            """
            This function plots a bar plot of the words
            """

            plt.figure(figsize=(15,10),tight_layout=True)
            sns.barplot(x = x_lab, y = y_lab,
                        data = df.sort_values(x_lab,ascending = order)[0:top],
                        palette = 'Blues_r')
            plt.xlabel(x_lab.capitalize(), fontsize=12)
            plt.ylabel("", fontsize=12)
            plt.yticks(fontsize=20)
            plt.xticks(fontsize=12)
            plt.show()

        # Create a bar plot of the top 20 best rated movies
        fig, ax  = plt.subplots(1,2,figsize=(20,10))
        sns.barplot(ax=ax[0], x='rating',y = 'title', data=movies.head(20)) 
        ax[0].set_title('The top 20 best rated movies ') 


        #st.title("EDA Overview")
        #st.write("Describe your winning approach on this page")    
    
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
