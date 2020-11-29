"""
Functions to build EDA page in streamlit app

Authored by: JHB_team_RM4
"""


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from utils import data_loader as dl

sns.set(font_scale=1)
sns.set_style("white")

# Load data
train_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/train.csv', index=None)
movies_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/movies.csv', index='movieId')
imdb_df = dl.load_dataframe('../unsupervised_data/unsupervised_movie_data/imdb_data.csv', index=None)

# Functions
# Ratings
def user_ratings_count(df, n): # N can be played with and  included as an app?
    """
    Returns the top n users by number of ratings in a barplot
    Parameters
    ----------
        df (DataFrame): input DataFrame
        n (int): number of users to show
    Returns
    -------
        barplot (NoneType): barplot of top n users by number of observations
    Example
    -------
        >>> df = pd.DataFrame({'userId':[1,2,3,1,2,4,5,4]})
        >>> user_ratings_count(df, 3)
            NoneType (barplot)
    """
    plt.figure(figsize=(8,6))
    data = df['userId'].value_counts().head(n)
    ax = sns.barplot(x = data.index, y = data, order= data.index, palette='brg', edgecolor="black")
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), fontsize=11, ha='center', va='bottom')
    plt.title(f'Top {n} Users by Number of Ratings', fontsize=14)
    plt.xlabel('User ID')
    plt.ylabel('Number of Ratings')
    print("Combined number of ratings:\t",df['userId'].value_counts().head(n).sum(),
         "\nTotal number of movies:\t\t", df['movieId'].nunique())
    plt.show()

def ratings_distplot(df, column='rating'):
    """
    docstring
    """
    plt.figure(figsize=(8,6))
    ax = sns.distplot(df[f'{column}'],bins=10, kde=False, hist_kws=dict(alpha=0.6),color="#4DA017")
    mean = df[f'{column}'].mean()
    median = df[f'{column}'].median()
    plt.axvline(x=mean, label = f'mean {round(mean,2)}' , color='#FF0029', lw=3, ls = '--')
    plt.axvline(x=median, label = f'median {median}' , color='#4DA017', lw=3, ls = '--')
    plt.xlim((0.5,5))
    plt.ylim((0,2500000))
    plt.title(f'Distribution of Ratings', fontsize=14)
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def mean_ratings_scatter(df, color='#4DA017', column='userId'):
    """
    Describe function here
    Parameters
    ----------
    Returns
    -------
    Example
    """
    plt.figure(figsize=(6,4))
    mean_ratings = df.groupby(f'{column}')['rating'].mean()
    user_counts = df.groupby(f'{column}')['movieId'].count().values
    sns.scatterplot(x=mean_ratings, y = user_counts, color=color)
    plt.title(f'Mean Ratings by Number of Ratings', fontsize=14)
    plt.xlabel('Rating')
    plt.ylabel('Number of Ratings')
    plt.show()

def plot_ratings(count, n, color='#4DA017', best=True, method='mean'):
    """
    docstring
    """
    eda_df = train_df[train_df['userId']!=72315]
    if method == 'mean':
        movie_avg_ratings = pd.merge(eda_df, movies_df, on='movieId', how='left').groupby(['movieId', 'title'])['rating'].mean()
    else:
        movie_avg_ratings = pd.DataFrame(eda_df.join(movies_df, on='movieId', how='left').groupby(['movieId', 'title'])['rating'].median())
    movie_avg_ratings['count'] = eda_df.groupby('movieId')['userId'].count().values
    movie_avg_ratings.reset_index(inplace=True)
    movie_avg_ratings.set_index('movieId', inplace=True)

    # Remove movies that have been rated fewer than n times
    data = movie_avg_ratings[movie_avg_ratings['count']>count]
    data.sort_values('rating', inplace= True,ascending=False)
    if best == True:
        plot = data.head(n).sort_values('rating', ascending=True)
        title='Best Rated'
    else:
        plot = data.tail(n).sort_values('rating', ascending=False)
        title='Worst Rated'
    plt.figure(figsize=(6,5))
    sns.scatterplot(x=plot['rating'], y=plot['title'], size=plot['count'], color=color)
    plt.xlabel('Rating')
    plt.ylabel('')
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
    plt.title(f'Top {n} {title} Movies with Over {count} Ratings', fontsize=14)
    plt.show()

def number_users_per_rating(df1 = train_df):
    """
    Plots the number of users who gave a rating
    Parameters
    ----------
        df1 (DataFrame): input df containg user-item interactions matrix
    Returns
    -------
        barplot (NoneType): barplot of results
    """
    movieRatingDistGroup = df1['rating'].value_counts().sort_index().reset_index()
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(data=movieRatingDistGroup, x='index', y='rating', palette="brg", edgecolor="black", ax=ax)
    ax.set_xlabel("Rating")
    ax.set_ylabel('Number of Users')
    ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
    total = float(movieRatingDistGroup['rating'].sum())
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2., height+350, '{0:.2%}'.format(height/total), fontsize=11, ha="center", va='bottom')
    plt.title('Number of Users Per Rating', fontsize=14)
    plt.show()

