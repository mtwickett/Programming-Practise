import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper, (s)cissors, (q)uit')
        human_move = input()
        if human_move == 'q':
            sys.exit()
        if human_move == 'r' or human_move == 'p' or human_move == 's':
            break
        print('Please type one of r, p, s, or q')

    #display what the player chose
    if human_move == 'r':
        print('ROCK versus...')
    elif human_move == 'p':
        print('PAPER versus...')
    elif human_move == 's':
        print('SCISSORS versus...')

    #display what the computer chose
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_num == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_num == 3:
        computer_move = 's'
        print('SCISSORS')
 
    #display or record the win/loss
    if human_move == computer_move:
        print('It\'s a tie!')
        ties += 1
    elif human_move == 'r' and computer_move == 'p':
        print('Computer Wins!')
        losses += 1
    elif human_move == 'r' and computer_move == 's':
        print('Human Wins!')
        wins += 1
    elif human_move == 'p' and computer_move == 'r':
        print('Human Wins!')
        wins += 1
    elif human_move == 'p' and computer_move == 's':
        print('Computer Wins!')
        losses += 1
    elif human_move == 's' and computer_move == 'r':
        print('Computer Wins!')
        losses += 1
    elif human_move == 's' and computer_move == 'p':
        print('Human Wins!')
        wins += 1
