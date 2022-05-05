# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F2205222%2Fbca114f2e4f6b9b46f2cc76527d7401e%2FImage_header.png?generation=1593773828621598&amp;alt=media" alt="">
# 
# <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQJbAdF6rYFoLf4Msxb9SeGHJgJ8zijnmJ8eRngLxrlieDLeFBcc3NS6epzPj6pVSEFvjW2yxJb8ODk/embed?start=true&loop=true&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
# # Movie Recommendation Challenge
# https://docs.google.com/presentation/d/e/2PACX-1vQJbAdF6rYFoLf4Msxb9SeGHJgJ8zijnmJ8eRngLxrlieDLeFBcc3NS6epzPj6pVSEFvjW2yxJb8ODk/pub?start=true&loop=true&delayms=3000
# ###  1. [Overview](#Overview) 
# - #### [Data](#The-Data)
# 
# ###  2. [EDA](#Exploring-our-data)
# ###  3. [Machine Learning](#Building-the-model)
# - #### Content based filtering
# - #### Collaborative filtering
# 
# ###  4. [Conclusion](#Conclusion)
# - #### [Deployment and future work](#Deployed-App)
# 
# 
# 
# %% [markdown]
# ## Overview
# %% [markdown]
# In today’s technology driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. One application where this is especially true surrounds movie content recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.
# 
# With this context, EDSA is challenging you to construct a recommendation algorithm based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed based on their historical preferences.
# %% [markdown]
# ## The Data
# This dataset consists of several million 5-star ratings obtained from users of the online [MovieLens](https://movielens.org/) movie recommendation service. The MovieLens dataset has long been used by industry and academic researchers to improve the performance of explicitly-based recommender systems, and now you get to as well!
# 
# 
# 
# ## Importing the dependancies

# %%
#===== The Usual Suspects =============
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#===== Machine Learning with Scikit Surprise ================
from surprise import SVD, accuracy, Dataset, NormalPredictor,SVDpp
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split

# %% [markdown]
# ### Loading csv files

# %%
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# %% [markdown]
# ## Exploring our data

# %%
movies.head()


# %%
ratings.head()


# %%
# Merge the two datasets to gain more insights
df = pd.merge(movies,ratings, on='movieId').drop('timestamp', axis=1)

# Extract the year from each movie title to create a year release year column for each movie
df['year'] = df.title.str.extract("\((\d{4})\)", expand=True)
df.year = pd.to_datetime(df.year, format='%Y')

df.head()


# %%
df.loc[df.year.isnull()]

# %% [markdown]
# ## Explore the data with some plots

# %%
# Plot the number of movies released each year

movies_per_year = df[['movieId', 'year']].groupby('year')

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(movies_per_year.year.first(), movies_per_year.movieId.nunique(), "g-o")
ax.grid(None)
ax.set_ylim(0,)
ax.set_xlabel('Year')
ax.set_ylabel('Number of movies released')

# %% [markdown]
# #### Insight 1
# 
# We see a sharp increase in the number of movies released between 1980 and 2000, and a sharp drop in movie production in 2009.

# %%
# Create a new dataframe with avarage rating and the number of rating for each movie

rating_df = pd.DataFrame(df.groupby('title')['rating'].mean())
rating_df['num_ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
rating_df.head()


# %%
_ = plt.figure(figsize=(10,5))
_ = sns.distplot(rating_df.num_ratings,bins=100, kde=False)

# %% [markdown]
# #### Insight 2
# 
# Most movies have zero or one rating. This can be attributed to the unavailability of movie rating systems in the 1900s to early 90s, and that most people only rate the big hit movies. This could potentially affect the results of a collaborative filtering algorithm since it maps user ratings to items.

# %%
# Visual distribution of the average ratings

_ = plt.figure(figsize=(10,5))
_ = sns.distplot(df.rating, kde=False)

# %% [markdown]
# #### Insight 3
# 
# Movie ratings seem to be normally distributed.

# %%
# Plot the relationship between average rating and number of ratings

_ = plt.figure(figsize=(10,7))
_ = sns.jointplot(x='rating',y='num_ratings',data=rating_df,alpha=0.5)

# %% [markdown]
# #### Insight 4
# 
# Looks like the more ratings a movie has, the higher the ratings for that movie.
# %% [markdown]
# ## Building the model

# %%
print('Length of Movies dataset:', movies.shape[0],'rows')
print('Length of Ratings dataset:', ratings.shape[0],'rows')


# %%
ratings = ratings.drop('timestamp',axis=1)


# %%
# Set the reader variable

reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings,reader)

# Instantiate the model
SVDpp_model = SVDpp()


# Train Test Split method
X_train, X_test = train_test_split(data,test_size=0.2)


# %%
# Fit the model to our data

SVDpp_model.fit(X_train)


# %%
# Predict 

predictions = SVDpp_model.test(X_test)


# %%
# Check the accuracy of our model

accuracy.rmse(predictions)

# %% [markdown]
# ## Conclusion
# 
# The model chosen for this task is the Singular Value Decomposition(`SVDpp`). This model performs probabilistic matrix factorization which is suitable for our Collaborative filtering task.
#   
# %% [markdown]
# ## Deployed App
# 
# 
# [Link to the deployed streamlit app](###)

# %%
# Prepare Kaggle submission

test = pd.read_csv('test.csv')

# Make predictions on test data
pred_list = []

for _,row in test.iterrows():
    x = (SVDpp_model.predict(row.userId, row.movieId))
    pred = x[3]
    pred_list.append(pred)


# %%
# Convert values to strings

test['userId'] = test['userId'].astype(str)
test['movieId'] = test['movieId'].astype(str)


# %%
# Create submission column

test['Id'] = test['userId'] +'_'+test['movieId']


# %%
submission_df = pd.DataFrame({'Id':test['Id'],
                              'rating':pred_list})


# %%
import pickle

model_save_path = 'SVDpp_model.pkl'
with open(model_save_path, 'wb') as file:
    pickle.dump(SVDpp_model, file)


# %%
submission_df.head()


# %%
submission_df.to_csv('k_sub.csv', index=False)


