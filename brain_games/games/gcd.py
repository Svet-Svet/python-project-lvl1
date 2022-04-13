#!/usr/bin/env python
import math
from brain_games.utilits import start_game, get_number


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_game_gcd():
    num1 = get_number()
    num2 = get_number()
    question = f'{num1} {num2}'

    result = math.gcd(num1, num2)
    return str(result), question


def main():
    start_game(get_game_gcd, QUESTION)


if __name__ == '__main__':
    main()
