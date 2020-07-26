#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import re


# In[2]:


train = pd.read_csv('../unsupervised_data/unsupervised_movie_data/train.csv')
movies = pd.read_csv('../unsupervised_data/unsupervised_movie_data/movies.csv')
df = pd.merge(train,movies, on='movieId')


# In[3]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())


# In[4]:


vote_counts = ratings[ratings['num of ratings'].notnull()]['num of ratings'].astype('int')
vote_averages = ratings[ratings['rating'].notnull()]['rating'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.95)


# In[5]:


ratings = pd.merge(ratings,movies, on='title')


# In[6]:


def get_dates_from_title(title):
    date_list = re.findall(r'\((\d{4})\)', title)
    if len(date_list)>0:
        return int(date_list[-1])
    else:
        return None

ratings['year'] = ratings['title'].apply(get_dates_from_title)


# In[7]:


genre_list = []
for i in ratings['genres']:
    genre_list.append(i.split('|'))
ratings['genres'] = genre_list


# In[8]:


s = ratings.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_ratings = ratings.drop('genres', axis=1).join(s)


# In[9]:


def build_chart(genre, percentile=0.85):
    df = gen_ratings[gen_ratings['genre'] == genre]
    vote_counts = df[df['num of ratings'].notnull()]['num of ratings'].astype('int')
    vote_averages = df[df['rating'].notnull()]['rating'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['num of ratings'] >= m) & (df['num of ratings'].notnull()) & (df['rating'].notnull())][['title', 'year', 'num of ratings', 'rating']]
    qualified['num of ratings'] = qualified['num of ratings'].astype('int')
    qualified['rating'] = qualified['rating'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['num of ratings']/(x['num of ratings']+m) * x['rating']) + (m/(m+x['num of ratings']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    
    return qualified['title'].head(10).tolist()


# In[ ]:





# In[ ]:




