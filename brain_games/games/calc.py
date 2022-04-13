#!/usr/bin/env python
import random
from brain_games.utilits import start_game, get_number

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_sign():
    math_list = ['-', '+', '*']
    random_index = random.choice(math_list)
    return random_index


def get_game_calc():
    num1 = get_number()
    num2 = get_number()
    sign = get_sign()
    question = f'{num1} {sign} {num2}'

    if sign == '-':
        result = num1 - num2
    elif sign == '+':
        result = num1 + num2
    elif sign == '*':
        result = num1 * num2
    return str(result), question


def main():
    start_game(get_game_calc, QUESTION)
