"""
Bite 30. Movie data analysis
In this Bite we are going to parse a csv movie dataset to identify the directors with the highest rated movies.

Write get_movies_by_director: use csv.DictReader to convert movie_metadata.csv into
a (default)dict of lists of Movie namedtuples. Convert/filter the data:
- Only extract director_name, movie_title, title_year and imdb_score, ignoring movies without all of these fields.
- Type conversions: title_year -> int / imdb_score -> float
- Discard any movies older than 1960.

Here is an extract:
....
{ 'Woody Allen': [
    Movie(title='Midnight in Paris', year=2011, score=7.7),
    Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
    Movie(title='To Rome with Love', year=2012, score=6.3),  ....
    ], ...
}
Write the calc_mean_score helper that takes a list of Movie namedtuples and calculates the mean IMDb score,
returning the score rounded to 1 decimal place.

Complete get_average_scores which takes the directors data structure returned by get_movies_by_director (see 1.)
and returns a list of tuples (director, average_score) ordered by highest score in descending order.
Only take directors into account with >= MIN_MOVIES
"""

from collections import defaultdict, namedtuple
from urllib.request import urlretrieve
from statistics import mean
import csv
import os

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)

    with open(MOVIE_DATA, "r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if not row["title_year"]:
                continue
            year = int(row["title_year"])
            if year < 1960:
                continue
            director = row["director_name"]
            title = row["movie_title"].strip()
            score = float(row["imdb_score"])
            movies[director].append(Movie(title=title, year=year, score=score))
    return movies

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    mean_score = mean(movie.score
                      for movie in movies)
    return round(mean_score, ndigits=1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = []

    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        average_scores.append((director, calc_mean_score(movies)))

    return sorted(average_scores,
                  key=lambda t: t[1],
                  reverse=True)
