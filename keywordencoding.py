def keywordEncode(message, keyword, groupSize):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    head = alphabet[0:len(keyword)]
    tail = alphabet[len(keyword):]
    headMapping = list(map(lambda x, y: (x, y), keyword, head))
    unused = alphabet
    unused = unused[::-1]

    for x in keyword:
        unused = unused.replace(x, '')
    tailMapping = list(map(lambda x, y: (x, y), unused, tail))
    finalMapping = headMapping + tailMapping
    finalMapping.append((" ", " "))

    message2 = message.upper()
    message2 = message2.replace(" ", "")

    offset = 0
    grouped = ""
    size = len(message2)
    while offset < size:
        grouped += message2[offset:offset + groupSize] + ' '
        offset += groupSize

    groupedLength = len(grouped)
    letterIndexes = {}
    for mapped, original in finalMapping:
        if original in grouped:
            for letterIndex in range(groupedLength):
                letter = grouped[letterIndex]
                if letter == original:
                    letterIndexes[letterIndex] = mapped

    result = ""
    for key in range(groupedLength):
        result += letterIndexes[key]
    print(finalMapping)
    print(grouped)
    return (result, keyword)


print(keywordEncode("Hello there buddysss", "PON", 5))