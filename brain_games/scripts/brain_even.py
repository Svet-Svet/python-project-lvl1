#!/usr/bin/env python
from random import randint
import prompt


# def welcome_user():
#    name = prompt.string('May I have your name? ')
#    print(f'Hello, {name}!')


# def is_even():
#    num = get_number()
#    return num % 2 == 0


# def right_answer():
#    return 'yes' if is_even() == True else 'no'


# def get_question():
#    your_answer = prompt.string('Your answer: ')
#    return your_answer

round_count = 3


def get_number():
    num = randint(1, 100)
    return num


def get_game_parity():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

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
            print(f"Let's try again, {name}")
            break
        print(f'Congratulations, {name}!')


def main():
    get_game_parity()


if __name__ == '__main__':
    main()
