#!/usr/bin/env python
from brain_games.utilits import start_game, get_number


get_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_parity():
    num = get_number()
    print(f'Question: {num}!')
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def main():
    start_game(get_game_parity, get_question)


if __name__ == '__main__':
    main()
