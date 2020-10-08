import printboard, sys

board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

pboard = '\n' + printboard.printBoard(board)
print(pboard)
print('The board is numbered 1-9 like a numpad. \nPlayers will take turns inputing which numbers they wish to play. ')


error = 'Your move must be an integer between 1-9. \n'
move1 = "P1's move: "
move2 = "P2's move: "
taken = 'These positions are already taken: '
remind = 'Unavailable moves: '

x = 'X'
o = 'O'

total = []

# move 1
p1 = input(move1)

while True:
	while True:
		try:
			int(p1)
			break
		except:
			p1 = input(error + move1)

	p1 = int(p1)
	if not p1 in board:
		p1 = input(error + move1)
		continue

	if not board.get(p1) == ' ':
		p1 = input(taken + str(total) + '\n' + move1)
		continue

	else:
		break

board[p1] = x
total.append(p1)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n' + remind + str(total))

# move 2
p2 = input(move2)

while True:
	while True:
		try:
			int(p2)
			break
		except:
			p2 = input(error + move2)

	p2 = int(p2)
	if not p2 in board:
		p2 = input(error + move2)
		continue

	if not board.get(p2) == ' ':
		p2 = input(taken + str(total) + '\n' + move2)
		continue

	else:
		break

board[p2] = o
total.append(p2)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n' + remind + str(total))

# move 3
p1 = input(move1)

while True:
	while True:
		try:
			int(p1)
			break
		except:
			p1 = input(error + move1)

	p1 = int(p1)
	if not p1 in board:
		p1 = input(error + move1)
		continue

	if not board.get(p1) == ' ':
		p1 = input(taken + str(total) + '\n' + move1)
		continue

	else:
		break

board[p1] = x
total.append(p1)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n' + remind + str(total))

# move 4
p2 = input(move2)

while True:
	while True:
		try:
			int(p2)
			break
		except:
			p2 = input(error + move2)

	p2 = int(p2)
	if not p2 in board:
		p2 = input(error + move2)
		continue

	if not board.get(p2) == ' ':
		p2 = input(taken + str(total) + '\n' + move2)
		continue

	else:
		break

board[p2] = o
total.append(p2)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n' + remind + str(total))

# move 5
p1 = input(move1)

while True:
	while True:
		try:
			int(p1)
			break
		except:
			p1 = input(error + move1)

	p1 = int(p1)
	if not p1 in board:
		p1 = input(error + move1)
		continue

	if not board.get(p1) == ' ':
		p1 = input(taken + str(total) + '\n' + move1)
		continue

	else:
		break

board[p1] = x
total.append(p1)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n')

if printboard.winCheck('X', board):
	print('P1 wins.')
	sys.exit(0)

print(remind + str(total))

# move 6
p2 = input(move2)

while True:
	while True:
		try:
			int(p2)
			break
		except:
			p2 = input(error + move2)

	p2 = int(p2)
	if not p2 in board:
		p2 = input(error + move2)
		continue

	if not board.get(p2) == ' ':
		p2 = input(taken + str(total) + '\n' + move2)
		continue

	else:
		break

board[p2] = o
total.append(p2)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n')

if printboard.winCheck('O', board):
	print('P2 wins.')
	sys.exit(0)

print(remind + str(total))

# move 7
p1 = input(move1)

while True:
	while True:
		try:
			int(p1)
			break
		except:
			p1 = input(error + move1)

	p1 = int(p1)
	if not p1 in board:
		p1 = input(error + move1)
		continue

	if not board.get(p1) == ' ':
		p1 = input(taken + str(total) + '\n' + move1)
		continue

	else:
		break

board[p1] = x
total.append(p1)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n')

if printboard.winCheck('X', board):
	print('P1 wins.')
	sys.exit(0)

print(remind + str(total))

# move 8
p2 = input(move2)

while True:
	while True:
		try:
			int(p2)
			break
		except:
			p2 = input(error + move2)

	p2 = int(p2)
	if not p2 in board:
		p2 = input(error + move2)
		continue

	if not board.get(p2) == ' ':
		p2 = input(taken + str(total) + '\n' + move2)
		continue

	else:
		break

board[p2] = o
total.append(p2)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n')

if printboard.winCheck('O', board):
	print('P2 wins.')
	sys.exit(0)

print(remind + str(total))

# move 9
p1 = input(move1)

while True:
	while True:
		try:
			int(p1)
			break
		except:
			p1 = input(error + move1)

	p1 = int(p1)
	if not p1 in board:
		p1 = input(error + move1)
		continue

	if not board.get(p1) == ' ':
		p1 = input(taken + str(total) + '\n' + move1)
		continue

	else:
		break

board[p1] = x
total.append(p1)

pboard = '\n' + printboard.printBoard(board)
print(pboard + '\n')

if printboard.winCheck('X', board):
	print('P1 wins.')

else:
	print('P1 and P2 tied.')
	sys.exit(0)

