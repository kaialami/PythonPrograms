
board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
test = {1:' ', 2:' ', 3:' ', 4:'O', 5:'O', 6:'O', 7:' ', 8:' ', 9:' '}
allO = {1:'O', 2:'O', 3:' ', 4:' ', 5:' ', 6:'O', 7:'O', 8:'O', 9:'O'}
def printBoard(board):
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print(' --+---+--')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(' --+---+--')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	return ' '

def winCheck(player = 'x or o', dic = {}):
	botrow = []
	midrow = []
	toprow = []
	leftcol = []
	midcol = []
	rightcol = []
	leftdiag = []
	rightdiag = []
	allsets = [botrow, midrow, toprow, leftcol, midcol, rightcol, leftdiag, rightdiag]

	for x, y in dic.items():
		if dic.get(x) == player:
			if x > 0 and x < 4:
				botrow.append(x)
			if x > 3 and x < 7:
				midrow.append(x)
			if x > 6:
				toprow.append(x)

			if x == 1 or x == 4 or x == 7:
				leftcol.append(x)
			if x == 2 or x == 5 or x == 8:
				midcol.append(x)
			if x == 3 or x == 6 or x == 9:
				rightcol.append(x)

			if x == 1 or x == 5 or x == 9:
				leftdiag.append(x)
			if x == 3 or x == 5 or x == 7:
				rightdiag.append(x)
	
	for n in allsets:
		if len(n) == 3:
			return True
	
	return False

def cpuWin(player = 'O', dic = {}):
	botrow = []
	midrow = []
	toprow = []
	leftcol = []
	midcol = []
	rightcol = []
	leftdiag = []
	rightdiag = []
	allsets = [botrow, midrow, toprow, leftcol, midcol, rightcol, leftdiag, rightdiag]
	br = {1, 2, 3}
	mr = {4, 5, 6}
	tr = {7, 8, 9}
	lc = {1, 4, 7}
	mc = {2, 5, 8}
	rc = {3, 6, 9}
	ld = {1, 5, 9}
	rd = {3, 5, 7}

	for x, y in dic.items():
		if dic.get(x) == player:
			if x > 0 and x < 4:
				botrow.append(x)
			if x > 3 and x < 7:
				midrow.append(x)
			if x > 6:
				toprow.append(x)

			if x == 1 or x == 4 or x == 7:
				leftcol.append(x)
			if x == 2 or x == 5 or x == 8:
				midcol.append(x)
			if x == 3 or x == 6 or x == 9:
				rightcol.append(x)

			if x == 1 or x == 5 or x == 9:
				leftdiag.append(x)
			if x == 3 or x == 5 or x == 7:
				rightdiag.append(x)
	
	# print(allsets)
	possible_moves = []
	for n in allsets:
		missing = set()
		if len(n) == 2:
			if n == botrow:
				missing = br - set(botrow)
				for x in missing:
					possible_moves.append(x)
			
			elif n == midrow:
				missing = mr - set(midrow)
				for x in missing:
					possible_moves.append(x)

			elif n == toprow:
				missing = tr - set(toprow)
				for x in missing:
					possible_moves.append(x)

			elif n == leftcol:
				missing = lc - set(leftcol)
				for x in missing:
					possible_moves.append(x)

			elif n == midcol:
				missing = mc - set(midcol)
				for x in missing:
					possible_moves.append(x)

			elif n == rightcol:
				missing = rc - set(rightcol)
				for x in missing:
					possible_moves.append(x)

			elif n == leftdiag:
				missing = ld - set(leftdiag)
				for x in missing:
					possible_moves.append(x)

			elif n == rightdiag:
				missing = rd - set(rightdiag)
				for x in missing:
					possible_moves.append(x)

	possible_moves = set(possible_moves)
	movelist = []
	for x in possible_moves:
		movelist.append(x)
	return movelist

# def cpuBlock(player = 'O', dic = {}):


			
	

# print(cpuWin('O', allO))