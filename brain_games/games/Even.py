#!/usr/bin/env python
import brain_games.utilits
from brain_games.utilits import *


def get_game_parity():
    num = brain_games.utilits.get_number()
    print(f'Question: {num}!')
    result = ''
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def main():
    start_game(get_game_parity)


if __name__ == '__main__':
    main()
