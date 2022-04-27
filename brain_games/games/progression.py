from brain_games.utilits import run_game, get_random_number
from random import randint


QUESTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def build_game_progression():
    first_number = get_random_number()
    difference = get_random_number()
    missed_element_index = randint(0, PROGRESSION_LENGTH - 1)
    progression = str()
    result = int()
    for i in range(PROGRESSION_LENGTH):
        number = first_number + i * difference
        if i == missed_element_index:
            progression += ' ..'
            result = number
        else:
            progression += ' ' + str(number)
    question = progression.lstrip()
    return str(result), question


def start_game_progression():
    run_game(build_game_progression, QUESTION)
