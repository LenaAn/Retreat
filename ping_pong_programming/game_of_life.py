class Game_Of_Life(object):
	"""docstring for Game_Of_Life"""
	def __init__(self, n ):
		super(Game_Of_Life, self).__init__()

		self.width=n
		self.height =n
		self.board =[]
		for row in range(self.height):
			self.board.append(self.createEmptyRow(row))

	def createEmptyRow(self, row_indx):
		row=[]
		for col in range(self.width):
			row.append(Cell(row_indx, col, 0))
		return row
	def setAlive(self, row_indx, col_indx):
		self.board[row_indx][col_indx].isAlive = True
		for neighbour in self.get_neighbours(self.board[row_indx][col_indx]):
			neighbour.neighbours_count = neighbour.neighbours_count +1

	def get_neighbours(self, cell):
		neighbours = []
		for row_step in [-1,0,1]:
			neighbours.extend(self.get_same_row_neighbours(cell, row_step))
		return neighbours
	def get_neighbours_count(self, row_indx, col_indx):
		return self.board[row_indx][col_indx].neighbours_count

	def get_same_row_neighbours(self, cell, row_step):
		neighbours =[]
		for col_step in [-1,0,1]:
			if row_step ==0 and col_step ==0:
				continue
			neighbours.append(self.board[cell.row+row_step][cell.col+col_step])
		return neighbours


	def isAlive(self, row_indx, col_indx):
		return self.board[row_indx][col_indx].isAlive

	def nextState(self):
		new_board = [0]*
		for row_indx in range(self.height):
			for col_indx in range(self.width):
				nex
				# pass


class Cell():
	def __init__(self, row, col, count):
		self.row = row
		self.col = col
		self.neighbours_count = 0
		self.isAlive =False

		