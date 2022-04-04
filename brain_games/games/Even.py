#!/usr/bin/env python
import prompt
from python-project-lvl1.brain_games.utilits import start_game
from utilits import get_number
from utilits import round_count



def get_game_parity():
    start_game()

    for _ in range(round_count):
        num = get_number()
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
    get_game_parity()


if __name__ == '__main__':
    main()
