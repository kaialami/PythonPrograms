
board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
test = {1:' ', 2:' ', 3:' ', 4:'O', 5:'O', 6:'O', 7:' ', 8:' ', 9:' '}
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
