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
import matplotlib.pyplot as plt
import time
import warnings
import wordcloud
from wordcloud import WordCloud

# Ignore FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
gen=pd.read_csv("resources/data/aggregated_rating_streamlit.csv")
mov=pd.read_csv("resources/data/movie_details_average.csv")
pie=pd.read_csv("resources/data/gen_only.csv")
movie_df = pd.read_csv('resources/data/movie_insights_3.csv')
tag_df = pd.read_csv('resources/data/tag_insights.csv')
rating_count = pd.read_csv('resources/data/rating_count.csv')

# Displaying the logo image

log = "resources/imgs/logo.jpg"
#st.image(image, width=200)

cola, mid, colb = st.columns([25,1,40])
with mid:
	st.image(log, width=100)

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Instruction & Overview",'Insights', 'Contact Us']
    with st.sidebar:
        st.image(log, width=250)

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
        movie_2 = st.selectbox('Second Option',title_list[2325:2525])
        movie_3 = st.selectbox('Third Option',title_list[2020:2120])
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
    if page_selection == "Instruction & Overview":
        st.title("Welcome to ***DATAMIN*** Movie Recommender App 🎥🍿")
        st.image("resources/imgs/Movie-Recommendation-System-with-Streamlit-and-Python-ML-1.jpg",)
        st.write("Hi there🙋‍♂️, looking for that nice thing to watch without having to go over the hustle of scrolling for movies? Relax, we've got you.🤗")
        st.write("")
        st.subheader("About the App")
        st.write("This app helps you discover personalized movie recommendations based on your preferences.")
        st.write("On the left of this page you will find a side-bar with a dropdown menu for the pages available, these pages include:")
        st.write("1. **Recommender System** - This is where you will get your recommended movies.")
        st.write("2. **Instruction and Overview** - The current page with the information about how to use this App.")
        st.write("3. **Insights** - This is were you get the insigts about the movies and genres. ")
        st.write("4. **Contact Us** - This page has the App developer team information.")

        
        # Defining a list of image paths
        image_urls = [
            "resources/imgs/free.jpg",
            "resources/imgs/images.jpg",
            "resources/imgs/download.jpg"
        ]

        # Creating three columns for the images
        col1, col2, col3 = st.columns(3)

        # Set a common width for the images
        image_width = 200

        # Loop through the images and display them in the columns
        index = 0
        count_pic = 0 
        while count_pic <1 :
            count_pic +=1
            col1.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
            index = (index + 1) 
            col2.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
            index = (index + 1) 
            col3.image(image_urls[index], width=image_width)
            time.sleep(2)  # Change image every 5 seconds
        
        # Center-align the subheader using Markdown and HTML formatting
        st.markdown("<h2 style='text-align: center;'>Yummy Flavors😋...!</h2>", unsafe_allow_html=True)

        st.subheader("How to Use the App")
        st.write("1. Navigate to the 'Recommender System' page.")
        st.write("2. Select the type of filtering (Content-based or Collaborative) for you movie choices.")
        st.write("2. Select you three favourated movies.")
        st.write("2. Press 'Recommand'.")
        st.write("3. Receive personalized movie recommendations based on your favourite movies.")

        st.write("**Content-based filtering** - means your recommended movies will be based on the properties of your three favourite movies.")
        st.write("**Collaborative filtering** - means your recommended movies will be based on other users who have liked your favourite movies.")
    
    if page_selection == "Insights":

       # st.markdown("<h2 style=color:#3FBEBF;>Top Rated Movies By Genres</h2>",unsafe_allow_html=True)

        tab1,tab2,tab3=st.tabs(["Genres Insights","Movie Insights","Other Visuals"])

        with tab1:
            col1,col2,col3,col4,col5=st.columns([10,10,15,10,10])
            with col1:
                act=st.checkbox("Action")
                war=st.checkbox("War")
                rom=st.checkbox("Romantic")
                com=st.checkbox("Comedy")
            with col2:
                drm=st.checkbox("Drama")
                adv=st.checkbox("Adventure")
                sf=st.checkbox("Sci-fi")
                thr=st.checkbox("Thriller")
            with col3:
                ani=st.checkbox("Animation")
                doc=st.checkbox("Documentary")
                chi=st.checkbox("Children")
                fan=st.checkbox("Fantasy")
            with col4:
                cri=st.checkbox("Crime")
                hor=st.checkbox("Horror")
                mys=st.checkbox("Mystery")
                im=st.checkbox("IMAX")
            with col5:
                mus=st.checkbox("Musical")
                wes=st.checkbox("Western")
                fil=st.checkbox("Film-Noir")

            ls="True"
            btn=st.button("Explore")

            if btn:
                col6,col7=st.columns([10,10])
                g_count=pie['genres'].value_counts()
                if act:
                    ls=ls+"& gen['Genres'].str.contains(\"Action\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Action")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Action'
                if war:
                    ls=ls+"& gen['Genres'].str.contains(\"War\")"
                    df_selected_genre = mov[mov['genres'].str.contains("War")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'War'
                if rom:
                    ls=ls+"& gen['Genres'].str.contains(\"Romance\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Romance")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Romance'
                if com:
                    ls=ls+"& gen['Genres'].str.contains(\"Comedy\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Comedy")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Comedy'
                if drm:
                    ls=ls+"& gen['Genres'].str.contains(\"Drama\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Drama")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Drama'
                if adv:
                    ls=ls+"& gen['Genres'].str.contains(\"Adventure\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Adventure")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Adventure'
                if sf:
                    ls=ls+"& gen['Genres'].str.contains(\"Sci-Fi\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Sci-Fi")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Sci-Fi'
                if thr:
                    ls=ls+"& gen['Genres'].str.contains(\"Thriller\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Thriller")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Thriller'
                if ani:
                    ls=ls+"& gen['Genres'].str.contains(\"Animation\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Animation")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Animation'
                if doc:
                    ls=ls+"& gen['Genres'].str.contains(\"Documentary\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Documentary")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Documentary'
                if chi:
                    ls=ls+"& gen['Genres'].str.contains(\"Children\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Children")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Children'
                if fan:
                    ls=ls+"& gen['Genres'].str.contains(\"Fantasy\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Fantasy")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Fantasy'
                if cri:
                    ls=ls+"& gen['Genres'].str.contains(\"Crime\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Crime")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Crime'
                if hor:
                    ls=ls+"& gen['Genres'].str.contains(\"Horror\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Horror")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Horror'
                if mys:
                    ls=ls+"& gen['Genres'].str.contains(\"Mystery\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Mystery")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Mystery'
                if im:
                    ls=ls+"& gen['Genres'].str.contains(\"IMAX\")"
                    df_selected_genre = mov[mov['genres'].str.contains("IMAX")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'IMAX'
                if mus:
                    ls=ls+"& gen['Genres'].str.contains(\"Musical\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Musical")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Musical'
                if wes:
                    ls=ls+"& gen['Genres'].str.contains(\"Western\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Western")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Western'
                if fil:
                    ls=ls+"& gen['Genres'].str.contains(\"Film-Noir\")"
                    df_selected_genre = mov[mov['genres'].str.contains("Film-Noir")]
                    df_genre_count = df_selected_genre.groupby(df_selected_genre['year'])['genres'].count()
                    highlight_genre = 'Film-Noir'
                with col6:
                    st.write("<p style='text-align: center;'>Top Ranked Movies</p>", unsafe_allow_html=True)
                    exec("st.write(gen["+ls+"].sort_values(by=['rating'], ascending=False,ignore_index=True)[['Title']])")
                with col7:
                    st.write("<p style='text-align: center;'>Proportion of the Genre</p>", unsafe_allow_html=True)
                    fig, ax = plt.subplots()
                    ax.pie(g_count.values, labels=g_count.index)
                    highlight_index = g_count.index.tolist().index(highlight_genre)
                    highlighted_wedge = ax.patches[highlight_index]
                    highlighted_wedge.set_edgecolor('white')
                    highlighted_wedge.set_linewidth(3)
                    highlighted_wedge.set_alpha(1)
                    ax.axis('equal')
                    st.pyplot(fig)

                col8,col9=st.columns([10,1])
                with col8:
                    st.write("<p style='text-align: center;'>Movies Releases Per Year</p>", unsafe_allow_html=True)
                    st.line_chart(df_genre_count)

  
        with tab2:
            years = sorted(movie_df['year'].unique())
            selected_year1 = st.selectbox("Select a year", years,key="movie_In")
            selected_year_df = movie_df[movie_df['year'] == selected_year1]
            all_movies_df = selected_year_df.sort_values(by=["rating"], ascending=False,ignore_index=True)[["title"]]
            st.write("List of Movies For the Year **{}**".format(selected_year1))
            st.write(all_movies_df)

            with st.form(key='searchform'):
                nav1,midn,nav2=st.columns([10,3,3])
                with nav1:
                    search_term=st.text_input("Which Movie You Want Details On?")
                with nav2:
                    st.text(" ")
                    st.text(" ")
                    submit_search=st.form_submit_button(label='Search')
        if submit_search:
            #st.success("You have searched for the movie **{}**.".format(search_term))
            
            ls=ls+"& mov['title'].str.contains(search_term)"
            mov['title'] = mov['title'].fillna('Unknown').astype(str)
            df_details=mov[mov['title'].str.contains(search_term,na=False)].sort_values(by=['year'], ascending=False,ignore_index=True)
            df_details['year'] = df_details['year'].astype(int)
            
            #exec("st.write(mov["+ls+"].sort_values(by=['year'], ascending=False,ignore_index=True)[['title','rating','genres','year','director','runtime','budget','title_cast']])")
            #df_details_dict=df_details.to
            

            def f_col(title,year,runtime,budget):
                st.write("-------")
                st.write("**Title:** ",title)
                st.write("**Year:** ",str(year))
                st.write("**Runtime:** ", str(runtime) + " Minutes")
                st.write("**Budget:** ",budget)
            
            def s_col(director,title_cast):
                st.write("---------")
                st.write("**Director:** ",director)
                st.write("**Casts:** ",title_cast)
                
            
            for i, r in df_details.iterrows():
                col10,col11=st.columns([10,10])
                with col10:
                    f_col(title=r['title'],year=r['year'],runtime=r['runtime'],budget=r['budget'])
                        
                        
                with col11:
                    s_col(director=r['director'],title_cast=r['title_cast'])

            filtered_m = tag_df[tag_df['title'].str.contains(search_term)] 
            selected_tags=filtered_m['tag']     
            m_tags=" ".join(selected_tags)
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(m_tags)

            # Display the WordCloud using Streamlit
            st.title(f"Word Cloud for the Movie {search_term}")
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)
        
        with tab3:

            # Get unique years from the DataFrame
            years = sorted(movie_df['year'].unique(), reverse=True)
            st.subheader('Select a year to see the top 10 rated movies for that year.')
            # Creating a sidebar with the year dropdown
            selected_year = st.selectbox("Select a year", years)

            # Filtering the DataFrame for the selected year
            selected_year_df = movie_df[movie_df['year'] == selected_year]

            # Sorting the DataFrame by rating in descending order and get the top ten movies
            top_movies_df = selected_year_df.nlargest(10, 'rating' )

            # Creating the bar chart
            fig, ax = plt.subplots(figsize=(12, 6))

            # Plotting the horizontal bar chart
            ax.barh(top_movies_df['title'], top_movies_df['rating'], color='skyblue')

            # Setting the font size for x and y-axis labels
            ax.tick_params(axis='x', labelsize=14)  # Set the font size for x-axis labels
            ax.tick_params(axis='y', labelsize=14)  # Set the font size for y-axis labels

            # Setting the x and y-axis labels and the title
            ax.set_xlabel('Rating', fontsize=16)   # Set the font size for x-axis label
            ax.set_ylabel('Movie Title', fontsize=16)  # Set the font size for y-axis label
            ax.set_title(f'Top 10 Movies of {selected_year}', fontsize=18)  # Set the font size for the title

            # Display the chart
            plt.tight_layout()  # Ensures all elements fit within the figure area

            # Desplaying the bar chart
            st.pyplot(fig)

            # Show the top ten movie titles in a table
            st.write("Top Ten Movie Titles:")
            st.table(top_movies_df[['title']])

            #---------------------------------------------------------------------------------------------------#
            # Create a dropdown to allow the user to select a year
            years = sorted(rating_count['year'].unique(), reverse=True)
            st.subheader('Select a year to see movies with the highest number of users that rated them for that year')
            selected_year = st.selectbox('Select a year', years)
            
            # Filter the merged DataFrame based on the selected year
            filtered_df = rating_count[rating_count['year'] == selected_year]

            # Group the filtered DataFrame by movie title and count the number of unique users
            movie_ratings_count = filtered_df.groupby('title')['userId'].nunique().reset_index()
            movie_ratings_count = movie_ratings_count.rename(columns={'userId': 'user_count'})

            # Sort the movies based on rating count in descending order
            movie_ratings_count = movie_ratings_count.sort_values(by='user_count', ascending=False)

            # Select only the top 10 movies (if there are more than 10)
            if len(movie_ratings_count) > 10:
                movie_ratings_count = movie_ratings_count.head(10)

            # Create a horizontal bar chart
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.barh(movie_ratings_count['title'], movie_ratings_count['user_count'], color='skyblue')

            # Setting the font size for x and y-axis labels
            ax.tick_params(axis='x', labelsize=12)  # Set the font size for x-axis labels
            ax.tick_params(axis='y', labelsize=12)  # Set the font size for y-axis labels

            ax.set_xlabel('Number of Users',fontsize=14)
            ax.set_ylabel('Movie Title',fontsize=14)
            ax.set_title(f'Top 10 Movies with Highest Rating Count in {selected_year}',fontsize=16)
            plt.tight_layout()

            # Display the bar chart in Streamlit
            st.pyplot(fig)
            #---------------------------------------------------------------------------------------------------#

            # # Get the unique years from the DataFrame
            unique_years = sorted(tag_df['year'].unique(), reverse=True)

            st.subheader('Select a year below for the Word Cloud of tags associated with the movies released in that year.')

            # Ask the user to select a year from the available options
            selected_year = st.selectbox("Select a year:", unique_years)

            # Filter the DataFrame to get the tags for the selected year
            selected_tags = tag_df[tag_df['year'] == selected_year]['tag']

            # Combine all the tags into a single string
            tags_text = " ".join(selected_tags)

            # Create a WordCloud based on the combined tags text
            wordcloud = WordCloud(width=900, height=500, background_color='black').generate(tags_text)

            # Display the WordCloud using Streamlit
            st.title(f"Word Cloud for Movies in {selected_year}")
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)

    if page_selection == "Contact Us":
                # Define the company details
        company_name = "DATAMIN"
        company_address = "123 Street, Johannesburg, South Africa"
        company_phone = "+27 11 555 6666"
        company_email = "datamin@data.com"

        # Display the company details in smaller boxes
        st.subheader("Company Details")
        st.info(f"Name: {company_name}")
        st.info(f"Address: {company_address}")
        st.info(f"Phone: {company_phone}")
        st.info(f"Email: {company_email}")

        # Create a form for user inquiries
        st.subheader("Inquiry Form")
        name = st.text_input("Your Email")
        inquiry = st.text_area("Your Inquiry")
        submit_button = st.button("Submit")

        # Store the user's inquiry in a database or file
        if submit_button:
            # Store the user's name and inquiry somewhere (e.g., database, file)
            # You can add your own code here to handle the storage
            st.success("Inquiry submitted successfully!")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
