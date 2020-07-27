"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from compress_pickle import dump, load
import random

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',',delimiter=',')
ratings_df = pd.read_csv('resources/data/train.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

#Top 100 listed movies
TOP_100=['Trainspotting (1996)',
 'Ghost (1990)',
 '2001: A Space Odyssey (1968)',
 'Bourne Identity, The (2002)',
 'Taxi Driver (1976)',
 'Home Alone (1990)',
 'Spider-Man (2002)',
 'Clockwork Orange, A (1971)',
 'Shining, The (1980)',
 'Being John Malkovich (1999)',
 'Minority Report (2002)',
 'Green Mile, The (1999)',
 'Batman Begins (2005)',
 'Twister (1996)',
 'Incredibles, The (2004)',
 'Stargate (1994)',
 'American History X (1998)',
 'Batman Forever (1995)',
 'Babe (1995)',
 'Aliens (1986)',
 "Ocean's Eleven (2001)",
 'Beautiful Mind, A (2001)',
 'Dumb & Dumber (Dumb and Dumber) (1994)',
 'Rock, The (1996)',
 'Ghostbusters (a.k.a. Ghost Busters) (1984)',
 'Star Wars: Episode I - The Phantom Menace (1999)',
 'X-Men (2000)',
 'Goodfellas (1990)',
 'Eternal Sunshine of the Spotless Mind (2004)',
 'Fifth Element, The (1997)',
 'Die Hard: With a Vengeance (1995)',
 'Kill Bill: Vol. 1 (2003)',
 'Truman Show, The (1998)',
 'Léon: The Professional (a.k.a. The Professional) (Léon) (1994)',
 'Godfather: Part II, The (1974)',
 "Amelie (Fabuleux destin d'Amélie Poulain, Le) (2001)",
 'Mrs. Doubtfire (1993)',
 'Monsters, Inc. (2001)',
 'E.T. the Extra-Terrestrial (1982)',
 'Pretty Woman (1990)',
 'Finding Nemo (2003)',
 'Mask, The (1994)',
 'Reservoir Dogs (1992)',
 'Beauty and the Beast (1991)',
 "One Flew Over the Cuckoo's Nest (1975)",
 'Alien (1979)',
 'Blade Runner (1982)',
 'Die Hard (1988)',
 'Mission: Impossible (1996)',
 'Pirates of the Caribbean: The Curse of the Black Pearl (2003)',
 'Titanic (1997)',
 'Groundhog Day (1993)',
 'Ace Ventura: Pet Detective (1994)',
 'Monty Python and the Holy Grail (1975)',
 'Princess Bride, The (1987)',
 'Good Will Hunting (1997)',
 'Indiana Jones and the Last Crusade (1989)',
 'Inception (2010)',
 'Terminator, The (1984)',
 'Men in Black (a.k.a. MIB) (1997)',
 'Memento (2000)',
 'Speed (1994)',
 'Dark Knight, The (2008)',
 'True Lies (1994)',
 'Dances with Wolves (1990)',
 'Shrek (2001)',
 'Lion King, The (1994)',
 'Aladdin (1992)',
 'Batman (1989)',
 'Gladiator (2000)',
 'Sixth Sense, The (1999)',
 'Saving Private Ryan (1998)',
 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)',
 'Fargo (1996)',
 'Apollo 13 (1995)',
 'Independence Day (a.k.a. ID4) (1996)',
 'Back to the Future (1985)',
 'Fugitive, The (1993)',
 'Seven (a.k.a. Se7en) (1995)',
 'Lord of the Rings: The Two Towers, The (2002)',
 'Lord of the Rings: The Return of the King, The (2003)',
 'Godfather, The (1972)',
 'American Beauty (1999)',
 'Star Wars: Episode VI - Return of the Jedi (1983)',
 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)',
 'Usual Suspects, The (1995)',
 'Lord of the Rings: The Fellowship of the Ring, The (2001)',
 'Star Wars: Episode V - The Empire Strikes Back (1980)',
 'Toy Story (1995)',
 'Terminator 2: Judgment Day (1991)',
 'Fight Club (1999)',
 'Braveheart (1995)',
 "Schindler's List (1993)",
 'Jurassic Park (1993)',
 'Star Wars: Episode IV - A New Hope (1977)',
 'Matrix, The (1999)',
 'Silence of the Lambs, The (1991)',
 'Pulp Fiction (1994)',
 'Forrest Gump (1994)',
 'Shawshank Redemption, The (1994)']

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model = load('resources/models/gzip_compressed_data', compression='lzma', set_default_extension=False)

def prediction_item(item_id):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.

    Parameters
    ----------
    item_id : int
        A MovieLens Movie ID.

    Returns
    -------
    list
        User IDs of users with similar high ratings for the given movie.

    """
    # Data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(ratings_df,reader)
    a_train = load_df.build_full_trainset()

    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=item_id,uid=ui, verbose = False))
    return predictions

def pred_movies(movie_list):
    """Maps the given favourite movies selected within the app to corresponding
    users within the MovieLens dataset.

    Parameters
    ----------
    movie_list : list
        Three favourite movies selected by the app user.

    Returns
    -------
    list
        User-ID's of users with similar high ratings for each movie.

    """
    # Store the id of users
    id_store=[]
    # For each movie selected by a user of the app,
    # predict a corresponding user within the dataset with the highest rating
    for i in movie_list:
        predictions = prediction_item(item_id = i)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    # Return a list of user id's
    return id_store

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def collab_model(movie_list,top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """

    try:
        indices = pd.Series(movies_df['title'])
        movie_ids = pred_movies(movie_list)
        df_init_users = ratings_df[ratings_df['userId']==movie_ids[0]]
        for i in movie_ids :
            df_init_users=df_init_users.append(ratings_df[ratings_df['userId']==i])
        # Getting the cosine similarity matrix
        cosine_sim = cosine_similarity(np.array(df_init_users), np.array(df_init_users))
        idx_1 = indices[indices == movie_list[0]].index[0]
        idx_2 = indices[indices == movie_list[1]].index[0]
        idx_3 = indices[indices == movie_list[2]].index[0]
        # Creating a Series with the similarity scores in descending order
        rank_1 = cosine_sim[idx_1]
        rank_2 = cosine_sim[idx_2]
        rank_3 = cosine_sim[idx_3]
        # Calculating the scores
        score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
        score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
        score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
        # Appending the names of movies
        listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
        recommended_movies = []
        # Choose top 50
        top_50_indexes = list(listings.iloc[1:50].index)
        # Removing chosen movies
        top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
        for i in top_indexes[:top_n]:
            recommended_movies.append(list(movies_df['title'])[i])
        return recommended_movies
    except:
        rec_list = []
        for i in range(10):
            rec_list.append(TOP_100[random_ind = random.randint(0,100)])
        return rec_list
