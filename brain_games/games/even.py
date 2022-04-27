from brain_games.utilits import run_game, get_random_number


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer_and_question_game_parity():
    number = get_random_number()
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def start_game_parity():
    run_game(get_answer_and_question_game_parity, QUESTION)
