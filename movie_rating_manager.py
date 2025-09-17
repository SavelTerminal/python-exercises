movies = {
    "Inception": {"year": 2010, "rating": 8.8, "votes": 2000},
    "The Matrix": {"year": 1999, "rating": 8.7, "votes": 1800},
    "Interstellar": {"year": 2014, "rating": 8.6, "votes": 1700}
}

# Adding a new movie in the dictionary "Movies"


def add_movie(movies, name, year, rating, votes):
    if name in movies:
        return None
    else:
        movies[name] = {"year": year, "rating": rating, "votes": votes}
    return name


# Call the function just created and add a new movie
added_title = add_movie(movies, "Star Trek", 1966, 8.1, 1500)
if added_title:  # Checking if the name exists, and print the correspective result
    print(f"{added_title} has been added to your movies!")
else:
    print("Movie already exists")


# Update rating of an existing movie

def update_rating(movies, name, new_rating):
    # Check if the movie exists in the dictionary
    if name in movies:
        # Validate that the new rating is between 1 and 10
        if new_rating >= 1 and new_rating <= 10:
            # Get current rating and number of votes
            current_rating = movies[name]["rating"]
            current_votes = movies[name]["votes"]

            # Compute the new weighted average rating
            new_average = (current_rating * current_votes + new_rating) / (current_votes + 1)

            # Update the dictionary in place with the new rating and votes
            movies[name]["rating"] = new_average
            movies[name]["votes"] += 1

            # Return the updated values (new average rating, new votes count)
            return new_average, current_votes + 1

    # If movie doesn't exist or rating is invalid, return None
    return None


# Example usage
result = update_rating(movies, "Star Trek", 10)       #Packing the return in a single variable
if result:                                            #Checking if the return is not a none 
    average, votes = result
    print(f"The average is {average}, the new votes are {votes}! ")
else:
    print("Movie doesn't exist!")



