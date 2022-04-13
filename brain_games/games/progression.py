#!/usr/bin/env python
from brain_games.utilits import start_game, get_number
from random import randint


QUESTION = 'What number is missing in the progression?'


def get_game_progression():
    first_num = get_number()
    difference = get_number()
    progression_length = 10
    missed_element = randint(0, progression_length - 1)
    num = str()
    result = ''
    for i in range(progression_length):
        number = first_num + i * difference
        if i == missed_element:
            num += ' ..'
            result = number
        else:
            num += ' ' + str(number)
    question = num[1:]
    return str(result), question


def main():
    start_game(get_game_progression, QUESTION)
