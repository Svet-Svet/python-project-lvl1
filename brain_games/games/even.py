#!/usr/bin/env python
from brain_games.utilits import run_game, get_random_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def specification_for_get_game_parity():
    number = get_random_number()
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def build_game_parity():
    run_game(specification_for_get_game_parity, QUESTION)
