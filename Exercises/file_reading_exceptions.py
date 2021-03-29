# Author: Gatlin Lawson
def getMovies():
    movies = []

    try:
        with open("Exercises/March23rd/movies.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
    except FileNotFoundError:
        print("File could not be located")

    return movies

print("!!!  Awesome movie program  !!!")
movies = getMovies()

for movie in movies:
    print(movie)