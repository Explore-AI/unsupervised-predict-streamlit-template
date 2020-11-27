#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import re


# In[2]:


train = pd.read_csv('resources/data/ratings.csv')
movies = pd.read_csv('resources/data/movies.csv')
df = pd.merge(train,movies, on='movieId')


# In[3]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
vote_counts = ratings[ratings['num of ratings'].notnull()]['num of ratings'].astype('int')
vote_averages = ratings[ratings['rating'].notnull()]['rating'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.95)


# In[4]:


ratings = pd.merge(ratings,movies, on='title')


# In[5]:


def get_dates_from_title(title):
    date_list = re.findall(r'\((\d{4})\)', title)
    if len(date_list)>0:
        return int(date_list[-1])
    else:
        return None

ratings['year'] = ratings['title'].apply(get_dates_from_title)


# In[6]:


genre_list = []
for i in ratings['genres']:
    genre_list.append(i.split('|'))
ratings['genres'] = genre_list


# In[7]:


qualified = ratings[(ratings['num of ratings'] >= m) & (ratings['num of ratings'].notnull()) & (ratings['rating'].notnull())][['title', 'year', 'num of ratings', 'rating', 'genres']]
qualified['num of ratings'] = qualified['num of ratings'].astype('int')
qualified['rating'] = qualified['rating'].astype('int')


# In[8]:


def weighted_rating(x):
    v = x['num of ratings']
    R = x['rating']
    return (v/(v+m) * R) + (m/(m+v) * C)


# In[9]:


qualified['wr'] = qualified.apply(weighted_rating, axis=1)
qualified = qualified.sort_values('wr', ascending=False).head(250)


# In[10]:


def popular_per_year(year):
    return qualified[qualified['year'] == year]['title'].head(10).tolist()


# In[ ]:





# In[ ]:




