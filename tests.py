from dice import rollDice
import pickle, os
from scoreboard import *
from moving import checkSquare
def test_roll():
    assert rollDice() in [1,2,3,4,5,6]
def test_sort():
    scoreboard = [{'player': 'Alice', 'score': 5}, {'player': 'Bob', 'score': 3}, {'player': 'Charlie', 'score': 7}]
    expected_result = [{'player': 'Bob', 'score': 3}, {'player': 'Alice', 'score': 5}, {'player': 'Charlie', 'score': 7}]
    result = bubblesort(scoreboard)
    assert result == expected_result
def test_returns_player_position():
    player_pos = 10
    dice_number = 4
    result = checkSquare(player_pos, dice_number)
    assert result == 10
def test_double():
    pos = 7
    dice = 3
    assert checkSquare(pos,dice) == 10

def test_ladder():
    pos = 47
    assert checkSquare(pos,0) == 65
