#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
with open('../resource/lib/public/georgia_tech_football.csv', 'r') as record_file:
    listOfGames = []
    headers = record_file.readline().strip().split(",")

    for line in record_file:
        game = {}
        values = line.strip().split(",")
        for k, v in zip(headers, values):
            game[k] = v
        listOfGames.append(game)

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

def findFirstOpponent():
    firstDate = listOfGames[0]["Date"]
    for game in listOfGames:
        if game["Date"] < firstDate:
            firstDate = game["Date"]
    for game in listOfGames:
        if game["Date"] == firstDate:
            return game["Opponent"]
        
def findPointsFor(opponent):
    total = 0
    for game in listOfGames:
        if game["Opponent"] == opponent:
            total += int(game["Points For"])
    return total

def findPointsAgainst(opponent):
    total = 0
    for game in listOfGames:
        if game["Opponent"] == opponent:
            total += int(game["Points Against"])
    return total

def findHomeRecord():
    wins = 0
    losses = 0
    ties = 0
    for game in listOfGames:
        if game["Location"] == "Home":
            if int(game["Points For"]) > int(game["Points Against"]):
                    wins += 1
            elif int(game["Points For"]) < int(game["Points Against"]):
                losses += 1
            else:
                ties += 1
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def findYearRecord(year):
    wins = 0
    losses = 0
    ties = 0
    for game in listOfGames:
        if str(year) in game["Date"]:
            if int(game["Points For"]) > int(game["Points Against"]):
                    wins += 1
            elif int(game["Points For"]) < int(game["Points Against"]):
                losses += 1
            else:
                ties += 1
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def findMonthRecord(month):
    wins = 0
    losses = 0
    ties = 0
    for game in listOfGames:
        date = game["Date"].split("-")
        if str(month) == game["Date"][5:7]:
            if int(game["Points For"]) > int(game["Points Against"]):
                    wins += 1
            elif int(game["Points For"]) < int(game["Points Against"]):
                losses += 1
            else:
                ties += 1
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def findYearsRecord(year1, year2):
    wins = 0
    losses = 0
    ties = 0
    for game in listOfGames:
        if int(game["Date"][0:4]) in range(year1, year2 + 1) :
            if int(game["Points For"]) > int(game["Points Against"]):
                    wins += 1
            elif int(game["Points For"]) < int(game["Points Against"]):
                losses += 1
            else:
                ties += 1
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def mostPointsFor():
    max = 0
    maxTeam = ""
    pointsAgainst = {}
    for game in listOfGames:
        if game["Opponent"] not in pointsAgainst:
            pointsAgainst[game["Opponent"]] = int(game["Points For"])
        else:
            pointsAgainst[game["Opponent"]] += int(game["Points For"])
            if pointsAgainst[game["Opponent"]] > max:
                max = pointsAgainst[game["Opponent"]]
                maxTeam = game["Opponent"]
    return maxTeam

def neverScoredAgainst():
    pointsAgainst = {}
    for game in listOfGames:
        if game["Opponent"] not in pointsAgainst:
            pointsAgainst[game["Opponent"]] = int(game["Points For"])
        else:
            pointsAgainst[game["Opponent"]] += int(game["Points For"])

    neverScored = []
    for k, v in pointsAgainst.items():
        if v == 0:
            neverScored.append(k)
    
    return neverScored

def neverScoredFor():
    pointsFor = {}
    for game in listOfGames:
        if game["Opponent"] not in pointsFor:
            pointsFor[game["Opponent"]] = int(game["Points Against"])
        else:
            pointsFor[game["Opponent"]] += int(game["Points Against"])

    neverScored = []
    for k, v in pointsFor.items():
        if v == 0:
            neverScored.append(k)
    
    return len(neverScored)

def mostDifferential():
    # Initialize max to negative infinity
    max = float('-inf') 
    team = "" 
    
    for game in listOfGames:
        differential = int(game["Points For"]) - int(game["Points Against"])
        
        # This will now work correctly for both positive and negative differentials
        if differential > max:
            max = differential
            team = game["Opponent"]
            
    return team

def highest_average_differential():
    # Step 1: Aggregate stats for each opponent
    opponent_stats = {}
    for game in listOfGames:
        opponent = game["Opponent"]
        
        # Add the opponent to our dictionary if they're not already there
        if opponent not in opponent_stats:
            opponent_stats[opponent] = {
                "games_played": 0,
                "total_points_for": 0,
                "total_points_against": 0
            }
        
        # Update the stats for the current opponent
        opponent_stats[opponent]["games_played"] += 1
        opponent_stats[opponent]["total_points_for"] += int(game["Points For"])
        opponent_stats[opponent]["total_points_against"] += int(game["Points Against"])
        
    # Step 2: Calculate averages and find the team with the highest
    max_avg_differential = float('-inf')
    best_team = None
    
    for opponent, stats in opponent_stats.items():
        
        # Apply the "at least 5 games" constraint
        if stats["games_played"] >= 5:
            
            # Calculate the average differential
            total_differential = stats["total_points_for"] - stats["total_points_against"]
            average_differential = total_differential / stats["games_played"]
            
            # If this team's average is the new max, save it
            if average_differential > max_avg_differential:
                max_avg_differential = average_differential
                best_team = opponent
                
    # Step 3: Return the result
    return best_team

# You can call the function like this:


def main():
    print(findFirstOpponent())
    print(findPointsFor("Auburn"))
    print(findPointsAgainst("Auburn"))
    print(findHomeRecord())
    print(findYearRecord(2009))
    print(findMonthRecord(10))
    print(findYearsRecord(1933, 1963))
    print(mostPointsFor())
    print(neverScoredAgainst())
    print(neverScoredFor())
    print(mostDifferential())
    print(highest_average_differential())

main()