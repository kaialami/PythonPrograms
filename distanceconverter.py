import sys

original = eval(input('Enter a measurement value you wish to convert: '))
unit1 = (input("What is the number's unit? Enter the unit in quotation marks. (mm, cm, m or km): "))
unit2 = (input('What unit do you want to convert it into? Enter the unit in quotation marks. (mm, cm, m or km): '))

isString1 = isinstance(unit1, str)
isString2 = isinstance(unit2, str)

if isString1 == False or isString2 == False:
    print('Enter both units within quotation marks.')
    sys.exit(0)

elif unit1 != 'mm' or unit1 != 'cm' or unit1 != 'm' or unit1 != 'km':
    print('Enter one of the units listed above.')
    sys.exit(0)
    
if unit2 != 'mm' or unit2 != 'cm' or unit2 != 'm' or unit2 != 'km':
    print('Enter one of the units listed above.')
    sys.exit(0)

if unit1 == unit2:
    print('The conversion is already complete ya dingus.')
    sys.exit(0)

if unit1 == 'mm':
    mm1 = unit1
if unit1 == 'cm':
    cm1 = unit1
    
# Incomplete