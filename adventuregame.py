import random, sys
name = str(input('Character Name: ')).capitalize()
print('')
# test
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
my_class = classes.get(class_num).lower()
print('Your class is ' + my_class + '.\n')

# Weapon
weapons = {
    1:'sword and shield',
    2:'fire and ice tome',
    3:'dual knives',
    4:'staff',
    5:'bow and arrow'
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

# Assigning common variables
error_yn = 'Enter yes or no. '
error_num = 'Enter one of the listed numbers. '
yes = 'yes'
y = 'y'
no = 'no'
n = 'n'

# Stats
strength = 2
dex = 2
intel = 2
charisma = 2
luck = 2
money = 5
if class_num == 1:
    strength += 5
    dex += 1
    intel -= 2
if class_num == 2:
    strength += 1
    dex += 4
    intel += 7
if class_num == 3:
    strength -= 1
    dex += 4
    intel += 2
    charisma += 3
    luck += 4
if class_num == 4:
    strength += 2
    dex -= 1
    intel += 3
    charisma += 1
if class_num == 5:
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

if strength < 1:
    strength = 0
if dex < 1:
    dex = 0
if intel < 1:
    intel = 0
if charisma < 1:
    charisma = 0
if luck < 1:
    luck = 0

print(f"""{name}'s stats:
Strength: {strength}
Dexterity: {dex}
Intelligence: {intel}
Charisma: {charisma}
Luck: {luck}
""")

# M or F
gender = str(input('Are you male or female [M or F]: ')).lower()
while True:
    if gender == 'male' or gender == 'm' :
        gender = 0
        break
    if gender == 'female' or gender == 'f':
        gender = 1
        break
    else:
        gender = str(input('Are you male or female [M or F]: ')).lower()
if gender == 0:
    they = 'he'
    theyC = 'He'
    their = 'his'
    them = 'him'
    hey = 'sir'
    friend = 'boy'
else:
    they = 'she'
    theyC = 'She'
    their = 'her'
    them = 'her'
    hey = "ma'am"
    friend = 'girl'

# "Randomly" generated names
town_names = {1:'Northwich', 2:'Tamworth', 3:'Greenflower', 4:'Bamburgh', 5:'Holmfirth'}
town = town_names.get(random.randint(1,5))
horse_names = {1:'Jerry', 2:'Barry', 3:'Billy Bob Jones'}
horse = horse_names.get(random.randint(1,3))
bartender_names = {1:'Fatso', 2:'Randolph', 3:'Higgy'}
bar = bartender_names.get(random.randint(1,3))

# Adventure Begins!
print(f"It's time to begin your adventure! Good luck, {my_class} {name}.\n")
print(f"""In the quaint town of {town}, a young {my_class} by the name of {name} is making {their} way down to the local pub.
It's a bright, sunny day, perfect for lazying around and having a drink with the locals.
Along the way, {name} comes across a frantic-looking man. He appears to be chasing after a horse before stopping to catch his breath, his hands on his knees.
""")

# First choice: Runaway horse.
help_man = str(input('Will you help the man out?: ')).lower()
while True:
    if help_man == yes or help_man == y:
        help_man = True
        break
    if help_man == no or help_man == n:
        help_man = False
        break
    else:
        help_man = str(input(error_yn + 'Will you help the man?: ')).lower()

if help_man:
    print(f'''{name} decided to help the man. 
The man sees you approaching. "Oh, {hey}, do ya think you can help me? My horse {horse} got spooked and ran off. 
I hafta to deliver these packages of milk before they go bad, but without ol' {horse} that ain't possible."
You can see {horse} running off down the road, but he doesn't seem to be going too fast for a horse.
    ''')
    run = str(input(f'Will you try running after {horse}? (DEX check): ')).lower()
    while True:
        if run == yes or run == y:
            run = True
            break
        if run == no or run == n:
            run = False
            break
        else:
            run = str(input(error_yn + f'Will you try running after {horse}? (DEX check): ')).lower()
    if run:
        print(f'{name} decided to try and run after the horse. \n')
        run_horse = []
        for x in range(dex):
            run_horse.append(random.randint(1, 3))
        print(f'Tossing aside {their} {my_weapon}, {name} dashed after {horse}.')
        if 3 in run_horse:
            print(f'''Luckily, {name} was faster than ol' {horse}.
{they.capitalize()} quickly caught up to the horse and hopped onto his back. 
{horse} reared back as {name} begins to calm him down. 
Eventually, {horse} calms down, and {name} starts heading back to the man.

"{horse}, my boy! Don't you dare try running off again. 
Thank you so much, pal. I owe you. {horse} is an old boy, but he's my boy."
The man happily took out some coins and shoved a few into {name}'s hands. 
He also gave {name} a fresh bottle of milk. "{horse}'s milk", it says on the label.
{name} decides it probably isn't a good idea to take a sip.

In any case, with a few extra coins to {their} name, {name} continues along towards the pub.
            ''')
            money += 5
        else:
            print(f'''Unfortunately, {name} was not having a good day.
Despite {their} best efforts, {they} was not able to catch up to {horse}.
After stopping to catch {their} breath, {name} started heading back to the man, who looked disappointed.

"Well, you tried your best, I guess. It looks like ol' {horse} still has some life left in him, eh? Thanks anyways..."
The man waved goodbye and ran off towards the direction of {horse}.
{name} continues along towards the pub.
            ''')
    else:
        print(f'''{name} decided it wasn\'t worth it to try and catch up with a horse
{they.capitalize()} continues down the path towards the pub, leaving the dejected-looking man behind.''')

else:
    print(f'{name} decided not to stop and help the man. {they.capitalize()} continues down the path towards the pub.')

enter = str(input('Press enter to continue: '))

# Enters the pub
print(f'''\n{name} finally makes it to the pub. {they.capitalize()} looks up at the dull, rickety sign above the door.
"{bar}'s Lounge"
{they.capitalize()} swings open the door and a light jingle chimes out.
The pub is just as it always was. Music blasting out the jukebox, men and women gathering and drinking, a thick cloud of smoke lingering through the air.
Across the dimly lit bar, {bar} looks over, a fat grin on his face.

"{name}, my friend, how are you, how are you? Come, sit, have a drink, let's chat, eh?"
{name} grabs a stool at the bar while {bar} hands {them} a cold beer.
"So, how's life, eh? Ya better not be causing no harm with that thing there, eh?"
He gestures to the {my_weapon} that {name} places on the bar.

"You know, that reminds me. A fella with a big ol' hat came in a while ago, said he was lookin' for some help."
{bar} takes out a dusty flier and slides it across the bar. 

"Help wanted: mysterious creatures spotted in the woods near {town}.
Looking for skilled fighters to investigate and report any suspiscious activity.
Sign up at the guard station."

It doesn't seem too interesting to {name}.
"Oh right, the man said somethin' about a reward. Was some good money, I think. I'd do it if I could, ya know?"
''')

# Second choice
job = str(input('Will you take the offer?: ')).lower()
while True:
    if job == yes or job == y:
        job = True
        break
    if job == no or job == n:
        job = False
        break
    else:
        job = str(input(error_yn + 'Will you take the offer?: ')).lower()

# Takes the job
if job:
    print(f'''{name} decided to take the job.
"Good choice, bud." {name} quickly downs the last of {their} beer and tosses two coins onto the counter.
"No, no, this one's on me. Pay up when you rake in the cash from the job, eh?"
{bar} returns the coins to {name}, who picks up {their} {my_weapon} and leaves for the guard station.

Outside the station on the bulletin board, {name} sees the flier clutched in {their} hand.
{theyC} enters the station. A man with a very curly moustache and a tall hat approaches.

"Ah, yes, are you here for that?" He points to the flier in {name}'s hands.
"Well, you look like you might be up for it. Come along, I'll write your name down and show you the location."

He pulls out a piece of paper from his desk and begins to write.
"What was your name, {friend}?" 
{name} gives him {their} name. The man scribbles quickly and shoves it back into his desk.
"Follow me, then." He grabs a scabbard hanging by the door and exits the station. {name} follows suit.
''')
    enter = input('Press enter to continue: ')

    print(f'''The two of them approach the dense forest surrounding the town.
"Here is where you will be located. The reports say that they heard some odd noises coming from these forests.
It's up to you to see if it's worth worrying about."
He swiftly turns in place and heads back.

There are two options: 1. enter the woods. 2. head home (pussy check)
''')
    woods = input('What will you do? Enter the corresponding number: ')
    while True:
        while True:
            try:
                int(woods)
                break
            except:
                woods = input(error_num + 'What will you do? Enter the corresponding number: ')
        woods = int(woods)
        if woods > 2 or woods < 1:
                woods = input(error_num + 'What will you do? Enter the corresponding number: ')
                continue
        else:
            break
    if woods == 1:
        print(f'''{name} decides to enter the forest and complete the mission.''')
    if woods == 2:
        print(f'''{name} decides to be a little pussy and ditches the job.
{theyC} scurries on back to {their} little home, makes some tea, crawls into bed with a nice book and enjoys the rest of the evening.
Actually, it doesn't sound so bad after all. 
As the sun goes to sleep and night envelopes the town, {name} blows out the candle and snuggles up in {their} blanket.
{name} had a very good night's sleep.

The End.
''')
        sys.exit(0)

 

# Stays at the bar, man beats up other dude.
else:
    print(f'''{name} decided it wasn't worth the time and effort
"Hey, I get it, it don't seem that interesting. You can stay 'ere an' chat with me."

{name} and {bar} chat and drink, catching up with each other for the first time in a while.
{name} finishes {their} drink and gets another.
Time flies by, and the sun starts to set. As night falls, {name} hears a loud noise outside.
It sounds like someone hitting something.
''')
    noise = str(input('Will you investigate the strange noise?: ')).lower()
    while True:
        if noise == yes or noise == y:
            noise = True
            break
        if noise == no or noise == n:
            noise = False
            break
        else:
            noise = str(input(error_yn + 'Will you investigate the strange noise?: ')).lower()
    if noise:
        print(f'''{name} decides to investigate the noise.
{theyC} opens the door to the bar and sees a large, bald man with a scruffy beard. He's beating up a frail, skinny man.

"I'm sorry, please, I didn't mean to! I swear on my momma! Please stop!" the frail man cries.
This is not a fair fight.
It looks like you can attempt a few things: 1. intervene (STR or INT check), 2. persuade, or 3. pickpocket (DEX & CHAR check).
''')
        beard_man = input('What will you do? Enter the corresponding number: ')
        while True:
            while True:
                try:
                    int(beard_man)
                    break
                except:
                    beard_man = input(error_num + 'What will you do? Enter the corresponding number: ')
            beard_man = int(beard_man)
            if beard_man > 3 or beard_man < 1:
                beard_man = input(error_num + 'What will you do? Enter the corresponding number: ')
                continue
            else:
                break
        
        if beard_man == 1:
            print(f'''{name} decides to intervene.
{theyC} walks up to the scruffy and gets his attention.
"Whaddaya want, shrimpy?" {name} lays in the big man's shadow.
"Get outta mah sight, or I'll kick yer ass, {friend}."
''')
            if class_num == 1:
                fight = f'impales him through the chest'
                attack = 'sword strike hits him on his arm guard'
            if class_num == 2:
                fight = f'blasts him with an inferno and burns him to a crisp'
                attack = 'magic spell wasn\'t strong enough'
            if class_num == 3:
                fight = f'slices his forearms. He falls to the ground and writhes in pain as he quickly bleeds out'
                attack = 'slices'
            if class_num == 4:
                fight = f'summons spears of light that impale him'
                attack = 'magic spell missed by a hair'
            if class_num == 5:
                fight = f'draws and shoots an arrow in each of his eyes'
                attack = 'arrow shot missed'
            
            print(f'{name} readies {their} {my_weapon}.')
            intense = str(input('Do you want to go all out? (STR or INT check): '))
            while True:
                if intense == yes or intense == y:
                    intense = True
                    break
                if intense == no or intense == n:
                    intense = False
                    break
                else:
                    intense = str(input(error_yn + 'Do you want to go all out? (STR or INT check): '))
            if intense:
                baldy = []
                lucky = []
                if strength >= intel:
                    for x in range(strength):
                        baldy.append(random.randint(1,7))
                else:
                    for x in range(intel):
                        baldy.append(random.randint(1,7))
                
                for x in range(luck):
                    lucky.append(random.randint(1,15))
                if 5 in lucky:
                    lucky = True
                else:
                    lucky = False
                if 5 in baldy or 4 in baldy:
                    print(f'''{name} decided to go all out against scruffy. 
Scruffy begins to charge at {name}, his fists raised, poised to beat {name} down.
''')
                    if lucky:
                        print(f'''All of a sudden, due to sheer dumb luck, scruffy trips over the man he had just beaten.
He falls right on his head and stops moving completely. 
The crowd that had started to gather during all the commotion fell silent.
A pool of blood began to form around scruffy's head.
A woman from the crowd steps forward and kneels next to him.

"He's dead..."

That was easy enough.
{name} heads back inside to reunite with {bar}.

"Hey, pal, you're back. What was that about, outside I mean."

{name} gave a shrug, sat down at the bar and gulped down {their} drink.

The End.
''')
                        sys.exit(0)
                    else:
                        print(f'''Before he is able to bring his fist down, {name} {fight}.
There was no surviving that.
Although {name} won this fight, a crowd had gathered around the two of them.
Silence filled the street.
Among the crowd was a patrol officer.

"You there, you're under arrest for murder!" He points his lanky, bony finger at {name}.
{name} makes a dash for it. {theyC} runs off into an alleyway, but unfortunately comes to a dead-end.
With {their} hands in the air, {name} gets arrested and thrown into the back of a polic carriage.
As {they}'s getting carried away, the frail man runs up to the carriage.

"Thank you, {hey}, thank you, with all my heart. Thank you."

The carriage sets off to the lock-up as the frail man falls to his knees.

The End.
''')                    
                        sys.exit(0)

                else:
                    print(f'''{name} readies {their} {my_weapon}. Scruffy charges at {them} with his fists above him, ready to strike.
Unfortunately for {name}, {their} {attack}. Scruffy seizes the opportunity and lands a nasty strike to {name}'s forehead.
{name} lies on the ground, barely any strength left.

"What a wimp." Scruffy turns back to his original victim.
Unfortunately for him, {name} provided the perfect distraction for him to run off.
Scruffy, with fury in his eyes, kicks the wall of {bar}'s Lounge before angrily stomping off. 
''')
                    if class_num == 4:
                        print(f'''Luckily for {name}, clerics are masters of healing.
Using the last bit of {their} strength, {name} casts healing on {them}self.
Revitalization rushes over every cell in {their} body.
{theyC} stands up, feeling healthy as normal.
{name} heads back inside and reunites with {bar}.

"Eh, what took you so long, pal, eh?" {bar} looks a little peeved.

{name} sits down, brushes him off and orders another drink.

The End.
''')
                        sys.exit(0)
                    else:
                        print(f'''{name} took a hard hit to the head.
Unable to move, {they} lies on the ground. {theyC} feels a slight warmth surrounding {their} head.
Everything begins to fade, until soon, {name} sees only darkness.

The End.
''')
                        sys.exit(0)
            
            else:
                print(f'''{name} decided it wasn't worth it to go all out.
Scruffy raises his arms and charges at {name}.
To scruffy's surprise, {name} tosses aside {their} weapon and charges back at him.
As the large man ran towards the small {my_class}, a smirk formed on his face.
''')
                nuts = []
                for x in range(intel):
                    nuts.append(random.randint(1,5))
                if 5 in nuts:
                    print(f'''Just as the two of them were only feet apart, {name} had a flash of inspiration.
Before their fists connected, {name} gave a nice, strong kick to scruffy's groin.
Instantly, all of scruffy's fighting spirit left his body as he rolled across the ground in sheer pain.

{name} helped up the frail man, who gave {them} his thanks before running off.
{name} headed on back to the pub, where he explained what just happened outside to {bar}.
The two laughed well and {bar} handed {name} another drink.

The End.
''')
                    sys.exit(0)
                else:
                    print(f'''Although {name} was first to deliver a blow, it barely made a dent in the thick skull of scruffy.
Scruffy retaliated with a strike of his own. Fortunately, {name} was able to block it in time with {their} free arm, but it still caused quite a bit of damage.
Blow after blow, scruffy kept the pressure on, and {name} was growing weaker.
All of a sudden, {bar} decides to come out and check out the situation.

"Hey, what do ya think you're doing, bucko?"
He grabs scruffy by the shoulders, pulls him off {name} and throws him to the mud.

"Get on outta here or I'll beat the devil outta ya!"
He gave scruffy a good kick to the side.
Scruffy scrambled to his feet and scurried away.

"Hooligans, eh? They just ain't right in the head." {bar} helps {name} to {their} feet.
"Come on back inside, I'll fix you a drink."

The exhausted {my_class} slumped down into a stool, picked up the cold pint, and took a nice, long chug.

The End.
''')
                    sys.exit(0)
        
        if beard_man == 3:
            print(f'''{name} decided to attempt to rob scruffy.
            
''')

        if beard_man == 2:
            print(f'''{name}, thinking of what the smartest thing would be to do, decided to head on back inside.
"What was it, pal?"
{name} told him it was none of their businesses to worry about.
{bar} seemed content with that answer.
The two of them continued their chat.
''')
