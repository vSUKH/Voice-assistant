import random

def roll ():
    min_value = 2
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll
while True :
    players = input("Inter the number of players (2-6): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=6 :
            break
        else:
            print ("Must be between 2-6 players. ")
    else:
        print ("invalid, try agrain.")

max_score = 50
players_scores = [0 for _ in range (players)]

while max (players_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayers number",player_idx + 1, "Turn has just started!\n")
        current_score = 0

        while True :
            should_roll = input("Wholdyou like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else :
                current_score += value
                print("You rolled a :" ,value)

            print("Your score is :",current_score)

        players_scores[player_idx] += current_score
        print("Your total score is: ",players_scores[player_idx])
                
max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number",winning_idx + 1, "is the winner with a score of :",max_score)

