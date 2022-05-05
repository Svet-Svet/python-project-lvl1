from brain_games.engine import run_game
from brain_games.utilities import get_random_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def get_answer_and_question():
    number = get_random_number()
    result = is_even(number)
    return result, number


def start_game_parity():
    run_game(get_answer_and_question, QUESTION)
