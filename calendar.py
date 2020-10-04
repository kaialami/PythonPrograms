print('M    T    W    T    F    S    S ')
print('---------------------------------')
offset = 3

for row in range(6):
    for col in range(7):
        if col < offset:
            print(row * 7 + (col + 1 + offset), '  ', end = '')
    print('')
    




# Calendar with month and year.