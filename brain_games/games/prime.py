from brain_games.utilits import run_game, get_random_number

QUESTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
            break
    return count > 0


def get_answer_and_question():
    number = get_random_number()
    result = is_prime(number)
    if result:
        result = 'no'
    else:
        result = 'yes'
    return result, number


def start_game_prime():
    run_game(get_answer_and_question, QUESTION)
