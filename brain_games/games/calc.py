#!/usr/bin/env python
import random
from brain_games.utilits import run_game, get_random_number

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MATH_LIST = ['-', '+', '*']


def get_sign():
    return random.choice(MATH_LIST)


def specification_for_get_game_calc():
    number1 = get_random_number()
    number2 = get_random_number()
    sign = get_sign()
    question = f'{number1} {sign} {number2}'

    if sign == '-':
        result = number1 - number2
    elif sign == '+':
        result = number1 + number2
    elif sign == '*':
        result = number1 * number2
    else:
        raise Exception('<Попробуйте еще раз>')
    return str(result), question


def build_game_calc():
    run_game(specification_for_get_game_calc, QUESTION)
