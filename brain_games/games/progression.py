#!/usr/bin/env python
from brain_games.utilits import get_game, get_random_number
from random import randint


QUESTION = 'What number is missing in the progression?'


def get_game_progression():
    first_number = get_random_number()
    difference = get_random_number()
    progression_length = 10
    missed_element = randint(0, progression_length - 1)
    progression = str()
    result = str()
    for i in range(progression_length):
        number = first_number + i * difference
        if i == missed_element:
            progression += ' ..'
            result = number
        else:
            progression += ' ' + str(number)
    question = progression[1:]
    return str(result), question


def start_game_progression():
    get_game(get_game_progression, QUESTION)
