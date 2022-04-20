#!/usr/bin/env python
import math
from brain_games.utilits import run_game, get_random_number


QUESTION = 'Find the greatest common divisor of given numbers.'


def specification_for_get_game_gcd():
    number1 = get_random_number()
    number2 = get_random_number()
    question = f'{number1} {number2}'

    result = math.gcd(number1, number2)
    return str(result), question


def build_game_gcd():
    run_game(specification_for_get_game_gcd, QUESTION)
