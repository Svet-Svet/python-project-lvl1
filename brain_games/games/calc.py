#!/usr/bin/env python
import random
from brain_games.utilits import get_game, get_random_number

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_sign():
    math_list = ['-', '+', '*']
    return random.choice(math_list)


def get_game_calc():
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
    return str(result), question


def start_game_calc():
    get_game(get_game_calc, QUESTION)
