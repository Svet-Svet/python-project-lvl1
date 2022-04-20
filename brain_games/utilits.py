#!/usr/bin/env python
from random import randint
import prompt

ROUND_COUNT = 3
FIRST_NUMBER_FOR_RANDOM = 1
FINAL_NUMBER_FOR_RANDOM = 100


def get_random_number():
    return randint(FIRST_NUMBER_FOR_RANDOM, FINAL_NUMBER_FOR_RANDOM)


def run_game(specific_game, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)

    for _ in range(ROUND_COUNT):
        result, question_number = specific_game()
        print(f'Question: {question_number}!')
        user_answer = prompt.string('Your answer: ')

        if user_answer == result:
            print('Correct!')
        else:
            print(
                f'"{user_answer}" is wrong answer ;( '
                f'Correct answer is "{result}".'
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
