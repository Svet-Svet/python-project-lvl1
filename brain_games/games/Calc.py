#!/usr/bin/env python
import random
from brain_games.utilits import start_game, get_number


def get_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_game_calc():
    def get_sign():
        math_list = ["-", "+", "*"]
        random_index = random.choice(math_list)
        return random_index

    num1 = get_number(1, 5)
    num2 = get_number(1, 5)
    sign = get_sign()
    question = f'{num1} {sign} {num2}'
    print(f'Question: {question}!')

    if sign == '-':
        result = num1 - num2
    elif sign == '+':
        result = num1 + num2
    elif sign == '*':
        result = num1 * num2
    return str(result)


def main():
    start_game(get_game_calc, get_question)


if __name__ == '__main__':
    main()
