#!/usr/bin/env python
from random import randint
import prompt


def start_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_number():
    num = randint(1, 100)
    return num


round_count = 3


def main():
    start_game()
    get_number()


if __name__ == '__main__':
    main()
