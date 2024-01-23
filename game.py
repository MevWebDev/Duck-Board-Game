import pygame, random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png')
background = pygame.transform.scale(background, (1280, 720))
player1 = pygame.image.load('src/player1.png')
player1 = pygame.transform.scale(player1, (75, 75))
player2 = pygame.image.load('src/player2.png')
player2 = pygame.transform.scale(player2, (75, 75))
gameStarted = True
positionsX = {0:40, 1:40, 2:40,  3:40,  4:40,  5:40, 6:40, 7:40, 8:40, 9:120,10:200,11:300,12:380,13:460,14:560,15:640,16:720,17:800,18:900,19:980,20:1060,21:1060,22:1060,23:1060,24:1060,25:1060,26:1060,27:1060,28:980,29:900,30:800,31:720,32:640,33:560,34:460,35:380,36:300,37:200,38:200,39:200,40:200,41:200,42:200,43:200,44:280,45:360,46:440,47:540,48:620,49:700,50:800,51:880,52:880,53:880,54:880,55:880,56:810,57:720,58:640,59:550,60:460,61:370,62:370,63:370,64:440,65:530,66:620,67:700,68:780}
positionsY = {0:10, 1:70, 2:150, 3:210, 4:290, 5:360,6:430,7:500,8:570,9:570,10:570,11:570,12:570,13:570,14:570,15:570,16:570,17:570,18:570,19:570,20:570,21:500,22:430,23:360,24:290,25:210,26:150,27:70,28:70,29:70,30:70,31:70,32:70,33:70,34:70,35:70,36:70,37:70,38:130,39:200,40:270,41:360,42:430,43:500,44:500,45:500,46:500,47:500,48:500,49:500,50:500,51:500,52:440,53:370,54:300,55:200,56:200,57:200,58:200,59:200,60:200,61:200,62:280,63:350,64:350,65:350,66:350,67:350,68:350}
player1_position = 61
player2_position = 61
diceRolled = False
currentPlayer = player1

def rollDice():
    # number = random.randint(1, 6)
    number = 1
    return number

def move(player, number):
    if player == player1:
        screen.blit(player, (positionsX[number]+40, positionsY[number]))
    elif player == player2:
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
            if event.key == pygame.K_SPACE and not diceRolled:
                diceRolled = True
                if currentPlayer == player1:
                    player1_position += rollDice()
                    currentPlayer = player2
                else:
                    player2_position += rollDice()
                    currentPlayer = player1
                screen.blit(background, (0, 0))
            move(player1, player1_position)
            move(player2, player2_position)    
                 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                diceRolled = False  # Allow rolling again after release

    pygame.display.update()
    clock.tick(60)
