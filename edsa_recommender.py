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
    page_options = ["Homepage","Recommender System","Solution Overview","Data & Insights","Diversity Statistics",
                    "Mzansi Movie Magic","Female Directed Films","Diversity in Films","Quote of the Day","Our Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Home":
        st.markdown("# Welcome")

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
    if page_selection == "Solution Overview":
        st.write("# Solution Overview")
        st.write("Collaborative filtering uses the ratings of users with similar taste to make suggestions of future content.")
        st.write("""Matrix Factorisation is a class of Collaborative filtering algorithm that decomposes the user-item ratings matrix into a product of two lower
        dimensionality matrices that each represent users and items in latent space. Matrix R (m x n) is a sparse matrix of ratings where m = the
        number of users, and n = the number of items (movies). Matrix R can be factorised into two matrices, P (m x k) and Q (k x n) where k
        represents k unknown 'latent factors’.""")
        st.write("""These latent factors are hidden or underlying features in the data that account for the user's logic or decision making process in weighting
        factors that contribute to the rating of the item. This could be a genre they like, an actor they don't like, the movie being too long, amazing
        CGI, or bad sound mixing and so on.""")
        st.write("""All these latent features are taken into account when a user rates a movie. By using the known, true user ratings, Stochastic Gradient
        descent is used to find the optimum weightings of the latent features that will most closely approximate the actual rating. The predicted
        rating is equal to the dot product of the user vector and the item vector""")
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/sol_overview.png?raw=true", use_column_width=True)

    if page_selection == "Data & Insights":
        st.write("# Data & Insights")
        st.write("""The Spotlight Movie Recommender System uses the
        MovieLens dataset, maintained by the GroupLens research
        group in the Department of Computer Science and
        Engineering at the University of Minnesota. Additional
        movie content data is sourced from IMDB. Click through to
        view insights""")
        graphs = ["Ratings Distribution", "Top 10 Most Rated Movies", "Top 10 Movies: 5.0 Rating",
                  "Top 10 Movies: 0.5 Rating",
                  "Exploring Genres", "Exploring Title Casts", "Most Rated Directors", "Film Production by Country",
                  "Ratings by Release Year"]

        choice = st.selectbox("Choose graph",graphs)
        if choice == "Ratings Distribution":
            st.write("""The average movie rating is 3.55 with a standard deviation of 1.05.
            15% of ratings are rated as 5.00 & 17% of the ratings are below 2.50.
            The rating score with the highest percentage of observations is 4.0.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/ratingdist.png?raw=true",use_column_width=True)

        if choice == "Top 10 Most Rated Movies":
            st.write("• The most rated movie is the Shawshank Redemption,")
            st.write("""• The visualisation is not indicative of the quality, critical
            acclaim or public reception of the movie, but rather the next
            best approximation of the most popular or most watched
            movies.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/most_rated.png?raw=true",use_column_width=True)

        if choice == "Top 10 Movies: 5.0 Rating":
            st.write("• The most rated movie is the Shawshank Redemption,")
            st.write("""• The top ten movies with the highest number of 5.0 ratings
            contain most of the movies that have the most ratings
            overall.""")
            st.write("• Most of these movies are from 90's")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/high_rated.png?raw=true",use_column_width=True)

        if choice == "Top 10 Movies: 0.5 Rating":
            st.write("""• Three comedy movies starring Jim Carrey ('Dumb & Dumber', 'Ace
            Ventura: When Nature Calls' and 'Ace Venture: Pet Detective') make an
            appearance in the top ten.""")
            st.write("""• 50% of the top ten comprise popular movie franchises: 'Twilight', 'Star
            Wars' and 'The Lord of the Rings'. This indicates that although these
            films are popular with their respective fandoms, lots of people do not
            enjoy them.""")
            st.write("""• Star Wars: A New Hope (1977) appears in the top ten for both Most 5.0
            ratings and and Most 0.5 ratings alluding to the fact that it is one of the
            most watched (rated) movies.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/low_rated.png?raw=true",use_column_width=True)

        if choice == "Exploring Genres":
            st.write("""• As the various films can fall into multiple genres, a
            wordcloud is an appropriate method of visualising the
            most common genres""")
            st.write("""• The most common genres in the data set include
            Drama, Comedy and Action.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/genres.png?raw=true",use_column_width=True)

        if choice == "Exploring Title Casts":
            st.write("""Tom Hanks, Samuel L Jackson, Morgan Freeman and Brad Pitt
            appear frequently overall. A repeating trend is the lack of female
            actresses that appear overall which highlights the gender
            disparity in casting and leading film roles for women in the
            industry.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/cast.png?raw=true",use_column_width=True)

        if choice == "Most Rated Directors":
            st.write("• Quentin Tarantino is the Director with the most film ratings.")
            st.write("""• Unusually, several book authors appear in this visualisation: Michael Chrichton (Jurrassic Park Series), J.R.R.Tolkien
            (The Lord of the Rings Trilogy), Stephen King (The Shining & other books) and Thomas Harris (Hannibal Series. When
            researched, all of these films have directors that differ from the authors of the books they were based on.""")
            st.write("""• The DGA (Director's Guild of America) states that films can only have one credited director, unless directed by an
            established duo (such as the Coen brothers) 6. Even if the authors were bestowed director credits, they would have
            been given assistant director credits.""")
            st.write("""• This points to inconsistencies in the database, as the authors should be replaced with the actual directors of the
            movies.""")
            st.write("""• Ethan Coen and Lily Wachowski are listed as sole directors whilst in reality they work in established 'duo' directorships
            with their siblings and should be listed as 'established duos'.""")
            st.write("""• There is only one female director (Lily Wachowski, co-director of The Matrix) in the top 10. This reflects the current
            lack of gender diversity in the film industry.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/directors.png?raw=true",use_column_width=True)

        if choice == "Film Production by Country":
            st.write("• The majority of films for which a film budget is listed are either produced/filmed or funded in the United States.")
            st.write("""• Films made in China (CNY, Chinese Yuan) and India (INR, Indian Rupee) seem under represented in the data
            (No of films). Both the Chinese and Indian (Bollywood) film industry churn out a sizeable number of movies every
            year (772 & 1986 films in 2016 respectively in comparison to Hollywood's 646 5).""")
            st.write("""• This could be attributed to the Hollywood film industry being much older and therefore having more films, but if
            Bollywood and Chinese films had the same level of inclusivity for just 2016 alone, the no of films for INR and CYN
            would at least hit 2758 collectively.""")
            st.write("""• This speaks to the lack of diversity in films featured in the database. Although these films are in foreign
            languages, they do have subtitles and can gain more exposure if featured in the database and ergo the resultant
            recommender system. It would also attract a more diverse audience and improve user experience for users that
            are interested in foreign films to whatever platform the recommender system is being built for""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/film_curr.png?raw=true", use_column_width=True)

        if choice == "Ratings by Release Year":
            st.write("• The release year of movies in the database ranges from 1888 to 2019.")
            st.write("• Movie ratings range from 0 to a just over 1000 from the year 1888 to 1949.")
            st.write("• An upward trend is noted beyond 1949. This could be due to the wider use of colour negative film in the 1950s.")
            st.write("""• The number of ratings peak at 59600 in the year 1995. Movies produced in the 90's seem to have the most
            ratings. This could attributed to a number of factors:""")
            st.write("• They were released 20-30 years ago and have had more time for people to watch and rate them.")
            st.write("• The movies made in this era are simply, good movies with high 'rewatchability'.")
            st.write("• Popular movies and cult classics from the era are being discovered by younger generations.")
            st.write("""• A downward trend is noted from 1995 onward. This could either be because the data set is incomplete, i.e
            missing movies or ratings for this period, or perhaps less users are rating movies via the MovieLens platform in
            recent years. MovieLens is a web-based recommender system platform that recommends movies for its users to
            watch using collaborative filtering of users' movie ratings and reviews""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/years.png?raw=true", use_column_width=True)

    if page_selection == "Diversity Statistics":
        st.write("# Diversity Statistics")
        st.write("Facts and statistics about diversity in Film")
        st.write("""Click through to explore findings from the Hollywood Diversity Report
            (2019) & USC Annenberg Inclusion Initiative (2018)""")
        stats = ["Gender Diversity","Minority Groups"]
        sel = st.selectbox("Select Statistics",stats)
        if sel == "Gender Diversity":
            st.write("""Metacritic scores show just a slight difference between male directors
            (median 54: average 54.2) and female directors (median 55, average
            55.8).""")
            st.write("""Only 5.1% of Best Director award nominees across the Golden Globes,
            Academy Awards, DGA Awards, and Critics’ Choice Awards were
            women.""")
            st.write("""95.1% of top grossing film directors have been male since 2007.
            Women make up 4.9% with women of colour accounting for <1 %.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/gender.png?raw=true",use_column_width=True)

        if sel == "Minority Groups":
            st.write("""Metacritic scores of directors in 2019 by race are (median 54, average
            54.9) for directors of colour and (median 54, average 54.2) for white
            directors.""")
            st.write("86.4 % of top grossing film directors have been male since 2007.")
            st.write("Directors of colour account for 13.6 %.")
            st.write("""Source: Hollywood Diversity Report (2019) & USC Annenberg Inclusion
            Initiative (2018) )""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/minorities.png?raw=true",use_column_width=True)
    if page_selection == "Mzansi Movie Magic":
        st.write("# Mzansi Movie Magic")
        st.write("""Celebrate modern South African Film. Click to generate a proudly South African Film to check out!""")

        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/mazansi.png?raw=true",use_column_width=True)

    if page_selection == "Female Directed Films":
        st.write("# Female Directed")
        st.write("""Of the top 100 grossing films of 2019, women represented
                only 12% of directors (Center for the Study of Women in
                Television and Film). Only five female director’s have been
                nominated for the Academy Award for Best Director, with
                only one winner. Click below discover a female director with
                a story to tell.""")
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/wom_film.png?raw=true",use_column_width=True)

    if page_selection == "Diversity in Films":
        st.write("# Diversity in Films")
        st.write("""Click below discover a film celebrating the diversity of people!""")

        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/diversity.png?raw=true",use_column_width=True)

    if page_selection == "Quote of the Day":
        st.write("""# Quote of the Day""")
        st.write("""Click below for a quote to inspire you in the fight to be seen and feel represented""")

        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/inspo.png?raw=true",use_column_width=True)






    if page_selection == "Our Team":
        team="""

	<div style="background: #f1f2f6;text-align: center;">
		<div style="max-width: 1500px;margin: auto;padding: 40px;color: #333;overflow: hidden;">
      <h2><b>Meet our Team</b></h2>
      <!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/RNT03793-2%20(2).JPG?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Rohini Jagath</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>Passionate about all things data... but she won't share popcorn at the movies.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/rohini-jagath-2492a156" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/pila.jpg?raw=true">
					<div style="margin: 5px;text-transform: uppercase;">Pilasande Pakkies</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>An enthusiast who loves volleyball more than any sport. A pizza lover.</p></div>
					<div style="margin-top: 6px;">
						<a href="http://www.linkedin.com/in/Pilasande-Pakkies" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/20191130_203409.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Tumisang Sentle</div>
					<div style="font-style: italic;color: #3498db;">Web Developer</div>
					<div style=";color: #f63366;"><p>A math addict. He loves listening to debates but he can't debate.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/tumisang-sentle-53100a1a5/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/60532fb212cb493f8fc0c629ef61aa1b.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Refentse Motlogelwa</div>
					<div style="font-style: italic;color: #3498db;">Data Engineer</div>
					<div style=";color: #f63366;"><p>A lover of life with good statistics background. He is also a great DJ.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/ramotse-motlogelwa-8a09358b" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C5603AQEtkA_hyaeciA/profile-displayphoto-shrink_800_800/0?e=1600300800&v=beta&t=i2wG9MJ8LyVMEYkssSfzhKKIoCCmruWTIlt92QEFT9U">
					<div style="margin: 5px;text-transform: uppercase;">Philani Mkhize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>A problem is easier when broken into smaller easier problem.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/philani-mkhize-519995149/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/IMG-2211.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Sandile Mkize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>A former side stepper from the rugby field who turned into a data scientist.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/sandile-mkize-2395b4161/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->

                """
        st.markdown(team, unsafe_allow_html=True)
    if page_selection == "Homepage":
        st.write("# Spotlight Movie Recommender")
        st.write("""What are you in the mood for? Fast paced Action, a magical trip into a faraway fantasy land or
                feeling the thrill of the chase as you solve a mystery or save the world with our heroes &
                heroines? Whatever it may be, we have movie recommendations at your fingertips""")
        st.write("""Spotlight is a movie recommender app with a difference. Besides recommending movies based
                on your individual taste and preferences, we aim to direct the ‘spotlight’ on diversity in film. Use
                the Navigation bar on the left to explore movie recommendations, statistics and visualizations
                and discover something new!""")
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/homepage.png?raw=true", use_column_width=True)




if __name__ == '__main__':
    main()
