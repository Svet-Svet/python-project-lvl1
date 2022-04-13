#!/usr/bin/env python
from random import randint
import prompt

ROUND_COUNT = 3


def get_number():
    return randint(1, 100)


def start_game(specific_game, QUESTION):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)

    for _ in range(ROUND_COUNT):
        result, question = specific_game()
        print(f'Question: {question}!')
        your_answer = prompt.string('Your answer: ')

        if your_answer == result:
            print('Correct!')
        else:
            print(
                f'"{your_answer}" is wrong answer ;( '
                f'Correct answer is "{result}".'
            )
            print(f"Let's try again, {name}!")
            return
        print(f'Congratulations, {name}!')
