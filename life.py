import time
from bcolors import bcolors

BLINKER_CORNER = [[0, 0], [0, 1], [0, -1]] 
BLINKER = [[3, 3], [3, 4], [3, 5]]
TOAD = [[3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4]]
BEACON = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6], [6, 5], [6, 6]]
GLIDER = [[0, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


class Game(object):
	"""docstring for ClassName"""
	def __init__(self, n=10, is_donut=False):
		super(Game, self).__init__()
		self.is_donut = is_donut
		self.n = n
		self.grid = [ [0 for _ in range(n)] for _ in range(n)]


	def print(self):
		for line in self.grid:
			for item in line:
				if item == 1:
					print(bcolors.OKBLUE + str(item) + bcolors.ENDC, end = ' ')
				else:
					print(item, end = ' ')
			print()

	def start_state(self, list_of_points):
		for i, j in list_of_points:
			self.grid[i][j] = 1

	def is_valid(self, i, j):
		if self.is_donut:
			return True
		else:
			return i >= 0 and i < self.n and j >= 0 and j < self.n

	def count_neigh(self, x, y):
		count = 0
		for i in range(x-1, x+2):
			for j in range(y-1, y + 2):
				if i == x and j == y:
					pass
				else:
					if self.is_donut:
						i, j = (i+self.n) % self.n, (j+self.n) % self.n
						if self.grid[i][j] == 1:
							count += 1
					else:
						if self.is_valid(i, j):
							if self.grid[i][j] == 1:
								count += 1
		return count

	def step(self):
		new_grid = [ [item for item in line ] for line in self.grid ]
		for i in range(self.n):
			for j in range(self.n):
				if self.grid[i][j] == 1:
					if self.count_neigh(i, j) in [2, 3]:
						pass
					else:
						new_grid[i][j] = 0
				else:
					if self.count_neigh(i, j) == 3:
						new_grid[i][j] = 1
		self.grid = new_grid

	def live(self):
		while True:
			self.print()
			print()
			self.step()
			time.sleep(1)


if __name__ == '__main__':
	g = Game(is_donut=True)
	g.start_state( GLIDER )
	# g.start_state( BLINKER_CORNER )
	g.live()
