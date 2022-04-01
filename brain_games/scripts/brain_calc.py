#!/usr/bin/env python
import random
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

rounds_count = 3


def get_number():
    num = randint(1, 100)
    return num


def get_sign():
    math_list = ["-", "+", "*"]
    random_index = random.choice(math_list)
    return random_index


def get_game_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    for _ in range(rounds_count):
        num1 = get_number()
        num2 = get_number()
        sign = get_sign()
        question = f'{num1} {sign} {num2}'

        if sign == '-':
            answer = num1 - num2
        elif sign == '+':
            answer = num1 + num2
        elif sign == '*':
            answer = num1 * num2

        print(f'Question: {question}!')
        your_answer = prompt.string('Your answer: ')

        if your_answer == str(answer):
            print('Correct!')
        else:
            print(
                f'"{your_answer}" is wrong answer ;( '
                f'Correct answer is "{answer}".'
            )
            print(f"Let's try again, {name}")
            break
        print(f'Congratulations, {name}!')


def main():
    get_game_calc()


if __name__ == '__main__':
    main()
