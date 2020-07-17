"""

    Collaborative-based filtering for item recommendation.

    Author: TEAM_1_DBN.

    Description: Collaborative filtering algorithm for rating predictions on 
                 Movie data.

"""

# Script dependencies
import pandas as pd
import bz2
import _pickle as cPickle
import surprise as surp

# Pickle loading function

def decompress_pickle(file):
    data_b = bz2.BZ2File(file, 'rb')
    data_b = cPickle.load(data_b)
    return data_b

# Importing data from S3 Bucket

model = decompress_pickle('/home/explore-student/c_model.pbz2')

df_movie = pd.read_csv('/home/explore-student/unsupervised_data/unsupervised_movie_data/movies.csv',sep = ',',delimiter=',')
df_rating = pd.read_csv('/home/explore-student/unsupervised_data/unsupervised_movie_data/train.csv')

#-----------------------------#
# Class to pre-process data #

class CFData:
    def __init__(self, df_rating, test_ratio=None, df_id_name_table=None, rating_scale=(1, 5)):
            """
            Initialize collaborative filtering data class
            :param df_rating: pandas dataframe containing columns: 'userID', 'itemID', 'rating' in correct order
            :param df_id_name_table: table to convert itemID to readable item name (like movie title). 
                                     dataframe containg columns: 'itemID' and 'itemName' in correct order
            :return: None
            Eg: 
                df_id_name_table = df_movie[['movieId', 'title']].\
                    rename(index=str, columns={'movieID':'itemID', 'title':'itemName'})
                cfdata_example = CFData(data, df_id_name_table)
                cfdata_example.convert_name_to_id('Toy Story (1995)')
                cfdata_example.convert_id_to_name(1)
            """      
            reader = surp.Reader(rating_scale=rating_scale)
            rating_data = surp.Dataset.load_from_df(df_rating, reader)
            self.trainset = rating_data.build_full_trainset()
      
            if test_ratio is not None:
                self.trainset, self.testset = surp.model_selection.train_test_split(data=rating_data, test_size=test_ratio)
            else:
                self.trainset = rating_data.build_full_trainset()
    
            # self.__dict_id_to_name: id_1: [name1_1, name1_2...], id_2: [name2_1, name2_2....]
            # self.__dict_name_to_id: name1: [id1_1, id1_2...], name2: [id2_1, id2_2...]
            if df_id_name_table is not None:
                self.__dict_id_to_name = df_id_name_table.groupby('itemID')['itemName'].apply(lambda x: x.tolist()).to_dict()
                self.__dict_name_to_id = df_id_name_table.groupby('itemName')['itemID'].apply(lambda x: x.tolist()).to_dict()
                  
    def convert_name_to_id(self, item_name):
        """
        Convert item name to item id
        :param item_name: item name
        :return: item id if single id is found
                 None if nothing or multiple id's are found
        """  
        if item_name not in self.__dict_name_to_id or len(self.__dict_name_to_id[item_name]) > 1:
            return None
        return self.__dict_name_to_id[item_name][0]
        
    def convert_id_to_name(self, item_id):
        """
        Convert item id to item name
        :param item_id: item id
        :return: item name if single name is found
                 None if nothing or multiple id's are found
        """
        if item_id not in self.__dict_id_to_name or len(self.__dict_id_to_name[item_id]) > 1:
            return None
        return self.__dict_id_to_name[item_id][0]


#-----------------------------#
# Load rating data to CFData class #

df_data = df_rating[['userId','movieId', 'rating',]]
df_data = df_data.rename(index=str, columns={'userId': 'userID', 'movieId': 'itemID', 'rating': 'rating'})
df_id_name_table = df_movie[['movieId', 'title']]
df_id_name_table = df_id_name_table.rename(index=str, columns={'movieId':'itemID', 'title':'itemName'})
data_movie = CFData(df_data, test_ratio=None, df_id_name_table=df_id_name_table, rating_scale=(0.5, 5))

#-----------------------------#
# Helper Functions #

def get_most_rated_movie(df_movie_in, df_rating_in, n_output):
    movie_list_tmp1 = pd.merge(df_movie, df_rating, on='movieId', how='inner').groupby('title').count()   
    movie_list_top_k = movie_list_tmp1['rating'].sort_values(ascending=False).index[:n_output]
    
    return movie_list_top_k

movie_list_top_n = get_most_rated_movie(df_movie, df_rating, 10000)

def get_similar_item(model, input_item_id, num_neighbor):

    # Convert input item_id to inner id generated during training
    input_inner_id = model.trainset.to_inner_iid(input_item_id)

    # 'sim' method is used to execute get_neighbors like KNN method

    if 'sim' in dir(model):
        # get a list of inner_id. Need to convert to item_id
        neighbor_inner_id = model.get_neighbors(input_inner_id, k=num_neighbor) 

        return [model.trainset.to_raw_iid(inner_id) for inner_id in neighbor_inner_id]
    else:
        return __get_top_similarities(input_inner_id, num_neighbor)
            

def __get_top_similarities(item_inner_id, k):

    # Get TOP-k similar item for matix factorization model
    
    from math import sqrt
    def cosine_distance(vector_a, vector_b):
        ab = sum([i*j for (i, j) in zip(vector_a, vector_b)])
        a2 = sum([i*i for i in vector_a])
        b2 = sum([i*i for i in vector_b])
        eta = 1./10**9
        return 1.0 - ab/sqrt((a2+eta)*(b2+eta))

    # obtain the vector representation of input item
    item_vector = model.qi[item_inner_id]
    similarity_table = []

    for other_inner_id in model.trainset.all_items():
        if other_inner_id == item_inner_id:
            continue
        other_item_vector = model.qi[other_inner_id]
        similarity_table.append((cosine_distance(other_item_vector, item_vector), 
                                 model.trainset.to_raw_iid(other_inner_id)
                                )) 
    similarity_table.sort()
    if k > len(similarity_table):
        return [i[1] for i in similarity_table]
    else:
        return [i[1] for i in similarity_table[0:k]]

#-----------------------------#
    

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
    
    # Movie names to id
    
    new_movie_ids = []
    for i in movie_list :
        the_name = data_movie.convert_name_to_id(i)
        new_movie_ids.append(the_name)
    
    def show_recommended_movies(movie_name, k=10): 
        
    # Convert user-selected movie name to movie id then obtain the top-k similar movies
        movie_item_id = data_movie.convert_name_to_id(movie_name)
        movie_neighbor_name = [data_movie.convert_id_to_name(i) for i in get_similar_item(model,movie_item_id, k) if i not in new_movie_ids]
   
        return movie_neighbor_name
    
    r_1 = show_recommended_movies(movie_list[0], k=4)
    r_2 = show_recommended_movies(movie_list[1], k=3)
    r_3 = show_recommended_movies(movie_list[2], k=3)

    master_list = r_1 + r_2 + r_3
    master_list = list(set(master_list))
        
    recommended_movies = master_list[0:10]
    
    return recommended_movies
