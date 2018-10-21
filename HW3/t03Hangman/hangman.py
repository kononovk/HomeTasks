from random import randint
from HW3.t03Hangman.hangman_logic import get_guessed_word, is_word_guessed
from termcolor import colored
from string import ascii_lowercase


def rand_word_gen(filename):
    with open(filename) as file:
        words = [row.strip() for row in file]
    random_word = words[randint(0, len(words) - 1)]
    return random_word


def letter_input():
    temp_character = input("Choose the next letter: ")
    if temp_character.lower() not in set(ascii_lowercase):
        print("You must input only latin letters")
        temp_character = input("Choose the next letter: ")
    return temp_character


def choose_complexity(word):
    complexity = int(input("1-Easy, 2-Medium, 3-Hard\nPlease, choose the complexity:"))
    while complexity not in {1, 2, 3}:
        print("The number of complexity must be 1, 2 or 3")
        complexity = int(input("1-Easy, 2-Medium, 3-Hard\nPlease, choose the complexity:\n"))
    attempts = len(word) * (4 - complexity)
    return attempts


if __name__ == '__main__':
    secret_word = rand_word_gen("words.txt")
    available_letters = set(secret_word)
    used_letters = set()
    num_of_attempts = choose_complexity(secret_word)

    print(colored("---------------------------", "green"))
    while not is_word_guessed(secret_word, used_letters) and num_of_attempts > 0:
        print("You have got {} attempts".format(num_of_attempts))
        print("Word: " + colored(get_guessed_word(secret_word, used_letters), "green"))
        curr_letter = letter_input().lower()
        if curr_letter not in available_letters:
            print("You didn't guess\n")
            num_of_attempts -= 1
        else:
            print()
            used_letters.add(curr_letter)
            available_letters.discard(curr_letter)

    print()
    if num_of_attempts <= 0:
        print("You lose, I pour your wine into the sink\nThe word was " + colored(secret_word, "green"))
    else:
        print(colored("Congratulations you won!!!", "yellow"))
