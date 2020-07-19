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
import re
from PIL import Image
#Plots
import seaborn as sns
import matplotlib.style as style 
sns.set(font_scale=1)
import matplotlib.pyplot as plt
from datetime import date
#import plotly.figure_factory as ff

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

data_path = '../unsupervised_data/unsupervised_movie_data/'
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System",'Exploratory Data Analysis',"Solution Overview","About us"]

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
    if page_selection == 'Exploratory Data Analysis':

        st.subheader('EDA') 
        drop_down_listings = st.selectbox('select_otions',['What\'s in a genre?','Greatest Hits','1 more plot','too many?'])
        if drop_down_listings == 'What\'s in a genre?':
            genres_setlist = ['Action','Adventure','Animation',
                              'Children','Comedy',
                              'Crime','Documentary',
                              'Drama','Fantasy','Horror','Mystery',
                              'Romance','Sci-fi',
                              'Thriller','War','Western']
            genres = st.multiselect('Pick your favourie genre(s) for some fun facts',genres_setlist)
#        st.write(genres)
            if len(genres) > 0:
                def genre_count(filename,list1):
                    '''Plots the distribution of genres in the movies dataset'''
                    filename = data_path+str(filename)
                    chunks = pd.read_csv(filename,chunksize=10000)
                    data = pd.DataFrame()
                    count = 0
                    dict_genres = {}
                    for chunk in chunks:
                        chunk_genres = ','.join([genres.replace('|',',') for genres in chunk.genres]).split(',')
                        chunk_genres = [item for item in chunk_genres if item in list1]
                        for genre in chunk_genres:
                            if genre in dict_genres:
                                dict_genres[genre]+=1
                            else:
                                dict_genres[genre]=1
                    sorted_dict = sorted(dict_genres.items(), key=lambda x: x[1],reverse=True)
                    genre, frequency = zip(*sorted_dict)
                    plt.figure(figsize=(10,5))
                    freq_plot = sns.barplot(x = frequency,y = list(genre),palette='pastel')
                    freq_plot.set(title='Number of movies in genre',
                                  xlabel='Genre_count',ylabel='Genre')
                    plt.show()
                    return (freq_plot)
                genre_count_figure = genre_count('movies.csv',genres).figure
                if st.checkbox('show genre counts in dataset'):
                    st.write(genre_count_figure)
        
        if drop_down_listings == 'Greatest Hits':
            # Movie Titles List:
            titles = ['The Shawshank Redemption','Pulp Fiction','Forrest Gump','The Silence of The Lambs',
                      'The MATRIX','Star Wars: Episode IV - A New Hope','Schindler\'s List','Fight Club',
                      'Star Wars: Episode V - The empire Strikes Back','Braveheart','The Usual Suspects',
                      'Jurassic Park','Terminator 2: Judgment Day','The Lord of The Rings (TFOTR)','Raisers of The Lost Ark']
            #Images List
            images = ['resources/imgs/thumbnails/shawshank_redemption.png','resources/imgs/thumbnails/pulp_fiction.png',
                      'resources/imgs/thumbnails/forest_gump.png','resources/imgs/thumbnails/silence_of_the_lambs.png',
                      'resources/imgs/thumbnails/the_matrix.png','resources/imgs/thumbnails/star_wars.png',
                      'resources/imgs/thumbnails/schindlers_list.png','resources/imgs/thumbnails/fight_club.png',
                      'resources/imgs/thumbnails/star_wars_2.png','resources/imgs/thumbnails/braveheart.png',
                      'resources/imgs/thumbnails/the_usual_suspects.png','resources/imgs/thumbnails/jurassic_park.png',
                      'resources/imgs/thumbnails/terminator_2.png','resources/imgs/thumbnails/LOTR_FLOTR.png',
                      'resources/imgs/thumbnails/raiders_of_lost_ark.png']
            descriptions = ['Realese year:1994  \n Genre: Drama  \nRealese year:1994  \nRuntime: 2h 22min  \nAverage rating: 4.4  \nNumber of ratings: 32831  \nStoryline:  \nChronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man\'s unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red.',
                            'Release year: 1994  \nGenre: Comedy, Crime  \nRuntime: 2h.58min  \nRatings: 4.2  \nNumber of Ratings: 31697  \nStoryline:  \nJules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hit men who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising a series of funny, bizarre and uncalled-for incidents.',
                            'Release year: 1994  \nGenre: Drama, Romance  \nRuntime: 2h.22min  \nRatings: 4.1  \nNumber of Ratings: 32383  \nStoryline:  \nForrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny. His \'mama\' teaches him the ways of life and leaves him to choose his destiny. Forrest joins the army for service in Vietnam, finding new friends called Dan and Bubba, he wins medals, creates a famous shrimp fishing fleet, inspires people to jog, starts a ping-pong craze, creates the smiley, writes bumper stickers and songs, donates to people and meets the president several times. However, this is all irrelevant to Forrest who can only think of his childhood sweetheart Jenny Curran, who has messed up her life. Although in the end all he wants to prove is that anyone can love anyone.',
                            'Release year:  1991  \nGenre: Crime, Drama, Thriller  \nRuntime: 1h.58min  \nRatings: 4.2  \nNumber of Ratings: 29444  \nStoryline:  \nF.B.I. trainee Clarice Starling (Jodie Foster) works hard to advance her career, while trying to hide or put behind her West Virginia roots, of which if some knew, would automatically classify her as being backward or white trash. After graduation, she aspires to work in the agency\'s Behavioral Science Unit under the leadership of Jack Crawford (Scott Glenn). While she is still a trainee, Crawford asks her to question Dr. Hannibal Lecter (Sir Anthony Hopkins), a psychiatrist imprisoned, thus far, for eight years in maximum security isolation for being a serial killer who cannibalized his victims. Clarice is able to figure out the assignment is to pick Lecter\'s brains to help them solve another serial murder case, that of someone coined by the media as "Buffalo Bill" (Ted Levine), who has so far killed five victims, all located in the eastern U.S.',
                            'Release year: 1999  \nGenre: Action, Sci-Fi  \nRuntime: 2h.16min  \nRatings: 4.2  \nNumber of Ratings: 29014  \nStoryline:  \nThomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. As a rebel against the machines, Neo must confront the agents: super-powerful computer programs devoted to stopping Neo and the entire human rebellion.',
                            'Release year: 1977  \nGenre: Action, Adventure, Fantasy  \nRuntime: 2h.1min  \nRatings: 4.2  \nNumber of Ratings: 27560  \nStoryline:  \nThe Imperial Forces, under orders from cruel Darth Vader, hold Princess Leia hostage in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker and Han Solo, captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 and C-3PO to rescue the beautiful princess, help the Rebel Alliance and restore freedom and justice to the Galaxy.',
                            'Release year: 1993  \nGenre: Biography, Drama, History  \nRuntime: 3h.15min  \nRatings: 4.2  \nNumber of Ratings: 24004  \nStoryline:  \nOskar Schindler is a vain and greedy German businessman who becomes an unlikely humanitarian amid the barbaric German Nazi reign when he feels compelled to turn his factory into a refuge for Jews. Based on the true story of Oskar Schindler who managed to save about 1100 Jews from being gassed at the Auschwitz concentration camp, it is a testament to the good in all of us.',
                            'Release year: 1999  \nGenre: Drama  \nRuntime: 2h.19min  \nRatings: 4.2  \nNumber of Ratings: 23536  \nStoryline:  \nA nameless first person narrator (Edward Norton) attends support groups in an attempt to subdue his emotional state and relieve his insomniac state. When he meets Marla (Helena Bonham Carter), another fake attendee of support groups, his life seems to become a little more bearable. However when he associates himself with Tyler (Brad Pitt) he is dragged into an underground fight club and soap making scheme. Together the two men spiral out of control and engage in competitive rivalry for love and power. When the narrator is exposed to the hidden agenda of Tyler\'s fight club, he must accept the awful truth that Tyler may not be who he says he is.',
                            'Release year: 1980  \nGenre:  Action, Adventure, Fantasy  \nRuntime: 2h.4min  \nRatings: 4.2  \nNumber of Ratings: 22956  \nStoryline:  \nLuke Skywalker, Han Solo, Princess Leia and Chewbacca face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth. While Han and Leia escape in the Millennium Falcon, Luke travels to Dagobah in search of Yoda. Only with the Jedi Master\'s help will Luke survive when the Dark Side of the Force beckons him into the ultimate duel with Darth Vader.',
                            'Release year: 1995  \nGenre: Biography, Drama, History  \nRuntime: 2h.58min  \nRatings: 4.0  \nNumber of Ratings: 23722  \nStoryline:  \nWilliam Wallace is a Scottish rebel who leads an uprising against the cruel English ruler Edward the Longshanks, who wishes to inherit the crown of Scotland for himself. When he was a young boy, William Wallace\'s father and brother, along with many others, lost their lives trying to free Scotland. Once he loses another of his loved ones, William Wallace begins his long quest to make Scotland free once and for all, along with the assistance of Robert the Bruce.',
                            'Release year: 1995  \nGenre: Crime, Mystery, Thriller  \nRuntime: 1h.46min  \nRatings: 4.3  \nNumber of Ratings: 22032  \nStoryline:  \nFollowing a truck hijack in New York, five criminals are arrested and brought together for questioning. As none of them are guilty, they plan a revenge operation against the police. The operation goes well, but then the influence of a legendary mastermind criminal called Keyser Söze is felt. It becomes clear that each one of them has wronged Söze at some point and must pay back now. The payback job leaves 27 men dead in a boat explosion, but the real question arises now: Who actually is Keyser Söze?',
                            'Release year: 1993  \nGenre: Action, Advecture, Sci-Fi  \nRuntime: 2h.7min  \nRatings: 3.7  \nNumber of Ratings: 25518  \nStoryline:  \nHuge advancements in scientific technology have enabled a mogul to create an island full of living dinosaurs. John Hammond has invited four individuals, along with his two grandchildren, to join him at Jurassic Park. But will everything go according to plan? A park employee attempts to steal dinosaur embryos, critical security systems are shut down and it now becomes a race for survival with dinosaurs roaming freely over the island.',
                            'Release year: 1991  \nGenre: Action, Sci-Fi  \nRuntime: 2h.17min  \nRatings: 4.0  \nNumber of Ratings: 23075  \nStoryline:  \nOver 10 years have passed since the first machine called The Terminator tried to kill Sarah Connor and her unborn son, John. The man who will become the future leader of the human resistance against the Machines is now a healthy young boy. However, another Terminator, called the T-1000, is sent back through time by the supercomputer Skynet. This new Terminator is more advanced and more powerful than its predecessor and it\'s mission is to kill John Connor when he\'s still a child. However, Sarah and John do not have to face the threat of the T-1000 alone. Another Terminator (identical to the same model that tried and failed to kill Sarah Conner in 1984) is also sent back through time to protect them. Now, the battle for tomorrow has begun.',
                            'Release year: 2001  \nGenre: Action, Adventure, Drama  \nRuntime: 2h.58min  \nRatings: 4.1  \nNumber of Ratings: 22216  \nStoryline:  \nAn ancient Ring thought lost for centuries has been found, and through a strange twist of fate has been given to a small Hobbit named Frodo. When Gandalf discovers the Ring is in fact the One Ring of the Dark Lord Sauron, Frodo must make an epic quest to the Cracks of Doom in order to destroy it. However, he does not go alone. He is joined by Gandalf, Legolas the elf, Gimli the Dwarf, Aragorn, Boromir, and his three Hobbit friends Merry, Pippin, and Samwise. Through mountains, snow, darkness, forests, rivers and plains, facing evil and danger at every corner the Fellowship of the Ring must go. Their quest to destroy the One Ring is the only hope for the end of the Dark Lords reign.',
                            'Release year: 1981  \nGenre: Action, Adventure  \nRuntime: 1h.55m  \nRatings: 4.1  \nNumber of Ratings: 21982  \nStoryline:  \nThe year is 1936. An archeology professor named Indiana Jones is venturing in the jungles of South America searching for a golden statue. Unfortunately, he sets off a deadly trap but miraculously escapes. Then, Jones hears from a museum curator named Marcus Brody about a biblical artifact called The Ark of the Covenant, which can hold the key to humanely existence. Jones has to venture to vast places such as Nepal and Egypt to find this artifact. However, he will have to fight his enemy Rene Belloq and a band of Nazis in order to reach it.'
            ]
            
            #Next Button
            button = 'button' #Initialise program only
            def next_prev(button):
                next_counter = pd.read_csv('resources/imgs/thumbnails/next_button.csv')['value']
                next_value = next_counter[0]
                if button == 'next':
                    if next_value >= 14:
                        next_value = 0
                    else:
                        next_value = next_value + 1
                    next_counter[0] = next_value
                    next_counter.to_csv('resources/imgs/thumbnails/next_button.csv')
                if button == 'previous':
                    if next_value < 1:
                        next_value = 14
                    else:
                        next_value = next_value - 1
                    next_counter[0] = next_value
                    next_counter.to_csv('resources/imgs/thumbnails/next_button.csv')
                return(next_value)
            st.subheader('{}. {}'.format(next_prev(button)+1,titles[next_prev(button)]))
            st.image(images[next_prev(button)],width=100)
            st.markdown(descriptions[next_prev(button)])
            if st.button('next'):
                next_prev('next')
            if st.button('previous'):
                next_prev('previous')

        if drop_down_listings =='1 more plot':
        current_year=date.today().year
        min_year = 1970
        add_slider = st.slider('Choose year range:',min_year, current_year,(min_year,current_year), step=1)
        if st.button('View highest rated in time frame'):
            def average_by_year(filename):
                a = add_slider[0]
                b = add_slider[1]
                counter = 0
                data_f1 = pd.DataFrame()
                data = pd.DataFrame()
                chunks_1 = pd.read_csv('../unsupervised_data/unsupervised_movie_data/movies.csv',chunksize=50000)
                for chunk in chunks_1:
                    chunk['release_year'] = chunk.title.map(lambda x: re.findall('\d\d\d\d',x))
                    chunk.release_year = chunk.release_year.apply(lambda x: np.nan if not x else int(x[-1]))
                    chunk = chunk[(chunk['release_year']>=a)&(chunk['release_year']<b+1)].drop(['genres'],axis=1)
                    data_f1 = pd.concat([chunk,data_f1])
                id_in_movies = data_f1.movieId
                
                chunks_2 = pd.read_csv('../unsupervised_data/unsupervised_movie_data/train.csv',chunksize=50000)
                for chunk in chunks_2:
                    identical = chunk[chunk['movieId'].isin(id_in_movies)].drop(['userId','timestamp'],axis=1)
                    data = pd.concat([identical,data])
                def top_movies_list(df=data):
                    m = df.movieId.value_counts().quantile(0.8)
                    vote_count = df.movieId.value_counts()
                    average_ratings = df.groupby(['movieId']).rating.mean()
                    C = average_ratings.mean() #average rating of a movie
                    q_movies = df.movieId.unique()
                    unique_val_counts = df.movieId.value_counts()
                    q_movies = [row for row in q_movies if unique_val_counts[row]>m]
                    def weighted_rating(movie_id,m=m,C=C):
                        v = vote_count[movie_id]
                        R = average_ratings[movie_id]
                        weighted_score = (v*R/(v+m))+(m*C/(v+m))
                        return(round(weighted_score,2))
                    def Top_N_Recommendations(movies_list=q_movies):
                        weighted_scores = [weighted_rating(movie_id) for movie_id in movies_list]
                        trending_df = pd.DataFrame({'movieId':movies_list,'IMDB_score':weighted_scores})
                        trending_df = trending_df.sort_values('IMDB_score',ascending=False)
                        trending_df = trending_df.merge(data_f1, on=['movieId'],how = 'inner')
                        return(trending_df)
                    trending_df = Top_N_Recommendations(movies_list=q_movies)
                    trending_df.index = np.arange(1, len(trending_df) + 1)
                    return(trending_df.head(10)[['title','release_year','IMDB_score']])
                return(top_movies_list())
            with st.spinner('Let\'s look back shall we...'):
                st.table(average_by_year(0))

        if drop_down_listings =='too many?':
            value = st.text_input('Movie title', 'Search film title')
            actor = st.text_input('Actor or producer:','')
            indexes = []
            count = 0
            chunksize = 100000
            chunks = [title_list[x:x+chunksize] for x in range(0, len(title_list), chunksize)]
            for chunk in chunks:
                for index,title in enumerate(chunk):
                    if value.lower() in title.lower():
                        indexes.append(count+index)
                    else:
                        pass
                count += chunksize
                options = np.array(title_list)[indexes]
            actors_and_dir = pd.DataFrame()
            for chunk_imdb in pd.read_csv('../unsupervised_data/unsupervised_movie_data/imdb_data.csv',chunksize=100000):
                chunk = chunk_imdb[(chunk_imdb.title_cast.map(lambda x: actor.lower() in str(x).lower())|chunk_imdb.director.map(lambda x: actor.lower() in str(x).lower()))]
                actors_and_dir = pd.concat([chunk,actors_and_dir],axis=1)
            actors_and_dir = actors_and_dir[['movieId']]
            for chunk in pd.read_csv('resources/data/movies.csv',chunksize=100000):
                actors_and_dir = actors_and_dir.merge(chunk,on='movieId',how='left')
            if len(value)==0 and len(actor)==0:
                options = 'Pick a value'
            if len(value)==0 and len(actor) > 0:
                options = [title for title in actors_and_dir.title]
            if len(value)>0 and len(actor)>0:
                options = [title for title in actors_and_dir.title if title in options]
            value = st.selectbox("title", options)
            if st.button('view ratings'):
                def movieId(filename):
                    chunks = pd.read_csv(filename,chunksize=10000)
                    for chunk in chunks:
                        chunk.title = chunk.title.apply(lambda x: str(x).lower())
                        if len(chunk[chunk.title==value.lower()]):
                            return(chunk[chunk.title==value.lower()])
                selid = movieId('resources/data/movies.csv').movieId.values[0]
                def rate(filename):
                    chunks = pd.read_csv(filename,chunksize=50000)
                    data = pd.DataFrame()
                    for chunk in chunks:
                        chunk = chunk[chunk['movieId']==selid][['movieId','rating']]
                        data = pd.concat([chunk,data])
                    data = data.rating.value_counts()
                    data = data*100/data.sum()
                    fig = plt.figure(figsize=(25,10))
                    ax = fig.add_subplot(111)
                    labels = [str(round(index,2))+' stars' for index in data.index]
                    theme = plt.get_cmap('Reds')
                    ax.set_prop_cycle("color", [theme(1. * i / len(labels)) for i in range(len(labels))])
                    sns.set(font_scale=2)
                    pie = ax.pie(data,autopct='%1.1f%%',shadow=True,
                                 startangle=10,pctdistance=1.115,
                                 explode = tuple([0.1 for i in range(len(labels))]))
                    centre_circle = plt.Circle((0,0),0.70,fc='white')
                    fig = plt.gcf()
                    fig.gca().add_artist(centre_circle)
                    plt.legend(pie[0], labels, loc="lower left")
                    ax.set_title(f'Rating distribution for {value}', fontsize=35)
                    plt.tight_layout()
                    plt.show()
                    return(ax.figure)
                st.write(rate('../unsupervised_data/unsupervised_movie_data/train.csv'))
    if page_selection == "Solution Overview":
        #st.title("Solution Overview")
        #st.write("Describe your winning approach on this page")
        sol_page = """
                    <div class="w3-light-grey w3-padding-64 w3-margin-bottom w3-center">
                    <h1 class="w3-jumbo">Solution Overview</h1>
                    </div>
​
                    <div class="w3-row-padding w3-content" style="max-width:1400px">
                    <div class="w3-twothird">
                    <img src="https://trello-attachments.s3.amazonaws.com/5f03a5ce9c3e440f72126d34/500x434/52d0ca01f0acd3d463ed9c23b7a2b18b/netflix-because-you-watched-rick-and-morty-theory-every-thing-28570667.png" alt="Notebook" style="width:100%">
                    <div class="w3-justify">
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                    </div>
                    <div class="w3-third">
                    <div class="w3-container w3-light-grey">
                    <h2>Very New News!</h2>
                    <p class="w3-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                    <br>
                    <div class="w3-container w3-light-grey w3-justify">
                    <h2>Recommender Systems</h2>
                    <p class="w3-justify"><b>Content-based recommenders:</b> suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person likes a particular item, he or she will also like an item that is similar to it.</p>
                    <p class="w3-justify"><b>Collaborative filtering engines:</b> these systems are widely used, and they try to predict the rating or preference that a user would give an item-based on past ratings and preferences of other users. Collaborative filters do not require item metadata like its content-based counterparts.</p>
                    </div>
                    </div>
                    </div>
                    """
        st.markdown(sol_page, unsafe_allow_html=True)
    
    if page_selection == "About us":
        the_team = """
                    <h1 style="color:black;padding-bottom: 15px"><b>Meet the team that made it happen</b></h1>
                    <!-----------One Member--------------->
                    <div style="overflow: auto;background-color: #f0f2f6;border-radius: 5px;margin: auto;width: 100%;padding: 10px;">
                    <img style="float: left;padding-right: 15px;border-radius: 2.5px" src="https://www.w3schools.com/howto/img_avatar.png" alt="Pineapple" width="170" height="170">
                    <h3 style="margin-bottom: 2px">Nicole Meinie</h3>
                    <p style="">Project Manager</p>
                    <ul>
                    <li style="display:inline;">
                    <a href="www.linkedin.com/in/nicole-meinie/"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
                    </li>
                    <li style="display:inline;">
                    <a href="https://github.com/NicoleMeinie"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
                    </li>
                    </ul>
                    </div>
                    <!-----------One Member--------------->
                    <div style="overflow: auto;background-color: #f0f2f6;border-radius: 5px;margin: auto;width: 100%;padding: 10px;">
                    <img style="float: left;padding-right: 15px;border-radius: 2.5px" src="https://media-exp1.licdn.com/dms/image/C5603AQHcTe4c3SNhdA/profile-displayphoto-shrink_800_800/0?e=1600300800&v=beta&t=wlzH7LmLPCnoO5b1LagSO9lr4WyDFCfWfIBcR0MuZUs" alt="Pineapple" width="170" height="170">
                    <h3 style="margin-bottom: 2px">Marcio Maluka</h3>
                    <p style="">Tech Lead</p>
                    <ul>
                    <li style="display:inline;">
                    <a href="linkedin.com/in/marcio-maluka-74b4065a"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
                    </li>
                    <li style="display:inline;">
                    <a href="https://github.com/xmaluka"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
                    </li>
                    </ul>
                    </div>
                    <!-----------One Member--------------->
                    <div style="overflow: auto;background-color: #f0f2f6;border-radius: 5px;margin: auto;width: 100%;padding: 10px;">
                    <img style="float: left;padding-right: 10px;border-radius: 2.5px" src="https://media-exp1.licdn.com/dms/image/C4E03AQFvPi_4_Kd6tA/profile-displayphoto-shrink_800_800/0?e=1600300800&v=beta&t=cVHjEqDL_hzLxHgiSEBVob8I2kQ_CGdATmorzaanQFI" alt="Pineapple" width="170" height="170">
                    <h3 style="margin-bottom: 2px">Phiwayinkosi Hlatshwayo</h3>
                    <p style="">Data Scientist</p>
                    <ul>
                    <li style="display:inline;">
                    <a href="https://www.linkedin.com/in/phiwayinkosi-hlatshwayo-03027b130/"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
                    </li>
                    <li style="display:inline;">
                    <a href="https://github.com/phiwa-lab"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
                    </li>
                    </ul>
                    </div>
                    <!-----------One Member--------------->
                    <div style="overflow: auto;background-color: #f0f2f6;border-radius: 5px;margin: auto;width: 100%;padding: 10px;">
                    <img style="float: left;padding-right: 15px;border-radius: 2.5px" src="https://avatars0.githubusercontent.com/u/60364030?s=400&u=b1b36e92c09ad91e06ff145924ad8b5457639ccd&v=4" alt="Pineapple" width="170" height="170">
                    <h3 style="margin-bottom: 2px">Karabo Leso</h3>
                    <p style="">Data Engineer</p>
                    <ul>
                    <li style="display:inline;">
                    <a href="https://www.linkedin.com/in/karabo-leso-191a01189/"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
                    </li>
                    <li style="display:inline;">
                    <a href="https://github.com/KaraboLeso"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
                    </li>
                    </ul>
                    </div>
                    <!-----------One Member--------------->
                    <div style="overflow: auto;background-color: #f0f2f6;border-radius: 5px;margin: auto;width: 100%;padding: 10px;">
                    <img style="float: left;padding-right: 15px;border-radius: 2.5px" src="https://www.w3schools.com/howto/img_avatar.png" alt="Pineapple" width="170" height="170">
                    <h3 style="margin-bottom: 2px">Noah Kaekae</h3>
                    <p style="">Software Developer</p>
                    <ul>
                    <li style="display:inline;">
                    <a href="#"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
                    </li>
                    <li style="display:inline;">
                    <a href="#"><img border="0" alt="Github" src="https://image.flaticon.com/icons/svg/25/25231.svg" width="25" height="25"></a>
                    </li>
                    </ul>
                    </div>
                    """
        st.markdown(the_team, unsafe_allow_html=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()