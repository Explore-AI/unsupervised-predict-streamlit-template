# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


# %%
get_ipython().run_cell_magic('time', '', "train = pd.read_csv('edsa-recommender-system-predict/train.csv')\ntest = pd.read_csv('edsa-recommender-system-predict/test.csv')\ntags = pd.read_csv('edsa-recommender-system-predict/tags.csv')\nmovies = pd.read_csv('edsa-recommender-system-predict/movies.csv')\nlinks = pd.read_csv('edsa-recommender-system-predict/links.csv')\nimdb_data = pd.read_csv('edsa-recommender-system-predict/imdb_data.csv')\ngenome_tags = pd.read_csv('edsa-recommender-system-predict/genome_tags.csv')\ngenome_scores = pd.read_csv('edsa-recommender-system-predict/genome_scores.csv')")


# %%
train.head()

# %% [markdown]
# Check for missing values.

# %%
train.isnull().sum()


# %%
movies.head()

# %% [markdown]
# Check for missing values.

# %%
movies.isnull().sum()

# %% [markdown]
# Most frequent genre

# %%
pd.DataFrame(movies.genres.describe())


# %%
merged = train.merge(movies, on='movieId')


# %%
merged.head()

# %% [markdown]
# #### Converting the timestamp to the corresponding year

# %%
merged['rating_year'] = merged['timestamp'].apply(lambda timestamp: datetime.fromtimestamp(timestamp).year)
merged.drop('timestamp', axis=1, inplace=True)


# %%
merged['rating_year'].nunique()


# %%
merged['rating_year'].min(), merged['rating_year'].max()

# %% [markdown]
# The movie ratings span a period of 25 years from 1995 all the way to 2019

# %%
def get_release_dates(title):
    sub = title[-5:-1]
    year = int(sub) if sub.isdigit() else 9999
    return year

merged['release_year'] = merged['title'].apply(get_release_dates)


# %%
merged.head()


# %%
merged['release_year'].nunique()


# %%
merged[(merged['release_year'] >= 1995) & (merged['release_year'] <= 2019)]['movieId'].nunique()


# %%
def get_releases_by_year(df, release_years):
    
    mask = df[(df['release_year'] >= release_years[0]) & (df['release_year'] <= release_years[-1])]
    return [mask[mask['release_year'] == year]['movieId'].nunique() for year in release_years]

number_movies_released = pd.DataFrame({'release_year': list(range(1995, 2020)),
                                       'count': get_releases_by_year(merged, range(1995, 2020))})


# %%
fig, ax = plt.subplots(1, 2, figsize = (12, 6))
ax1 = merged.groupby('rating_year')['rating'].count().plot(kind='bar', ax=ax[0], title='Ratings by year')

ax2 = number_movies_released.groupby('release_year')['count'].sum().plot(kind='bar', ax=ax[1], title='Movies released by year')
fig.tight_layout()


# %%
def count_ratings_by_years(df, start, end):
    
    ratings_count = [0] * 10
    ratings = np.linspace(0.5, 5.0, 10)
    for year in range(start, end + 1):
        df_year = df[df['rating_year'] == year]
        count = 0
        for rating in ratings:
            ratings_count[count] += (df_year[df_year['rating'] == rating]['movieId'].count())
            count += 1
    return ratings_count


# %%
keys = np.linspace(0.5, 5.0, 10)
fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = sns.barplot(keys, count_ratings_by_years(merged, 1995, 2019), ax=ax[0])
ax1.set_title('Ratings 1995 - 2019')
ax1.set(xlabel='Movie rating', ylabel='Number of ratings')

