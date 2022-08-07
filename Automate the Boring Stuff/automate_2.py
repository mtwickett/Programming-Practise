from random import randint

computer_number = randint(1, 10)
guess = int(input('I\'m thinking of a number between 1 and 20.\nTake a guess: '))
number_of_guesses = 1

while True:
    if guess == computer_number:
        if number_of_guesses == 1:
            print('Good Job! You guessed my number in 1 guess.')
            break
        else:
            print(f'Good Job! You guessed my number in {number_of_guesses} guesses.')
            break
    
    elif guess < computer_number:
        guess = int(input('You\'re guess is too low.\nTake another guess: '))
        number_of_guesses += 1
        continue
    
    elif guess > computer_number:
        guess = int(input('You\'re guess is too high.\nTake another guess: '))
        number_of_guesses += 1
        continue
