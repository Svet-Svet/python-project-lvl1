import prompt

ROUNDS_COUNT = 3


def run_game(get_specific_game, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)

    for _ in range(ROUNDS_COUNT):
        result, numbers_for_game = get_specific_game()
        print(f'Question: {numbers_for_game}!')
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
