from enum import Enum


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    MAIN = 1
    FOOD = 2
    EXERCISE = 3
    SMOKE = 4
    AGE = 5

game_state = {'state': GameState.TITLE}

def ChangeGamestate(old_gamestate, new_gamestate):
    old_gamestate['state'] = new_gamestate