# Genres

# function that hasn't found a use yet
def feat_extractor(df, col):
    """
    returns a list of all unique features in a DataFrame columns separated by "|"
    """
    df.fillna("", inplace=True)
    feat_set = set()
    for i in range(len(df[f'{col}'])):
        for feat in df[f'{col}'].iloc[i].split('|'):
            feat_set.add(feat)
    return sorted([feat for feat in feat_set if feat != ""])

@st.cache(allow_output_mutation=True)
def feature_frequency(df, column):
    """
    Function to count the number of occurences of metadata such as genre
    Parameters
    ----------
        df (DataFrame): input DataFrame containing movie metadata
        column (str): target column to extract features from
    Returns
    -------

    """
    # Creat a dict to store values
    df = df.dropna(axis=0)
    genre_dict = {f'{column}': list(),
                 'count': list(),}
    # Retrieve a list of all possible genres
    print('retrieving features...')
    for movie in range(len(df)):
        gens = df[f'{column}'].iloc[movie].split('|')
        for gen in gens:
            if gen not in genre_dict[f'{column}']:
                genre_dict[f'{column}'].append(gen)
    # count the number of occurences of each genre
    print('counting...')
    for genre in genre_dict[f'{column}']:
        count = 0
        for movie in range(len(df)):
            gens = df[f'{column}'].iloc[movie].split('|')
            if genre in gens:
                count += 1
        genre_dict['count'].append(count)

        # Calculate metrics
    data = pd.DataFrame(genre_dict)
    return data

def feature_count(df, column):
    """
    Returns a barplot showing the number of movies per genre
    Parameters
    ----------
        df (DataFrame): input dataframe containing genre frequency
        column (str): target column to plot
    Returns
    -------
        barplot (NoneType): barplot visual
    Example
    -------
    """
    plt.figure(figsize=(10,6))
    ax = sns.barplot(y = df[f'{column}'], x = df['count'], palette='brg', orient='h')
    plt.title(f'Number of Movies Per {column[:-1]}', fontsize=14)
    plt.ylabel(f'{column}')
    plt.xlabel('Count')
    plt.show()

    #mean_ratings = pd.DataFrame(train_df.join(movies_df, on='movieId', how='left').join(imdb_df, on = 'movieId', how = 'left').groupby(['movieId'])['rating'].mean())

@st.cache(allow_output_mutation=True)
def mean_calc(feat_df, ratings = train_df, movies = movies_df, metadata = imdb_df, column = 'genres'):
    """
    Function that calculates the mean ratings of a feature
    Parameters
    ----------
        feat_df (DataFrame): input df containing feature data eg genres
        ratings (DataFrame): user-item interaction matrix
        movies (DataFrame): input df containing item names and genres column
        metadata (DataFrame): input df containing imdb metadata
        column (str): target column to calculate means
    Returns
    -------
        means (list): list of means for each genre
    Example
    -------
        >>>genres['mean_rating'] = mean_calc(genres)

    """
    mean_ratings = pd.DataFrame(ratings.join(movies, on='movieId', how='left').groupby(['movieId'])['rating'].mean())
    movie_eda = movies.copy()
    movie_eda = movie_eda.join(mean_ratings, on = 'movieId', how = 'left')

    # Exclude missing values
    movie_eda = movie_eda
    movie_eda2 = movie_eda[movie_eda['rating'].notnull()]

    means = []
    for feat in feat_df[f'{column}']:
        mean = round(movie_eda2[movie_eda2[f'{column}'].str.contains(feat)]['rating'].mean(),2)
        means.append(mean)
    return means
    genres['mean_rating'] = mean_calc(genres)
    genres.sort_values('mean_rating', ascending=False).head(5)

def genre_popularity(df):
    """
    docstring
    """
    count_filt = 500
    plt.figure(figsize=(10,6))
    plot_data = df[df['count']>count_filt]
    mean = plot_data['mean_rating'].mean()
    min_ = plot_data['mean_rating'].min()
    max_ = plot_data['mean_rating'].max()
    sns.barplot(y = plot_data['genres'], x = plot_data['mean_rating'], order = plot_data['genres'], orient='h',palette='brg')
    plt.axvline(x=mean, label = f'mean {round(mean,1)}' , color='black', lw=1, ls ='--')
    plt.axvline(x=min_, label = f'min {round(min_,1)}' , color='#4D17A0', lw=1, ls = '--')
    plt.axvline(x=max_, label = f'max {max_}' , color='#4DA017', lw=1,ls = '--')
    plt.title(f'Mean Rating Per Genre', fontsize=14)
    plt.ylabel('Genre')
    plt.xlabel('Mean Rating')
    plt.legend(loc='lower center')
    plt.tight_layout()
    plt.show()

# Directors

