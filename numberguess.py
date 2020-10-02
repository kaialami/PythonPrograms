import random, sys

random = random.randint(1, 100)
even = "\nThe number I'm thinking of is even. "
odd = "\nThe number I'm thinking of is odd. "
guess = '\nWhat number am I thinking of? Enter a whole number between (and including) 1 and 99: '
strRandom = str(random)
toohigh = '\nYour guess is too high.'
toolow = '\nYour guess is too low.'
count = 1
lessthanzero = '\nYour guess must be greater than 0. '

print('\nGuess what number I\'m thinking of! \nYou start with 5 points. Every wrong guess will lose you a point.')
print('Try and stay above 0 points!')


if random % 2 == 0:
    print(even)
    answer = eval(input(guess))

else:
    print(odd) 
    answer = eval(input(guess))

if answer <= 0:
    print(lessthanzero)
    answer = eval(input(guess))

if answer > 99:
    print('That number is out of range.')
    answer = eval(input(guess))


strAnswer = str(answer)

if answer == random:
    print('\nWow, first try! The number I was thinking of is ' + strRandom + '. You finished with all 5 points!')
    sys.exit(0)

elif answer > random:
    print(toohigh + '\n')

else:
    print(toolow + '\n')


if random > 9:
    print('My number has a ' + strRandom[1] + ' in its rightmost digit. ')
    answer = eval(input(guess))

else:
    print('My number has a ' + strRandom[0] + ' in its rightmost digit. ')
    answer = eval(input(guess))

if answer <= 0:
    print(lessthanzero)
    answer = eval(input(guess))
    
if answer > 99:
    print('That number is out of range.')
    answer = eval(input(guess))

while answer != random:

    if answer <= 0:
        print(lessthanzero)
        answer = eval(input(guess))
   
    if answer > 99:
        print('That number is out of range.')
        answer = eval(input(guess))
    
    elif answer > random:
        print(toohigh)
        answer = eval(input(guess))
        count = count + 1
    
    else:
        print(toolow)
        answer = eval(input(guess))
        count = count + 1
        


if answer == random:
    count = count + 1
    points = 5 - (count - 1)
    pointstatement = 'You ended with ' + str(points) + ' points.'
    print('\nYou guessed it! My number was ' + strRandom + '. You took ' + str(count) + ' tries to guess correctly.')
    
    if points > 0 :
        print(pointstatement + ' You guessed the number while still in the green! Looks like you win this time.')
    else:
        print(pointstatement + ' Oh no, you ran out of points! I guess I win.')
        
         
    
    

