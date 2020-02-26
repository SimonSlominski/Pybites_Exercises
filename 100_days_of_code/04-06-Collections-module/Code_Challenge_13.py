"""
Code Challenge 13 - Highest Rated Movie Directors

Details
There is this great ML article Predict Movie Rating. In this week's code challenge we use its data set to
get the 20 highest rated directors based on their average movie IMDB ratings.

STEPS:
As mentioned in the article the dataset is here, but we provided a copy in the repo's 13/ subfolder.

1. Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts
from which you only need the following k,v pairs:

OrderedDict([...
            ('director_name', 'Lawrence Kasdan'),
            ...
            ('movie_title', 'Mumford\xa0'),
            ...
            ('title_year', '1999'),
            ...
            ('imdb_score', '6.9'),
            ...
2. Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data.
3. Take movies of year >= 1960.
4. Print the top 20 highest rated directors with their movies ordered desc on rating.
5. It should look something like this (indeed some awesome movies here!):

$ python directors.py

01. Sergio Leone                                         8.5
------------------------------------------------------------
1966] The Good, the Bad and the Ugly                     8.9
1968] Once Upon a Time in the West                       8.6
1984] Once Upon a Time in America                        8.4
1964] A Fistful of Dollars                               8.0

02. Christopher Nolan                                    8.4
------------------------------------------------------------
2008] The Dark Knight                                    9.0
2010] Inception                                          8.8
2014] Interstellar                                       8.6
2012] The Dark Knight Rises                              8.5
2006] The Prestige                                       8.5
2000] Memento                                            8.5
2005] Batman Begins                                      8.3
2002] Insomnia                                           7.2
.
.
.

We included a template but maybe you want to code this up from scratch and/or use your favorite power tools (Pandas, SQL, etc.)
"""


from collections import defaultdict, namedtuple
import csv
import os


MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''

    # Check if CSV files is in proper directory
    # cwd = os.getcwd()           # Get the current working directory (cwd)
    # files = os.listdir(cwd)     # Get all the files in that directory
    # print(cwd, files)

    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

# Print test data
# directors = get_movies_by_director()
# print(directors['Steven Spielberg'])


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''

    filtered_directors = defaultdict(list)

    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            filtered_directors[(director, _calc_mean(movies))] = movies

    return filtered_directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total = 0
    for movie in movies:
        total += movie.score

    return round(total / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    summary = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)[:NUM_TOP_DIRECTORS]

    for rank, movie in enumerate(summary, start=1):
        (director, avg), movies = movie
        print(fmt_director_entry.format(counter=rank, director=director, avg=avg))
        print(sep_line)

        for movie in movies:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))

        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()

