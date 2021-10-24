from Hangman_Words import words_in_a_list
import random
import string

print(words_in_a_list)


def get_valid_word(words):
    word = random.choice(words_in_a_list)
    while '-' in word or ' ' in words_in_a_list:  # the or keyword is adding a second piece of logic to the previous
        word = random.choice(words_in_a_list)    # then the second "in" keyword is exercised on the earlier logic
    return word.upper()


def hangman_game():
    word = get_valid_word(words_in_a_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    # guess_count = 0
    # guess_limit = 6  could use these it would make the code longer but more understandable
    # out_of_guesses = True
    lives = 6
    while len(word_letters) > 0 and lives != 0:
        print(f"You have {lives} lives left. You have used the Letters:", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))
        user_letter = input("Pick a letter from A to Z:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('That letter is not in the word.')
        elif user_letter in used_letters:
            print("You have already guessed that letter.")
        else:
            print("Invalid Character")
    if lives == 0:
        print("You have no lives left. Wanna play again?")
    else:
        print(f"You have guessed the word {word} correctly.")


# This is some code that could be used for the version I was going to make that would have been longer, I need to slow
# down plan and think more.
#     if user_letter not in word:
#         guess_count += 1
#     else:
#       print("Take another guess.")
#         if guess_count == guess_limit:
#             print("Your are out of guesses.")
hangman_game()

