from api import find_movie_by_title

def main():
    keyword = input("Keyword of title search: ")
    results = find_movie_by_title(keyword)

    for r in results:
        print(f"{r.title} has score {r.imdb_score}")

if __name__ == '__main__':
    main()
