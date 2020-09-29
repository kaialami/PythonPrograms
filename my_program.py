# bring in the kai magic functions
import kai
import statistics
import random

# declare some random number
a = 200
# declare a list
my_list = [3,1,152222,3,55,22]

# call the kai magic function to find of even numbers and assign to x


randlist = []
for i in range(0,20):
	n = random.randint(0,100)
	randlist.append(n)
print(randlist)

x = kai.findNumberOfEvens(10, randlist, True)
print('Number of evens: ' + str(x) + '\n')

