import random

print('Think of a number between (and including) 1 and 100\nI will ask 5 questions about your number.\nIf I can\'t guess it, you win!')

error = '\nEnter either a yes or no. '

yn = "[yes or no]: "
yes = 'yes'
no = 'no'

q1 = 'Is your number even? '
q2 = 'Is your number greater than or equal to 50? '
q3 = 'Is your number divisible by '
q4 = 'Is the leftmost digit of your number '
q5 = 'Is the rightmost digit of your number '


num = list(range(1, 101))

# q1
inp = str(input(q1 + yn)).lower().strip(' ')

while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input(q1 + yn)).lower().strip(' ')

if inp == yes:
    for x in num:
        if x % 2 == 1:
            num.remove(x)
    ognum = num
    div = '4'
    rd1 = 4
    rd2 = 6
            
else:
    for x in num:
        if x % 2 == 0:
            num.remove(x)
    ognum = num
    div = '3'
    rd1 = 3
    rd2 = 5

first = ognum[0]

# q2
inp = str(input(q2 + yn)).lower().strip(' ')

while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input(q1 + yn)).lower().strip(' ')

if inp == yes:
    if first == 2:
        num = ognum[25- 1 :]
    else:
        num = ognum[25 :]
    ld1 = 6
    ld2 = 8
    
else:
    if first == 2:
        num = ognum[: 25 - 1]
    else:
        num = ognum[: 25]
    ld1 = 1
    ld2 = 3
    
# q3
q3 = q3 + div + '? '
        
inp = str(input(q3 +  yn)).lower().strip(' ')

while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input(q3 + yn)).lower().strip(' ')

if inp == yes:
    for x in num:
        if x % int(div) != 0:
            num.remove(x)

else:
    for x in num:
        if x % int(div) == 0:
            num.remove(x)

# q4
q4 = q4 + str(ld1) + ' or ' + str(ld2) + '? '

inp = str(input(q4 +  yn)).lower().strip(' ')

while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input(q4 + yn)).lower().strip(' ')

strNum = []
templist = []
intTemp = []

for x in num:
    strNum.append(str(x))

if inp == yes:
    for i in strNum:
        if i[0] == str(ld1):
            templist.append(i)
        elif i[0] == str(ld2):
            templist.append(i)

else:
    for i in strNum:
        if  i[0] == str(ld1) or  i[0] == str(ld2):
            continue
        else:
            templist.append(i)

for n in templist:
    intTemp.append(int(n))
num = intTemp
    
# q5
q5 = q5 + str(rd1) + ' or ' + str(rd2) + '? '   

inp = str(input(q5 +  yn)).lower().strip(' ')

while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input(q5 + yn)).lower().strip(' ')

strNum = []
templist = []
intTemp = []

for x in num:
    strNum.append(str(x))

if inp == yes:
    for i in strNum:
        if i[-1] == str(rd1) or i[-1] == str(rd2):
            templist.append(i)

else:
    for i in strNum:
        if i[-1] == str(rd1) or i[-1] == str(rd2):
            continue
        else:
            templist.append(i)

for n in templist:
    intTemp.append(int(n))
num = intTemp

print('\n' + str(num))
inp = str(input('Just to confirm, is your number in the list above? ' + yn)).lower().strip(' ')
    
while True:
    if inp == yes or inp == no:
        break
    
    else:
        print(error)
        inp = str(input('Just to confirm, is your number in this list? ' + yn)).lower().strip(' ')

if inp == no:
    print('Well, it looks like I made a mistake. You win... I guess...')

else:
    ask = 'Did I guess correctly? '
    guess1 = random.choice(num)
    num.remove(guess1)
    guess2 = random.choice(num)
    print('Ok, here\'s my guess: ' + str(guess1))
    
    ans = str(input(ask + yn)).lower().strip(' ')
    
    while True:
        if ans == yes or ans == no:
            break
        
        else:
            print(error)
            ans = str(input(ask + yn)).lower().strip(' ')
    
    if ans == yes:
        print('Wow, I guessed it correctly? Looks like I win!')
    
    else:
        print('Aw, I guessed incorrectly?')
        
        ans = str(input('Do you want to give me one last try? ' + yn)).lower().strip(' ')
        
        while True:
            if ans == yes or ans == no:
                break
            
            else:
                print(error)
                ans = str(input('Do you want to give me one last try? ' + yn)).lower().strip(' ')
        
        if ans == yes:
            print('Ok, here it is: ' + str(guess2))
            
            ans = str(input(ask + yn)).lower().strip(' ')
            
            while True:
                if ans == yes or ans == no:
                    break
                
                else:
                    print(error)
                    ans = str(input(ask + yn)).lower().strip(' ')
                    
            if ans == yes:
                print('Hey, second try. Not bad.')
            else:
                print('Seems like you beat me twice. Well played.')

    

            