def count_directors(df, count = 10):
    """
    Function to count the most common dircetors in a DataFrame:
    Parameters
    ----------
        df (DataFrame): input dataframe containing imdb metadata
        count (int): filter directors with fewer than count films

    Returns
    -------
        directors (DataFrame): output DataFrame
    Examples
    --------
        >>> df = pd.DataFrame({'imdbid':[0,1,2,3,4,5], 'director': [A,B,A,C,B]})
        >>> count_directors(df, count = 1)
            |index|director|count|
            |0|A|2|
            |1|B|2|
            |2|C|1|
    """
    directors = pd.DataFrame(df['director'].value_counts()).reset_index()
    directors.columns = ['director', 'count']
    # Lets only take directors who have made 10 or more movies otherwise we will have to analyze 11000 directors
    directors = directors[directors['count']>=count]
    return directors.sort_values('count', ascending = False)
@st.cache(allow_output_mutation=True)
def dir_mean(df):
    df.set_index('director', inplace=True)

    direct_ratings = []
    directors_eda = train_df.merge(imdb_df.set_index('movieId'), on = 'movieId', how = 'left')
    for director in df.index:
        rating = round(directors_eda[directors_eda['director']==director]['rating'].mean(),2)
        direct_ratings.append(rating)
    df['mean_rating'] = direct_ratings
    return df.sort_values('mean_rating', ascending = False)

def feat_popularity(df, title = 'feat'):
    """
    docstring
    """
    plt.figure(figsize=(10,6))
    plot_data = df.copy()
    mean = plot_data['mean_rating'].mean()
    min_ = plot_data['mean_rating'].min()
    max_ = round(plot_data['mean_rating'].max(),2)
    sns.barplot(y = plot_data.index, x = plot_data['mean_rating'], order = plot_data.index, orient='h',palette='brg')
    plt.axvline(x=mean, label = f'mean {round(mean,1)}' , color='black', lw=1, ls ='--')
    plt.axvline(x=min_, label = f'min {round(min_,1)}' , color='#4D17A0', lw=1, ls = '--')
    plt.axvline(x=max_, label = f'max {max_}' , color='#4DA017', lw=1,ls = '--')
    plt.title(f'Mean Rating Per {title}', fontsize=14)
    plt.ylabel('Genre')
    plt.xlabel('Mean Rating')
    plt.legend(loc='lower center')
    plt.show()

def plot_ratings(count, n=10, color='#4DA017', best=True, method='mean'):
    """
    docstring
    """
    # What are the best and worst movies
    # Creating a new DF with mean and count
    if method == 'mean':
        movie_avg_ratings = pd.DataFrame(train_df.join(movies_df, on='movieId', how='left').groupby(['movieId', 'title'])['rating'].mean())
    else:
        movie_avg_ratings = pd.DataFrame(train_df.join(movies_df, on='movieId', how='left').groupby(['movieId', 'title'])['rating'].median())
    movie_avg_ratings['count'] = train_df.groupby('movieId')['userId'].count().values
    movie_avg_ratings.reset_index(inplace=True)
    movie_avg_ratings.set_index('movieId', inplace=True)

    # Remove movies that have been rated fewer than n times
    data = movie_avg_ratings[movie_avg_ratings['count']>count]
    data.sort_values('rating', inplace= True,ascending=False)
    if best == True:
        plot = data.head(n).sort_values('rating', ascending=True)
        title='Best Rated'
    else:
        plot = data.tail(n).sort_values('rating', ascending=False)
        title='Worst Rated'
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=plot['rating'], y=plot['title'], size=plot['count'], color=color)
    plt.xlabel('Rating')
    plt.ylabel('', fontsize=8)
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
    plt.title(f'Top {n} {title} Movies with Over {count} Ratings', fontsize=14)
    plt.tight_layout()
    plt.show()

    # function that hasn't found a use yet
def feat_extractor(df, col):
    """
    returns a list of all unique features in a DataFrame columns separated by "|"
    """
    df.fillna("", inplace=True)
    feat_set = set()
    for i in range(len(df[f'{col}'])):
        for feat in df[f'{col}'].iloc[i].split('|'):
            feat_set.add(feat)
    return sorted([feat for feat in feat_set if feat != ""])

def genre_frequency(df):
    """
    docstring
    """
    # Creat a dict to store values
    genre_dict = {'genre': list(),
                 'count': list(),}
    # Retrieve a list of all possible genres
    for movie in range(len(df)):
        gens = df['genres'].iloc[movie].split('|')
        for gen in gens:
            if gen not in genre_dict['genre']:
                genre_dict['genre'].append(gen)
    # count the number of occurences of each genre
    for genre in genre_dict['genre']:
        count = 0
        for movie in range(len(df)):
            gens = df['genres'].iloc[movie].split('|')
            if genre in gens:
                count += 1
        genre_dict['count'].append(count)

        # Calculate metrics
    data = pd.DataFrame(genre_dict)
    return data
    data = genre_frequency(movies_df)

def genre_count(df):
    plt.figure(figsize=(10,6))
    ax = sns.barplot(y = df['genre'], x = df['count'], palette='brg', orient='h')
    plt.title(f'Number of Movies Per Genre', fontsize=14)
    plt.ylabel('Genre')
    plt.xlabel('Count')
    plt.show()
