#!/usr/bin/env python
from brain_games.utilits import get_game, get_random_number


QUESTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def get_game_prime():
    number = get_random_number()
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count <= 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def start_game_prime():
    get_game(get_game_prime, QUESTION)
