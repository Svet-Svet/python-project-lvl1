from brain_games.engine import run_game
from brain_games.utilities import get_random_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


def get_answer_and_question():
    number = get_random_number()
    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return result, number


def start_game_parity():
    run_game(get_answer_and_question, QUESTION)
