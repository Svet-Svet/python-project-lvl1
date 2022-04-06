#!/usr/bin/env python
from brain_games.utilits import start_game, get_number


def get_game_parity():
    num = get_number()
    print(f'Question: {num}!')
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def main():
    start_game(get_game_parity)


if __name__ == '__main__':
    main()
