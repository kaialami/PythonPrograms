import sys

feet = eval(input('Enter a value in feet: '))
inches = eval(input('Enter a value in inches: '))

isOneFt = False
isOneInch = False

isFloatFt = isinstance(feet, float)
isFloatInch = isinstance(inches, float)

print('')

if isFloatFt == True or isFloatInch == True:
    print('Enter a whole number for each value.')
    sys.exit(0)

if feet < 0 or inches < 0:
    print('Enter a positive number for feet and inches.')


decimal = inches / 12

answer = str(float(feet) + decimal)

if feet == 1:
    isOneFt = True

if inches == 1:
    isOneInch = True

stringFeet = str(feet)
stringInches = str(inches)

if isOneFt == True and isOneInch == True:
    print(stringFeet + ' foot and ' + stringInches + ' inch is equal to ' + answer)
if isOneFt == True and isOneInch == False:
    print(stringFeet + ' foot and ' + stringInches + ' inches is equal to ' + answer)
if isOneFt == False and isOneInch == True:
    print(stringFeet + ' feet and ' + stringInches + ' inch is equal to ' + answer)
else:
    print(stringFeet + ' feet and ' + stringInches + ' inches is equal to ' + answer)
    


