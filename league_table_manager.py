# In this exercise i will practice the use of dictionaries


league = {  # Creating the league (Dictionary)
    "real_madrid": {  # Creating the team (Innested Dictionary)
        # gf as "Goal scored", ga as "Goals against"
        "played": 0, "won": 0, "drawn": 0, "lost": 0,
        "gf": 0, "ga": 0, "points": 0
    },
    "barcelona": {
        "played": 0, "won": 0, "drawn": 0, "lost": 0,
        "gf": 0, "ga": 0, "points": 0
    },
    "juventus": {
        "played": 0, "won": 0, "drawn": 0, "lost": 0,
        "gf": 0, "ga": 0, "points": 0
    },
    "milan": {
        "played": 0, "won": 0, "drawn": 0, "lost": 0,
        "gf": 0, "ga": 0, "points": 0
    },

}

# This function is used to create a new team


def create_team(league, name):
    if name in league:  # If to check if the name already exist
        return False  # This result is needed to tell the program what happened
    else:
        league[name] = {"played": 0, "won": 0, "drawn": 0, "lost": 0,  # Here i created a new team with the default values
                        "gf": 0, "ga": 0, "points": 0}
        return True


# Put the function result in a variable (True/False)
added = create_team(league, "milan")
if added:  # If added checks if the results is True or False
    print("Team created successfully")
else:
    print("Team already exist")

def delete_team(league, name):
    if name in league:
        del league[name]
        return True
    else:
        return False

delete = delete_team(league, "milan")

if delete:
    print("Team deleted successfully")
else:
    print("Team not found")

print(league["juventus"].keys())