import pygame,pickle,os
from sys import exit
from init import *
from scoreboard import *
from save import *
from dice import *
from moving import checkSquare
pygame.init()
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
                     'currentPlayer': 'player1' if currentPlayer == player1 else 'player2','player1_position': player1_position,'player2_position': player2_position,'gameEnded': gameEnded,'diceRolled': diceRolled,'player1_turns': player1_turns,'player2_turns': player2_turns,'player1_nickname': player1_nickname,'player2_nickname': player2_nickname,'player1Jailed':player1Jailed,'player2Jailed':player2Jailed,'player1_nickname':player1_nickname,'player2_nickname':player2_nickname
                }
                save_game_state(game_state)                 
            if event.key == pygame.K_SPACE and not diceRolled and not gameEnded: 
                diceRolled = True
                dice_number = rollDice()             
                if currentPlayer == player1:
                    if player1Jailed > 0:
                        player1Jailed -= 1
                        currentPlayer = player2
                    else:
                        if player1_position + dice_number <= 68:
                            player1_position += dice_number
                            screen.blit(background, (0, 0))
                            showDice(dice_number)
                            move(player1,player1_position)
                            move(player2, player2_position)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            player1_position = checkSquare(player1_position, dice_number)
                            if player1_position == 33:
                                prison_sound.play()
                                player1Jailed = 3
                        currentPlayer = player2
                elif currentPlayer == player2:
                    if player2Jailed > 0:
                        player2Jailed -= 1
                        currentPlayer = player1
                    else:
                        if player2_position + dice_number <= 68:
                            player2_position += dice_number
                            screen.blit(background, (0, 0))
                            showDice(dice_number)
                            move(player1,player1_position)
                            move(player2, player2_position)
                            pygame.display.update()
                            pygame.time.delay(1000)
                            player2_position = checkSquare(player2_position, dice_number)
                            if player2_position == 33:
                                prison_sound.play()
                                player2Jailed = 3
                        currentPlayer = player1
                screen.blit(background, (0, 0))                    
                move(player1, player1_position)
                move(player2, player2_position)
                showDice(dice_number)
            if player1Jailed > 0:
                    player1Jailed -=1
            if player2Jailed > 0:
                    player2Jailed -=1
            if player1_position == 68:
                    print(player1_nickname, "won")
                    gameEnded = True
                    update_scoreboard(player1_nickname, player1_turns)
                    display_scoreboard()
                    if os.path.exists("savegame.pkl"):
                        os.remove("savegame.pkl")               
            if player2_position == 68:
                    print(player2_nickname, "won")
                    gameEnded = True
                    update_scoreboard(player2_nickname, player2_turns)
                    display_scoreboard() 
                    if os.path.exists("savegame.pkl"):
                        os.remove("savegame.pkl")                                                       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                diceRolled = False
    pygame.display.update()
    clock.tick(60)
