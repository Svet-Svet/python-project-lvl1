#!/usr/bin/env python
import math
from brain_games.utilits import get_game, get_random_number


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_game_gcd():
    number1 = get_random_number()
    number2 = get_random_number()
    question = f'{number1} {number2}'

    result = math.gcd(number1, number2)
    return str(result), question


def start_game_gcd():
    get_game(get_game_gcd, QUESTION)
