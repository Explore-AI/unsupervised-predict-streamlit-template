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
import requests
from PIL import Image
from streamlit_lottie import st_lottie


# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

movie_image = Image.open(r'resources/imgs/Movies_AI.webp')
logo_a= Image.open(r'resources/imgs/lens.jpeg')

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

# Load your raw data
raw_m = pd.read_csv("resources/data/movies.csv")
raw_r= pd.read_csv("resources/data/ratings.csv")

#load lottie urls
data_lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_8gmx5ktv.json")
info_lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_HhOOsG.json")

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home", "Recommender System","Top Rated Movies", "Solution Overview", "Latest Movie News", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        head, im = st.columns(2)
        head.title('DATA LENS ANALYTICS')
        im.image('resources/imgs/lens.jpeg', caption = 'See the Real-Time World Through our Eyes', width = 125)
        st.write('### Movie Recommender Engine')
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
    if page_selection == 'Home':
		
		
		#define a function to access lottiee files

        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
		
        lottie_coding = load_lottieurl("https://lottie.host/c010cc98-6a3f-479a-a00a-78a84a9c56b5/iHcqx2032P.json")
        phonecall_lottie = load_lottieurl("https://lottie.host/96d1924e-b132-4167-ad2a-fcbfb8918dbd/6TdAaxPO28.json")
        
		# header section
        with st.container():
                
            st.subheader("Welcome :wave:, We are Data Lens Analytics")
            st.image(logo_a, use_column_width=True)
            st.write('---')
            st.title('A Data Science Based Team Focused on Creating Real-World Data-Driven Solutions')
            st.write(""" \n We are passionate about the use of intricately collected and analysed data to allow
			companies and individuals to make well informed decisions""")
		
		#what do we do?
        with st.container():
            st.write('---')
            left_column, right_column = st.columns(2)

            with left_column:
                st.header("What do we do?")
                st.write('##')
                st.markdown(
					"""
					<ul> We create highly trained AI models to clients to increase productivity and overall user experience.
					 <li>  Leveraging available data to analyse trends and usage to be later used in recommendation engines. </li>
					 <li>  Building recommender engines to recommend products and services to users based on well researched data. </li>
                     <li>  Building accurate classification and regression models in relation to current technological standards. </li>
					 <li>  Developing ready to use web-applications for solution deployment. </li>
                     </ul>
					    """
				, unsafe_allow_html= True)
            with right_column:
                st_lottie(lottie_coding, height = 300, key = "coding" )
			
		# This project
        with st.container():
            st.write("---")
            st.header("This Solution")
            st.write("##")

            image_column, text_column = st.columns((1,2))

            with image_column:
			# import the image
                st.image(movie_image)
            with text_column:
                st.subheader("Generate movie predictions on our web application in a few steps")
                st.markdown(
					"""
					<ul> 
					<li>  Pick your favourite movies from a list.
                    <li>  Select a prefered algorithm between a Content or Collaborative based one.
                    <li>  Click on Recommend.
                    <li>  Watch modern magic at work.
                    </ul>
				""", unsafe_allow_html= True)
			
            with st.container():
                st.write('---')
                st.header("Get In Touch With Us")
                st.write("We will get back to you as soon as possible")
                st.write("##")
                contact_form = """
				<form action="https://formsubmit.co/markasavuxx@yahoo.com" method="POST">
     <input type="text" name="message" placeholder = "enter a message" required>
     <input type="email" name="email" placeholder = "enter your email" required>
     <button type="submit">Send</button>
</form>
					"""
                info_column, phonecall_column = st.columns((2,1))

                with info_column:
                    st.markdown(contact_form, unsafe_allow_html=True)   
                
                
                with phonecall_column:
                    st_lottie(phonecall_lottie)

				#styling the contact form
            
            def locall_css(filename):
                with open(filename) as f:
                    st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)
					
                locall_css("style/style.css")    
    
    
    if page_selection == "Top Rated Movies":
        # Header Contents
        st.write("# Top Rated Movies")
        images = ['resources/imgs/info.webp']
        for i in images:
            st.image(i, use_column_width=True)
        filters = ["None", "Top rated Movies"]
        filter_selection = st.selectbox("Fact Check", filters)
        if filter_selection == "Top rated Movies":
            movie_list = pd.read_csv('resources/data/movies.csv')
            ratings = pd.read_csv('resources/data/ratings.csv')
            df = pd.merge(movie_list, ratings, on='movieId', how='left')
            movie_ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
            movie_ratings["Number_Of_Ratings"] = pd.DataFrame(df.groupby('title')['rating'].count())
            indes = movie_ratings.index
            new_list = []
            for movie in indes:
                i = ' '.join(movie.split(' ')[-1])
                new_list.append(i)
            new_lists = []
            for i in new_list:
                if len(i) < 2:
                    empty = i
                    new_lists.append(empty)
                elif i[0] == "(" and i[-1] == ")" and len(i) == 11:
                    R_strip = i.rstrip(i[-1])
                    L_strip = R_strip.lstrip(R_strip[0])
                    spaces = ''.join(L_strip.split())
                    data_type_int = int(spaces)
                    new_lists.append(data_type_int)
                else:
                    new_lists.append(i)
            cnn = []
            for i in new_lists:
                if type(i) != int:
                    i = 0
                    cnn.append(i)
                else:
                    cnn.append(i)
            movie_ratings["Year"] = cnn

            def user_interaction(Year, n):
                list_movies = movie_ratings[movie_ratings['Year'] == Year].sort_values('Number_Of_Ratings',
                                                                                       ascending=False).index
                return list_movies[:n]

            selected_year = st.selectbox("Year released", range(1970, 2020))
            no_of_outputs = st.radio("Movies to view", (5, 10, 20, 50))
            output_list = user_interaction(selected_year, no_of_outputs)
            new_list = []
            for movie in output_list:
                updated_line = ' '.join(movie.split(' ')[:-1])
                updated_line = "+".join(updated_line.split())
                new_list.append(updated_line)
            url = "https://www.imdb.com/search/title/?title="
            movie_links = []
            for i in new_list:
                links = url + i
                movie_links.append(links)
            dict_from_list = dict(zip(output_list, movie_links))
            for items in dict_from_list:
                st.subheader(items)
                

                
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "Latest Movie News":
        st.title("Get The Latest Movie News")
        st.write('---')
		
        st.write("""Stay updated on matters relating to movie releases, actors,
        awards, financing. Never miss an update on upcoming movies and ticket releas dates to
        be the first on at the big screen. Know about your favourite films and movie stars with single click.

		"""
		)
        st.write('##')
        st.image("resources/imgs/news_img.webp", width=600, caption=" Source: https://www.freepik.com/")
        st.write('---')
        st.write("""
		Click the button below to to get a round up of the latest news in Hollywood from around the web.
		 You can proceed to the news source by clicking the provided link to the article
		""")
        btn = st.button("Click to get latest movies related news")

        if btn:
            url ="https://newsapi.org/v2/everything?" 
            request_params = {
		    	"q": 'hollywood OR upcomming movies OR new movies OR hollywood actors',
				"sort by": "latest",
				"language": 'en',
				"apikey": "950fae5906d4465cb25932f4c5e1202c"
			}
            r = requests.get(url, request_params)
            r = r.json()
            articles = r['articles']

            for article in articles:
                st.header(article['title'])
                if article['author']:
                    st.write(f"Author: {article['author']}")
                st.write(f"Source: {article['source']['name']}")
                st.write(article['description'])
                st.write(f"link to article: {article['url']}")
                #st.image(article['urlToImage'])
                
    
    if page_selection == "About Us":
        st.title("About Us")
        st.write("We are a team of Data Scientists and Engineers passionate about building efficient Machine Learning Models")
        st.write("Our goal is to provide accurate movie recommendations so as to provide the ultimate user experience")
        
        st.header("The Team")
        
        #create space for images and their descriptions
        col1, col2, col3 = st.columns(3)
        des1, des2, des3 = st.columns(3)
        col4, col5 = st.columns(2)
        des4, des5 = st.columns(2)
        
        col1.image('resources/imgs/Obinna.jpg', caption = "Data Engineer", width = 200)
        col2.image('resources/imgs/Mark.jpg', caption = "Data Scientist", width = 200)
        col3.image('resources/imgs/Salami.jpg', caption = "Data Scientist", width = 200)
        
        des1.subheader("Obinna Ekesi")
        des1.write("Obinna is our steadfast team leader and experienced data scientist. He has a strong background in Data analytics and Project Management.")

        des2.subheader("Mark Kasavuli")
        des2.write("Mark is an experienced data scientist and app developer. He has a strong background in Data science and Front-End App Development.")
        
        des3.subheader("Oluwaseyi Olanike Rachael")
        des3.write("Oluwaseyi is an experienced Project Coordinator and Data Enginner. She has background knowledge in Project Control and Data analytics.")

        col4.image('resources/imgs/Musa.jpg', caption = "Data Engineer", width = 200)
        col5.image('resources/imgs/Richard.jpg', caption = 'Data Scientist', width = 200)
        
        des4.subheader("Musa Aliu")
        des4.write("Musa is an experienced Data Engineer and pipeline developer. He has vast experience with Exploratory Data Analysis.")
        
        des5.subheader("Richard Sam")
        des5.write("Richard is an experienced Data Scientist. He as a strong background in Machine Learning Model Development and Deployment.")
        
        
        
        
if __name__ == '__main__':
    main()
