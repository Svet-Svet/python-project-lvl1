#!/usr/bin/env python
import brain_games.utilits
from brain_games.utilits import *


def get_game_parity():
    for _ in range(brain_games.utilits.round_count):
        num = brain_games.utilits.get_number()
        print(f'Question: {num}!')
        your_answer = prompt.string('Your answer: ')

        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        if your_answer == result:
            print('Correct!')
        else:
            print(
                f'"{your_answer}" is wrong answer ;( '
                f'Correct answer is "{result}".'
            )
            print(f"Let's try again, {start_game.__name__}")
            break
        print(f'Congratulations, {start_game.__name__}!')


def main():
    start_game(get_game_parity)


if __name__ == '__main__':
    main()
