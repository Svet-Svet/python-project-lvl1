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


def get_number():
    num = randint(1, 100)
    return num


def get_game_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    rounds_count = 1

    while rounds_count <= 3:
        num1 = get_number()
        num2 = get_number()
        answer = f'{num1} + {num2}'
        true_answer = str(num1 + num2)
        print(f'Question: {answer}!')
        your_answer = prompt.string('Your answer: ')

        if your_answer == true_answer:
            print('Correct!')
            rounds_count += 1
        else:
            print(f'"{your_answer}" is wrong answer ;( Correct answer is "{true_answer}".')
            print(f"Let's try again, {name}")
            break
        print(f'Congratulations, {name}!')


def main():
    get_game_calc()


if __name__ == '__main__':
    main()
