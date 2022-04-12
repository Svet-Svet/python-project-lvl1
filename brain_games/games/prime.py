#!/usr/bin/env python
from brain_games.utilits import start_game, get_number


get_question = 'Answer "yes" if the number is prime, otherwise answer "no".'


def get_game_prime():
    num = get_number()
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count <= 0:
        result = 'yes'
    else:
        result = 'no'
    return result, num


def main():
    start_game(get_game_prime, get_question)


if __name__ == '__main__':
    main()
