from random import randint

FIRST_NUMBER_FOR_RANDOM = 1
FINAL_NUMBER_FOR_RANDOM = 100


def get_random_number():
    return randint(FIRST_NUMBER_FOR_RANDOM, FINAL_NUMBER_FOR_RANDOM)
