#!/usr/bin/env python
from brain_games.utilits import get_game, get_random_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_parity():
    number = get_random_number()
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def start_game_parity():
    get_game(get_game_parity, QUESTION)
