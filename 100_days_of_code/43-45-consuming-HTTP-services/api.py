from typing import List

import requests
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f"http://movie_service.talkpython.fm/api/search/{keyword}"

    response = requests.get(url)
    response.raise_for_status()

    results = response.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies
