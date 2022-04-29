import random
from brain_games.utilits import run_game, get_random_number

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MATH_SIGNS = ['-', '+', '*']


def get_sign():
    return random.choice(MATH_SIGNS)


def get_answer_and_question():
    number1 = get_random_number()
    number2 = get_random_number()
    sign = get_sign()
    question = f'{number1} {sign} {number2}'

    if sign == '-':
        result = number1 - number2
    elif sign == '+':
        result = number1 + number2
    elif sign == '*':
        result = number1 * number2
    else:
        raise Exception('<This sign is not supported>')
    return str(result), question


def start_game_calc():
    run_game(get_answer_and_question, QUESTION)
