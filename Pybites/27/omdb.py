import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movies.append(json.load(f))
    return movies

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies,
               key=lambda movie: int(movie["Awards"].split(" & ")[-1].replace(" nominations.", ""))
               )["Title"]

def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies,
               key= lambda movie: int(movie["Runtime"].replace(" min", ""))
               )["Title"]
