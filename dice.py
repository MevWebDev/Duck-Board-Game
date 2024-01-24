import pygame, random,pickle,os
from sys import exit
from init import *
def rollDice():
    number = random.randint(1, 6)
    rollsound.play()
    showDice(number)
    return number
# Funkcja wyświetlająca kostkę
def showDice(number):
    match number:
        case 1:
            dice = pygame.image.load('src/dice1.png')
        case 2:
            dice = pygame.image.load('src/dice2.png')
        case 3:
            dice = pygame.image.load('src/dice3.png')
        case 4:              
            dice = pygame.image.load('src/dice4.png')
        case 5:
            dice = pygame.image.load('src/dice5.png')
        case 6:
            dice = pygame.image.load('src/dice6.png')
    dice = pygame.transform.scale(dice, (60, 60))
    screen.blit(dice,(1200,20))