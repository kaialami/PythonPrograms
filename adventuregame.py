name = str(input('Character Name: '))
print('')

# Choose your character's class
print('Character Classes: ')
classes = {
    1:'Knight',
    2:'Magician',
    3:'Theif',
    4:'Cleric',
    5:'Ranger'
}
for num, clss in classes.items():
    info = ''
    if num == 1:
        info = ' - Exceeds in physical combat and can take hits easily. Wields a sword and shield.'
    if num == 2:
        info = ' - Master of elemental magic. Able to dish out massive damage but can be frail. Wields a tome of fire and ice.'
    if num == 3:
        info = ' - Excellent speed and stealth, but not great at one-to-one combat. Wields two knives.'
    if num == 4:
        info = ' - Possesses the ability to heal while fighting with light magic. Not especially agile. Wields a magic staff.'
    if num == 5:
        info = ' - Agile archer with excellent technical skill. Wields a bow and arrow.'

    print(str(num) + '. ' + clss + info)
class_num = input('Select a class using the corresponding numbers: ')
while True:
    while True:
        try:
            int(class_num)
            break
        except:
            class_num = input('Select a class using the corresponding numbers: ')
    class_num = int(class_num)
    if class_num > 5 or class_num < 1:
        class_num = input('Select a class using the corresponding number: ')
        continue
    else:
        break
my_class = classes.get(class_num)
print('Your class is ' + my_class + '.\n')

# Weapon
weapons = {
    1:'Sword and shield',
    2:'Fire and ice tome',
    3:'Dual knives',
    4:'Staff',
    5:'Bow and arrow'
}
my_weapon = weapons.get(class_num)

# Choose your character's strength and weakness
attributes = {
    1:'Strength',
    2:'Dexterity',
    3:'Intelligence',
    4:'Charisma',
    5:'Luck'
}
my_attributes = []
print('Character Attributes: ')
for num, att in attributes.items():
    info = ''
    if num == 1:
        info = ' - Combat ability and health.'
    if num == 2:
        info = ' - Reflexes, agility and technique.'
    if num == 3:
        info = ' - Magical ability and perception.'
    if num == 4:
        info = ' - Persuasion and bargaining.'
    if num == 5:
        info = ' - Affects certain events. May come in handy.'
    print(str(num) + '. ' + att + info)

strong_num = input('Select an attribute to be your strength using the corresponding number: ')
while True:
    while True:
        try:
            int(strong_num)
            break
        except:
            strong_num = input('Select an attribute to be your strength using the corresponding number: ')
    strong_num = int(strong_num)
    if strong_num > 5 or strong_num < 1:
        strong_num = input('Select an attribute to be your strength using the corresponding number: ')
        continue
    else:
        break
att_str = attributes.get(strong_num)
my_attributes.append(strong_num)
print('Your strength is ' + att_str + '.\n')

weak_num = input('Select an attribute to be your weakness using the corresponding number: ')
while True:
    while True:
        try:
            int(weak_num)
            break
        except:
            weak_num = input('Select an attribute to be your weakness using the corresponding number: ')
    weak_num = int(weak_num)
    if weak_num in my_attributes:
        weak_num = input('Your selected attribute has already been chosen as your strength.\nSelect an attribute to be your weakness using the corresponding number: ')
        continue
    if weak_num > 5 or weak_num < 1:
        weak_num = input('Select an attribute to be your weakness using the corresponding number: ')
        continue
    else:
        break
att_weak = attributes.get(weak_num)
my_attributes.append(weak_num)
print('Your weakness is ' + att_weak + '.\n')

# Stats
strength = 2
dex = 2
intel = 2
charisma = 2
luck = 2
if class_num == 1:
    hp = 50
    strength += 5
    dex += 1
    intel -= 2
if class_num == 2:
    hp = 25
    strength += 1
    dex += 4
    intel += 8
if class_num == 3:
    hp = 35
    strength -= 1
    dex += 4
    intel += 2
    charisma += 3
    luck += 4
if class_num == 4:
    hp = 40
    strength += 2
    dex -= 1
    intel += 5
    charisma += 1
if class_num == 5:
    hp = 30
    strength += 3
    dex += 5
    charisma -= 1

if strong_num == 1:
    strength += 2
if weak_num == 1:
    strength -= 2
if strong_num == 2:
    dex += 2
if weak_num == 2:
    dex -= 2
if strong_num == 3:
    intel += 2
if weak_num == 3:
    intel -= 2
if strong_num == 4:
    charisma += 2
if weak_num == 4:
    charisma -= 2
if strong_num == 5:
    luck += 2
if weak_num == 5:
    luck -=2

print(f"""{name}'s stats:
HP: {hp}
Strength: {strength}
Dexterity: {dex}
Intelligence: {intel}
Charisma: {charisma}
Luck: {luck}
""")
