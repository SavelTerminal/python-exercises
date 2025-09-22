movies = {
    "Inception": {"year": 2010, "rating": 8.8, "votes": 2000},
    "The Matrix": {"year": 1999, "rating": 10, "votes": 1800},
    "Interstellar": {"year": 2014, "rating": 8.9, "votes": 1700}
}

# Add a new movie in the dictionary "movies"
def add_movie(movies, name, year, rating, votes):
    # Check if the movie already exists
    if name in movies:
        return None
    else:
        # Add the movie with its details if not present
        movies[name] = {"year": year, "rating": rating, "votes": votes}
    # Return the name of the movie just added
    return name


# Call the function and add "Star Trek"
added_title = add_movie(movies, "Star Trek", 1966, 8.1, 1500)

# Print the result depending on the return value
if added_title:  # If the movie was added
    print(f"{added_title} has been added to your movies!")
else:  # If the movie already existed
    print("Movie already exists")


# Update the rating of an existing movie
def update_rating(movies, name, new_rating):
    # Check if the movie exists in the dictionary
    if name in movies:
        # Validate that the new rating is between 1 and 10
        if new_rating >= 1 and new_rating <= 10:
            # Get current rating and number of votes
            current_rating = movies[name]["rating"]
            current_votes = movies[name]["votes"]

            # Compute the new weighted average rating
            new_average = (current_rating * current_votes +
                           new_rating) / (current_votes + 1)

            # Update the dictionary with new rating and incremented votes
            movies[name]["rating"] = new_average
            movies[name]["votes"] += 1

            # Return the updated values (new average rating, new votes count)
            return new_average, current_votes + 1

    # If movie doesn't exist or rating is invalid, return None
    return None


# Example usage of update_rating
result = update_rating(movies, "Star Trek", 10)
if result:  # If the function returned values (not None)
    average, votes = result
    print(f"The average is {average}, the new votes are {votes}! ")
else:
    print("Movie doesn't exist!")


# Get the movie with the highest rating
def get_highest_rated(movies): 
    best_rating = 0.0
    
    # Loop through all movies
    for movie in movies:
        rating = movies[movie]["rating"]
        # Update the best rating and movie if a higher rating is found
        if rating > best_rating:
            best_rating = rating
            movie_title = movie
    # Return both the rating and the movie title
    return best_rating, movie_title
    

# Call the function and unpack the results
best_rating, name = get_highest_rated(movies) 
print(f"The best movie is {name} rated {best_rating}!")


# Print all movies in the catalog with their details
def print_catalog(movies):
    for movie in movies:
        print(f"Movie: {movie}")
        print(f"Year: {movies[movie]['year']}")
        print(f"Rating: {movies[movie]['rating']}")
        print(f"Votes: {movies[movie]['votes']}\n")


# Call the function to display the catalog
print_catalog(movies)


# Calculate the average rating across all movies
def get_average_rating(movies):
    total_rating = 0.0
    # Sum the ratings of all movies
    for movie in movies:
        current_rating = movies[movie]["rating"]
        total_rating += current_rating
    
    # Divide the total by the number of movies
    average_result = total_rating / len(movies)
    return average_result


# Call the function and print the result
average = get_average_rating(movies)
print(f"The average rating for this catalog is {average}!")
