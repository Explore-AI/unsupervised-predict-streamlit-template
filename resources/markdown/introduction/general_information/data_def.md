### Variable Definitions

#### Numeric:

* budget: - (continuous) dollar cost of production of the movie.
* rating: - (discrete) users rating of a movie from. TARGET
* relevance: - (continuous) measure (0-1) of the relevance of a genome tag to the movie, where 1 implies 100% relevance.
* runtime: - (continuous) movie duration in minutes.
* timestamp: - (continuous) the time at which a user rated the movie.

#### Categorical:

* director: - (nominal) the person who controls the making of a film and supervises the actors and technical crew.
* genres: - (nominal) the style or category of the movie. A movie may belong to multiple (up to nineteen) genres, or may be absent a genre listing.
* imdbId: - (nominal) unique identifying key for each IMBD entry. Can also be used in conjunction with the TMDB API.
* movieId: - (nominal) a unique identifier for each movie. There are 48,213 unique movies.
* plot_keywords: - (nominal) key words used to identify characteristics of a movie's storyline.
* tag: - (nominal) genome label
* tagId: - (nominal) unique genome identifier.
* tmdbId: - (nominal) unique identifier that works in conjunction with the TMDB API.
* title: - (nominal) the unique title identifying the movie. Included is a year of release enclosed in parenthesis at the end of the title.
* title_cast: - (nominal) the actors of the main characters in the movie. This does not include extras.
* userId: - (nominal) a unique identifier for each user. There are 162,541 unique users.

*The Movie Genome concept is borrowed from the Human Genome Project, a scientific project to identify and map all human genes. Similarly, a Movie Genome identifies and indexes multiple “genes” (elements and aspects) of a movie.*
