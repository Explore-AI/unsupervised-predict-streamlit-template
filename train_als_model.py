# Importing the ALS model
import pandas as pd
import numpy as np
import pickle
from surprise import SVD, Reader, Dataset

def train_als_model():
    # Load the ratings data
    ratings = pd.read_csv('resources/data/ratings.csv')
    # Create a Surprise reader
    reader = Reader(rating_scale=(0.5, 5))
    # Load the data into Surprise Dataset
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    # Build the trainset
    trainset = data.build_full_trainset()
    # Instantiate the ALS model
    als_model = SVD(n_factors=200, n_epochs=40, lr_all=0.005, reg_all=0.02)
    # Train the model on the data
    als_model.fit(trainset)
    # Save the model
    pickle.dump(als_model, open('resources/models/ALS_model.pkl', 'wb'))

if __name__ == '__main__':
    train_als_model()
