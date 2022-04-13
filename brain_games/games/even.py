#!/usr/bin/env python
from brain_games.utilits import start_game, get_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_parity():
    num = get_number()
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, num


def main():
    start_game(get_game_parity, QUESTION)


if __name__ == '__main__':
    main()
