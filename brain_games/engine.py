import prompt

ROUNDS_COUNT = 3


def run_game(get_specific_game, game_task):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_task)

    for _ in range(ROUNDS_COUNT):
        result, question = get_specific_game()
        print(f'Question: {question}!')
        user_answer = prompt.string('Your answer: ')

        if user_answer == result:
            print('Correct!')
        else:
            print(
                f'"{user_answer}" is wrong answer ;( '
                f'Correct answer is "{result}".'
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
