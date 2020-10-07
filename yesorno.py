def yesOrNo(inp):
    while True:
        if not inp == 'yes' or not inp == 'no':
            inp = yesOrNo(inp)
            continue

        else:
            break
    return inp
	

print(yesOrNo(''))
