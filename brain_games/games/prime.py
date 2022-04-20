#!/usr/bin/env python
from brain_games.utilits import run_game, get_random_number


QUESTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def specification_for_get_game_prime():
    number = get_random_number()
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
            break
    if count <= 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def build_game_prime():
    run_game(specification_for_get_game_prime, QUESTION)
