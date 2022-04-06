#!/usr/bin/env python
from random import randint
import prompt


def get_number():
    num = randint(1, 100)
    return num


round_count = 3


def start_game(specific_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(round_count):
        result = specific_game()
        your_answer = prompt.string('Your answer: ')

        if your_answer == result:
            print('Correct!')
        else:
            print(
                f'"{your_answer}" is wrong answer ;( '
                f'Correct answer is "{result}".'
            )
            print(f"Let's try again, {name}")
            break
        print(f'Congratulations, {name}!')