import pygame, random,pickle,os
def save(gamestate):
        with open('savegame.pkl', 'wb') as f:
            pickle.dump(gamestate, f)
        print("Game saved!")
