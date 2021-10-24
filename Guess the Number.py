import random

# Guess the Number computer


def guess(x):
    random_number = random.randint(1, x)
    _guess = 0
    while _guess != random_number:
        _guess = int(input(f'Guess a number between 1 and {x} my friend:'))
        print(_guess)
        if _guess == random_number:
            print("That was it my dude")
        elif _guess < random_number:
            print("Too low.")
        elif _guess > random_number:
            print("Thats too high")


# Guess the Number User


def computer_guess(c):  # Hey future Daniel this needs a parameter
    low = 1
    high = c
    feedback = ''
    another_guess = ''
    while feedback != "s":
        if low != high:
            another_guess = random.randint(low, high)
        else:
            another_guess = low
        feedback = input(f'Is {another_guess} too high (H), too low (L) or just right (s)?:').lower()
        if feedback == 'h':
            high = another_guess - 1
        elif feedback == "l":
            low = another_guess + 1
    print(f'Yay the computer guessed the number {another_guess} correctly, no way!!')


computer_guess(100)
guess(10)


num = 1
while num <= 5:
    print(num)
    num += 1


# number = 22
# running = True
# guess = ''
# while running and guess is not number:  # have to make use of logical, membership and identity operator keywords in
#     guess = int(input('Enter an integer between 0 and 25 : '))  # loop and logical code blocks
#     if guess == number:
#         print('Congratulations, you guessed it.')  # this causes the while loop to stop, running = False
#     elif guess < number:
#         print('No, it is a little higher than that.')
#     if guess > number:
#         print('No, it is a little lower than that.')
# if guess == number:
#     running = False


secret_word = 'Mouse'
guess = ''
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('Enter your guess:')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Game over')
else:
    print('you win!!')

print(random.randint(1, 100000))
