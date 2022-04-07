#!/usr/bin/env python
from brain_games.utilits import start_game, get_number


def get_question():
    print('What number is missing in the progression?')


def get_game_progression():
    first_num = get_number()
    difference = get_number(1, 5)
    progression_length = 10

    def get_progression(first_num, difference, progression_length):
        result = ''
        i = first_num

        while 
    print(f'Question: {num}!')
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def main():
    start_game(get_game_progression, get_question)


if __name__ == '__main__':
    main()

