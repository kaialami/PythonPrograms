def shiftEncode(message, shift, groupSize):
    import math

    if len(message) < 1 or groupSize < 1:
        return None

    message2 = message.upper()
    message2 = message2.replace(" ", "")
    coded = ''
    ordA = ord("A")
    ordZ = ord("Z")

    for i in message2:
        ordi = ord(i) + shift
        if ordi > ordZ: # Loop forward from Z to A
            ordi -= ordZ
            ordi += ordA - 1
        elif ordi < ordA: # Loop backward from A to Z
            ordi -= ordA
            ordi += ordZ + 1
        coded += chr(ordi)
    
    size = len(coded)
    offset = 0
    codedGroup = ""
    while offset < size:
        codedGroup += coded[offset:offset + groupSize] + ' '
        offset += groupSize
    codedGroup = codedGroup.rstrip() # Remove excess space on right
    groupLength = len(codedGroup)

    if size % groupSize != 0:
        numOfGroups = math.floor(size/groupSize) + 1 # Total num of groups
        maxSize = numOfGroups * groupSize # Max size of encoded group
        fillX = maxSize - size # Subtracting encoded group size from final size gives num of "~" needed
        codedGroup = codedGroup.ljust(groupLength + fillX, "~")
        # print(f"og size = {size} \ngrouped size = {groupLength} \nMax Size = {maxSize} \nFill X = {fillX} \n{coded}") # Check variables
    return codedGroup

def shiftDecode(message, shift):
    dictionary = ["A", "I", "YOU", "ME", "HAVE", "THE", 'HIM', 'HER', 'HIS', 'SHE', 'THEM', 'THEY', 'HOUSE', 'KEY', 'KEYS', 'TO']

    message2 = message
    message2 = message2.replace(" ", "")
    message2 = message2.replace("~", "")
    ordA = ord("A")
    ordZ = ord("Z")
    decoded = ''

    for i in message2:
        ordi = ord(i) - shift
        if ordi > ordZ:
            ordi -= ordZ
            ordi += ordA - 1
        elif ordi < ordA:
            ordi -= ordA
            ordi += ordZ + 1
        decoded += chr(ordi)

    final = ''
    index = 0
    size = len(decoded)
    word = ''
    while index < size:
        word += decoded[index]
        if word in dictionary:
            final += word + ' '
            index += 1
            lastWord = word
            word = ''
        else:
            index += 1
    return final.capitalize()


msg = 'I have the key to the house'
coded = shiftEncode(msg, 3, 5)
print(shiftDecode(coded, 3))
