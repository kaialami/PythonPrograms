import random

while True:
    ask = 'Rock, paper, scissors: '
    inp = str(input(ask)).lower()
    
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    error = 'Enter one of the following. '
    
    ans = random.randint(0, 3)
    
    while True:
        if inp == r or inp == p or inp == s:
            break
        else:
            inp = str(input(error + ask))
    
    if inp == r:
        num = 0
    
    elif inp == p:
        num = 1
    
    else:
        num = 2
    
    if num == ans:
        print('Tie')
        continue
    
    if num == 0:
        if ans == 1:
            print('Paper. You lose.')
        else:
            print('Scissors. You win.')
    
    elif num == 1:
        if ans == 0:
            print('Rock. You win.')
        else:
            print('Scissors. You lose.')
    
    else:
        if ans == 0:
            print('Rock. You lose.')
        else:
            print('Paper. You win.')
        
    again = str(input('Play again? ([y] n): ')).lower()
    y = 'y'
    n = 'n'
    if again == 'yes':
        again = y
    elif again == 'no':
        again = n
        
    while True:
        if again == y or again == n:
            break
        else:
            again = str(input(error + 'Play again? ([y] n): ')).lower()
            if again == 'yes':
                again = y
            elif again == 'no':
                again = n
        
    if again == y:
        continue
    else:
        break
        