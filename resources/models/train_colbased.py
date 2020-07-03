import numpy as np
import pandas as pd
from surprise import SVD
import surprise
import pickle

#importing datasets
ratings = pd.read_csv('ratings.csv')
ratings.drop('timestamp',axis=1,inplace=True)

def svd_pp(save_path):
    # check the range of the rating
    min_rat = ratings['rating'].min()
    max_rat = ratings['rating'].max()
    # changing ratings to their standard form
    reader = surprise.Reader(rating_scale = (min_rat,max_rat))    
    # Loading the data frame using surprice
    data_load = surprise.Dataset.load_from_df(ratings, reader)
    #insatntiating surpricce
    method = SVD(n_factors = 200 , lr_all = 0.005 , reg_all = 0.02 , n_epochs = 40 , init_std_dev = 0.05)
    # loading a trainset into the model
    model = method.fit(data_load.build_full_trainset())
    #print (f"Training completed. Saving model to: {save_path}")
    
    return pickle.dump(model, open(save_path,'wb'))
svd_pp('SVD.pkl')