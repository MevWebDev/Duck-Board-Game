# Importy itp.
import pygame, random,pickle,os
from sys import exit
from init import *
from scoreboard import *
from save import *
from dice import *
pygame.init()
try:
    # Jeżeli istnieje plik to ustawia te zmienne na zmienne w tym pliku
    with open('savegame.pkl', 'rb') as f:
        game_state = pickle.load(f)
        player1_position = game_state['player1_position']
        player2_position = game_state['player2_position']
        currentPlayer = player1 if game_state['currentPlayer'] == 'player1' else player2
        gameEnded = game_state['gameEnded']
        diceRolled = game_state['diceRolled']
        gameStarted = True  
        print("Loaded saved game.")
except FileNotFoundError:
    #Jeżeli nie ma zapisu to ustawia zmienne na zmienne startowe
    player1_position = 0
    player2_position = 0
    currentPlayer = player1
    gameEnded = False
    gameStarted = True
    diceRolled = False 
# Funkcja przemieszczająca pionki
def move(player, number):
    if player == player1:
        if number <= 68:
            screen.blit(player, (positionsX[number]+40, positionsY[number]))
    elif player == player2:
        if number <= 68:
            screen.blit(player, (positionsX[number]+80, positionsY[number]))
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameStarted == True:       
            screen.blit(background, (0, 0))
            move(player1,player1_position)
            move(player2,player2_position)
            gameStarted=False
        if event.type == pygame.KEYDOWN:
            # Po kliknięciu 's' program tworzy status gry w słowniku i zapisuje je do pliku
            if event.key == pygame.K_s:
                game_state = {
                    'player1_position': player1_position,
                    'player2_position': player2_position,
                    'currentPlayer': 'player1' if currentPlayer == player1 else 'player2',
                    'gameEnded': gameEnded,
                    'diceRolled': diceRolled,
                    'player1_turns': player1_turns,
                    'player2_turns': player2_turns,
                    'player1_nickname': player1_nickname,
                    'player2_nickname': player2_nickname
                }
                save(game_state)                 
            if event.key == pygame.K_TAB:
                display_scoreboard()
            if event.key == pygame.K_SPACE and not diceRolled and gameEnded == False: 
                diceRolled = True
                dice_number = 0
                if currentPlayer == player1:
                    dice_number = rollDice()
                    player1_turns += 1
                    if player1_position + dice_number <= 68:
                        player1_position += dice_number
                    currentPlayer = player2
                else:
                    dice_number = rollDice()
                    player2_turns += 1
                    if player2_position + dice_number <= 68:
                        player2_position += dice_number
                    currentPlayer = player1
                screen.blit(background, (0, 0))                    
                move(player1, player1_position)
                move(player2, player2_position)
                showDice(dice_number)
                if player1_position == 68:
                    print(player1_nickname, "won")
                    gameEnded = True
                    update_scoreboard(player1_nickname, player1_turns)
                    if os.path.exists("savegame.pkl"):
                        os.remove("savegame.pkl")               
                if player2_position == 68:
                    print(player2_nickname, "won")
                    gameEnded = True
                    update_scoreboard(player2_nickname, player2_turns) 
                    if os.path.exists("savegame.pkl"):
                        os.remove("savegame.pkl")                                                       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                diceRolled = False
    pygame.display.update()
    clock.tick(60)
