import random
import math

def keynumberEncode(message, key, groupSize, encode=True):
    message2 = message.upper()
    keystring = str(key)
    size = len(message2)
    keysize = len(keystring)
    offset = 0
    increment = 0
    assignment = {}
    specials = ["#", "?", "$", "!", "&", "%"]

    while increment < size:
        if message2[increment] == " ":
            assignment[increment] = random.choice(specials)
        else:
            assignment[increment] = keystring[offset]
            offset += 1
            if offset > keysize - 1:
                offset = 0
        increment += 1

    if encode:
        shift = 1
    else:
        shift = -1

    ordA = ord("A")
    ordZ = ord("Z")
    encoded = ""
    for letterIndex in range(size):
        letter = message2[letterIndex]
        if letter != " ":
            letterOrd = ord(letter)
            newOrd = letterOrd + (int(assignment[letterIndex]) * shift)
            if newOrd > ordZ or newOrd < ordA:
                newOrd -= 26 * shift
        else:
            newOrd = ord(assignment[letterIndex])
        encoded += chr(newOrd)

    groupOffset = 0
    grouped = ""
    while groupOffset < size:
        grouped += encoded[groupOffset:groupOffset + groupSize] + " "
        groupOffset += groupSize
    grouped = grouped.rstrip()
    groupedLength = len(grouped)

    if size % groupSize != 0:
        numOfGroups = math.floor(size/groupSize) + 1
        maxSize = numOfGroups * groupSize # Max size of encoded group
        fillX = maxSize - size # Subtracting encoded group size from final size gives num of "~" needed
        grouped = grouped.ljust(groupedLength + fillX, random.choice(specials))
    return (grouped, key)

def keynumberDecode(message, key):
    message2 = message.upper()
    message2 = message2.replace(" ", "")

    keystring = str(key)
    size = len(message2)
    keysize = len(keystring)
    offset = 0
    increment = 0
    assignment = {}
    specials = ["#", "?", "$", "!", "&", "%"]

    while increment < size:
        if message2[increment] in specials:
            assignment[increment] = 0
        else:
            assignment[increment] = keystring[offset]
            offset += 1
            if offset > keysize - 1:
                offset = 0
        increment += 1
    
    ordA = ord("A")
    decoded = ""
    for letterIndex in range(size):
        letter = message2[letterIndex]
        if letter not in specials:
            letterOrd = ord(letter)
            newOrd = letterOrd - int(assignment[letterIndex])
            if newOrd < ordA:
                newOrd += 26
        else:
            newOrd = 32
        decoded += chr(newOrd)
    
    return decoded.capitalize()
    
   
print(ord("a"), ord("A"), ord("z"), ord("Z"))
print(chr(91))

msg = "This is a SAMPLE sentence for encoding"
key = 34265
encoded = keynumberEncode(msg, key, 5)
print(encoded[0])
decoded = keynumberDecode(encoded[0], key)
print(decoded)