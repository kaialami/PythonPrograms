import random, sys, check

# variables
yes = 'y'
no = 'n'
error_num = "ERROR: Password length is not a number."
error_range = "ERROR: Length does not fall within the range 6-24."
error_yn = "ERROR: Input is not y or n."
characters = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]
pass_nums = []
pass_list = []

# Pass length
length = input("Password Length (6-24): ")
if not check.int_check(length):
    print(error_num)
    sys.exit(0)
length = int(length)

# Pass in range
if not check.range_check(length, 6, 24):
    print(error_range)
    sys.exit(0)

# Exclusion of certain characters
exclude = str(input("Exclude ()[]{};:,./\\~<>\"'|+-=` [y/n]: ")).lower()
if not exclude == yes and not exclude == no:
    print(error_yn)
    sys.exit(0)
elif exclude == yes:
    excluded_list = [40, 41, 91, 93, 123, 125, 59, 58, 44, 46, 47, 92, 126, 60, 62, 34, 39, 124, 43, 45, 61, 96]
else:
    excluded_list = []

# Exclusion of similar characters
similar = str(input("Exclude similar characters (1, i, I, l, L, o, O, 0) [y/n]: ")).lower()
if not similar == yes and not similar == no:
    print(error_yn)
    sys.exit(0)
elif similar == yes:
    excluded_list = excluded_list + [49, 105, 73, 108, 76, 111, 79, 48]

# Generate ascii nums
for x in range(length):
    symbol = random.choice(characters)
    while symbol in excluded_list:  # continue selecting nums until it is not in the excluded list
        symbol = random.choice(characters)
    pass_nums.append(symbol)

# Convert ascii nums into characters
for y in pass_nums:
    pass_list.append(chr(y))

# Create password
password = ''.join(pass_list)
print(f"Generated Password: {password}")

