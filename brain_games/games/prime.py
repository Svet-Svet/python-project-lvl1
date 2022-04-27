from brain_games.utilits import run_game, get_random_number

QUESTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime():
    number = get_random_number()
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
            break
    if count <= 0:
        result = True
    else:
        result = False
    return result, number


def get_answer_and_question_game_prime():
    result, number = is_prime()
    if result:
        result = 'yes'
    else:
        result = 'no'
    return result, number


def start_game_prime():
    run_game(get_answer_and_question_game_prime, QUESTION)
