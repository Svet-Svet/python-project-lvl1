#!/usr/bin/env python
import math
from brain_games.utilits import start_game, get_number


get_question = 'Find the greatest common divisor of given numbers.'


def get_game_gcd():
    num1 = get_number()
    num2 = get_number()
    question = f'{num1} {num2}'
    print(f'Question: {question}!')

    result = math.gcd(num1, num2)
    return str(result)


def main():
    start_game(get_game_gcd, get_question)


if __name__ == '__main__':
    main()