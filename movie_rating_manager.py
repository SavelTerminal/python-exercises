movies = {
    "Inception": {"year": 2010, "rating": 8.8, "votes": 2000},
    "The Matrix": {"year": 1999, "rating": 8.7, "votes": 1800},
    "Interstellar": {"year": 2014, "rating": 8.6, "votes": 1700}
}

# Adding a new movie in the dictionary "Movies"


def add_movies(movies, name, year, rating, votes):
    if name in movies:
        print("Movie already exist")
        return False
    else:
        movies[name] = {"year": year, "rating": rating, "votes": votes}
        
        last = ""

        for movie in movies:
            last = movie
        print(f"You successfully added {last} in your movies list!")
    return True

add_movies(movies, "Star Trek", 1966, 8.1, 1500)



# Update rating of an existing movie

movies["Star Trek"]["rating"] = 8.1

print(movies)
