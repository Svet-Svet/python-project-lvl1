#!/usr/bin/env python
from random import randint
import prompt


#def welcome_user():
#    name = prompt.string('May I have your name? ')
#    print(f'Hello, {name}!')


def get_number():
    num = randint(1, 100)
    return num


def is_even():
    num = get_number()
    return num % 2 == 0


def get_question():
    your_answer = prompt.string('Your answer: ')
    return your_answer


def right_answer():
    return 'yes' if is_even() == True else 'no'


def get_game_parity():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 1

    while rounds_count <= 3:
        print(f'Question: {get_number()}!')
        print(f'{get_question()}')

        if get_question() == right_answer():
            print('Correct!')
            rounds_count += 1
        else:
            print(f'"{get_question()}" is wrong answer ;( Correct answer is "{right_answer()}".')
            print(f"Let's try again, {name}")
            break
        if rounds_count == 3:
            print(f'Congratulations, {name}!')


def main():
    get_game_parity()

if __name__ == '__main__':
    main()