ax2 = sns.barplot(keys, count_ratings_by_years(merged, 1995, 1999), ax=ax[1])
ax2.set_title('Ratings 1995 - 1999')
ax2.set(xlabel='Movie rating', ylabel='Number of ratings')
fig.tight_layout(pad=10.0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax3 = sns.barplot(keys, count_ratings_by_years(merged, 2000, 2004), ax=ax[0])
ax3.set_title('Ratings 2000 - 2004')
ax3.set(xlabel='Movie rating', ylabel='Number of ratings')

ax4 = sns.barplot(keys, count_ratings_by_years(merged, 2005, 2009), ax=ax[1])
ax4.set_title('Ratings 2005 - 2009')
ax4.set(xlabel='Movie rating', ylabel='Number of ratings')
fig.tight_layout(pad=10.0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax5 = sns.barplot(keys, count_ratings_by_years(merged, 2010, 2014), ax=ax[0])
ax5.set_title('Ratings 2010 - 2014')
ax5.set(xlabel='Movie rating', ylabel='Number of ratings')

ax6 = sns.barplot(keys, count_ratings_by_years(merged, 2015, 2019), ax=ax[1])
ax6.set_title('Ratings 2015 - 2019')
ax6.set(xlabel='Movie rating', ylabel='Number of ratings')

fig.tight_layout(pad=10.0)

# %% [markdown]
# #### Checking the sequence of user and movie ids

# %%
merged['userId'].min(), merged['userId'].max(), merged['userId'].nunique()


# %%
merged['movieId'].min(), merged['movieId'].max(), merged['movieId'].nunique()

# %% [markdown]
# We see above that the user ids are sequential, while the movie ids on the other hand are not. Later in the model building phase,
# the movie ids will need to be re-indexed. This will ensure no unnecessary space is used when the movie matrix is created for example. At the same time we will need to keep track of the original movie ids for when predictions need to be made.

# %%
merged['genre_count'] = merged['genres'].apply(lambda genres: len(genres.split('|')))


# %%
movie_genres = []
merged['genres'].apply(lambda genres: movie_genres.extend(genres.split('|')))
movie_genres = sorted(set(movie_genres))


# %%
def get_genre_count(number_of_genres, movie_genres, df):
    
    genre_count = [0] * len(movie_genres)
    for index, genres in df[df['genre_count'] == number_of_genres]['genres'].items():
        for genre in genres.split('|'):
            genre_count[movie_genres.index(genre)] += 1
            
    return genre_count


# %%
merged['genre_count'].min(), merged['genre_count'].max()


# %%
fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = merged.groupby('genre_count')['rating'].count().plot(kind='bar', title='Number of genres', ax=ax[0])
ax2 = merged.groupby('genre_count')['rating'].mean().plot(kind='line', marker='o', title='Average rating', ax=ax[1])

fig.tight_layout()


# %%
plt.barh(movie_genres, get_genre_count(1, movie_genres, merged))


# %%
plt.barh(movie_genres, get_genre_count(2, movie_genres, merged))


# %%
plt.barh(movie_genres, get_genre_count(3, movie_genres, merged))


# %%
plt.barh(movie_genres, get_genre_count(4, movie_genres, merged))


# %%
decades = [(1870, 1879), (1880, 1889), (1990, 1909), (1910, 1919), (1920, 1929),
           (1930, 1939), (1940, 1949), (1950, 1959), (1960, 1969), (1970, 1979),
           (1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (9999, 10000)]

decade_categories = ['1870s', '1880s', '1890s', '1900s', '1910s', '1920s', '1930s', '1940',
           '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', 'Unspecified']

def movie_rating_decade_released(start_year, end_year, decades, df):
    
    ratings_count = []
    ratings_average = []
    
    for start, end in decades:
        mask_1 = (df['release_year'] >= start) & (df['release_year'] <= end)
        mask_2 = (df['rating_year'] >= start_year) & (df['rating_year'] <= end_year)
        sub_df = df[mask_1 & mask_2]['rating']
        ratings_count.append(sub_df.count())
        ratings_average.append(np.round(sub_df.mean(), 2))
    
    return ratings_count, ratings_average


# %%
count, average = movie_rating_decade_released(1995, 2019, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)
decades_df


# %%
fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade', ax=ax[1])

fig.tight_layout()


# %%
count, average = movie_rating_decade_released(1995, 1999, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade: 1995 - 1999', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade: 1995 - 1999', ax=ax[1])

fig.tight_layout()


# %%
count, average = movie_rating_decade_released(2000, 2004, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade: 2000 - 2004', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade: 2000 - 2004', ax=ax[1])

fig.tight_layout()


# %%
count, average = movie_rating_decade_released(2005, 2009, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade: 2005 - 2009', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade: 2005 - 2009', ax=ax[1])

fig.tight_layout()


# %%
count, average = movie_rating_decade_released(2010, 2014, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade: 2010 - 2014', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade: 2010 - 2014', ax=ax[1])

fig.tight_layout()


# %%
count, average = movie_rating_decade_released(2015, 2020, decades, merged)
decades_df = pd.DataFrame(list(zip(decade_categories, count, average)), columns=['decade', 'ratings_count', 'ratings_average']).fillna(0)

fig, ax = plt.subplots(1, 2, figsize = (12, 6))

ax1 = decades_df.groupby('decade')['ratings_count'].sum().plot(kind='bar', title='Number of ratings per decade: 2015 - 2020', ax=ax[0])
ax2 = decades_df.groupby('decade')['ratings_average'].sum().plot(kind='line', marker='o', title='Average rating per decade: 2015 - 2020', ax=ax[1])

fig.tight_layout()

# %% [markdown]
# Analysis will centre around revenue cost for having movies on catalogue, showing users movies they don't want see - brand affinity, computational resources and the expense thereof.

# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



