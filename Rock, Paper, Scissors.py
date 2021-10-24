import random


def sweeeet_sweeeet_sweet_victory(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        print("Awwwww yeah baby ur on stable cleaning duty.")


def we_have_lost_sire(player, opponent):
    if (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') or (player == 'r' and opponent == 'p'):
        print("oh no oh no oh no no no no")


def play():
    possible_choices = ['r', 'p', 's']
    user = input("'r' for rock, 'p' for paper and 's' for scissors:")
    computer = random.choice(possible_choices)
# logic can go r>s, s>p, p>r or p<s, s<r, r<p
    if user == computer:
        print("Bitch that won't work we gotta play again.")
    if sweeeet_sweeeet_sweet_victory(user, computer):
        pass
    if we_have_lost_sire(user, computer):
        pass


play()
