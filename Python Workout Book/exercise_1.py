import random

def guessing_game():
    random_number = random.randint(0,100)

    while True:
        guess = int(input('Guess a number between 0 and 100: '))

        if guess == random_number:
            print('Just right')
            break

        elif guess > random_number:
            print('Too high, please try again')
            continue

        else:
            print('Too low, please try again')
            continue

guessing_game()
