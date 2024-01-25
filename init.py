import pygame, random,pickle,os
from sys import exit
pygame.init()

# Zmienne przechowujące tło, zegar, pionki i kostę

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png')
background = pygame.transform.scale(background, (1280, 720))
soundtrack = pygame.mixer.Sound('src/soundtrack.mp3')
soundtrack.set_volume(0.009)
rollsound = pygame.mixer.Sound('src/roll.mp3')
rollsound.set_volume(0.2)
player1 = pygame.image.load('src/player1.png')
player1 = pygame.transform.scale(player1, (75, 75))
player2 = pygame.image.load('src/player2.png')
player2 = pygame.transform.scale(player2, (75, 75))
gameStarted = True
dice = pygame.image.load('src/dice1.png')
ladder_sound = pygame.mixer.Sound('src/ladder.mp3')
ladder_sound.set_volume(0.05)
rip_sound = pygame.mixer.Sound('src/rip.mp3')
rip_sound.set_volume(0.01)
prison_sound = pygame.mixer.Sound('src/prison.mp3')
prison_sound.set_volume(0.01)
x2_sound = pygame.mixer.Sound('src/x2.mp3')
x2_sound.set_volume(0.01)
wind_sound = pygame.mixer.Sound('src/wind.mp3')
wind_sound.set_volume(0.05)

# Słowniki przechowujące koordynaty każdego pola

positionsX = {0:40, 1:40, 2:40,  3:40,  4:40,  5:40, 6:40, 7:40, 8:40, 9:120,10:200,11:300,12:380,13:460,14:560,15:640,16:720,17:800,18:900,19:980,20:1060,21:1060,22:1060,23:1060,24:1060,25:1060,26:1060,27:1060,28:980,29:900,30:800,31:720,32:640,33:560,34:460,35:380,36:300,37:200,38:200,39:200,40:200,41:200,42:200,43:200,44:280,45:360,46:440,47:540,48:620,49:700,50:800,51:880,52:880,53:880,54:880,55:880,56:810,57:720,58:640,59:550,60:460,61:370,62:370,63:370,64:440,65:530,66:620,67:700,68:780}
positionsY = {0:10, 1:70, 2:150, 3:210, 4:290, 5:360,6:430,7:500,8:570,9:570,10:570,11:570,12:570,13:570,14:570,15:570,16:570,17:570,18:570,19:570,20:570,21:500,22:430,23:360,24:290,25:210,26:150,27:70,28:70,29:70,30:70,31:70,32:70,33:70,34:70,35:70,36:70,37:70,38:130,39:200,40:270,41:360,42:430,43:500,44:500,45:500,46:500,47:500,48:500,49:500,50:500,51:500,52:440,53:370,54:300,55:200,56:200,57:200,58:200,59:200,60:200,61:200,62:280,63:350,64:350,65:350,66:350,67:350,68:350}
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
        player1Jailed = game_state['player1Jailed']
        player2Jailed = game_state['player2Jailed']
        player1_nickname = game_state['player1_nickname']
        player2_nickname = game_state['player2_nickname']
        player1_turns = game_state['player1_turns']
        player2_turns = game_state['player2_turns']
        print("Loaded saved game.")
except FileNotFoundError:
    #Jeżeli nie ma zapisu to ustawia zmienne na zmienne startowe
    player1_nickname = input(str("Player 1 please enter your nickname: "))
    player2_nickname = input(str("Player 2 please enter your nickname: "))
    player1Jailed = 0
    player2Jailed = 0
    player1_position = 0
    player2_position = 0
    currentPlayer = player1
    gameEnded = False
    gameStarted = True
    diceRolled = False 
    player1_turns = 0
    player2_turns = 0
soundtrack.play(-1)