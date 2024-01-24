import pygame, random,pickle,os
from sys import exit
pygame.init()
scoreboard_file = 'scoreboard.pkl'
def load_scoreboard():
    try:
        with open(scoreboard_file,'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"An error occurred while loading the scoreboard: {e}")
        return []
def save_scoreboard(scoreboard_data):
    with open(scoreboard_file, 'wb') as f:
        pickle.dump(scoreboard_data, f)

def update_scoreboard(player_name, score):
    scoreboard_data = load_scoreboard()
    
    # Check if the player is already in the scoreboard
    for entry in scoreboard_data:
        if entry['player'] == player_name:
            entry['score'] = score
            break
    else:
        # If the player isn't in the scoreboard, add them
        scoreboard_data.append({'player': player_name, 'score': score})
    
    # Sort the scoreboard based on scores in descending order
    scoreboard_data = bubblesort(scoreboard_data)
    
    # Save the updated scoreboard
    save_scoreboard(scoreboard_data)
def bubblesort(scoreboard):
    n = len(scoreboard)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if scoreboard[j]['score'] > scoreboard[j + 1]['score']:
                # Swap the entire entry, not just the score
                scoreboard[j], scoreboard[j + 1] = scoreboard[j + 1], scoreboard[j]
    return scoreboard
def display_scoreboard():
    scoreboard = load_scoreboard()
    print('Scoreboard:')
    for index, entry in enumerate(scoreboard):
        print(f"{index + 1}. {entry['player']}, Moves: {entry['score']}")
# Funkcja rzucająca kostką i zwracająca wynik