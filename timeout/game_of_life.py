from itertools import product

class Game:
	def __init__(self, size=10):
		self.size = size
		self.grid = [[0]*size for _ in range(size)]

	def set_active(self, pattern):
		for i, j in pattern:
			self.grid[i][j] = 1

	def isActive(self, i, j):
		return self.grid[i][j] == 1


	def count_neigh(self, i, j):
		count = 0
		for di, dj in product([-1, 0, 1], [-1, 0, 1]):
			if di == 0 and dj == 0:
				pass
			else:
				count += self.grid[(i+di+self.size) % self.size][(j+dj+self.size) % self.size]
		return count

	def step(self):
		new_grid = []
		for i in range(self.size):
			new_grid.append([0]*self.size)
		 # = [ [0]*self.size for _ in range(self.size)]

		for i in range(self.size):
			for j in range(self.size):
				if (self.isActive(i, j) and (self.count_neigh(i, j) == 2)) or (self.count_neigh(i, j) == 3):
					new_grid[i][j] = 1
				else:
					new_grid[i][j] = 0

		for i in range(self.size):
			for j in range(self.size):
				self.grid[i][j] = new_grid[i][j]
		# self.grid = new_grid

	def __str__(self):
		lines = [' '.join([str(item) for item in self.grid[i]]) for i in range(self.size)]
		return '\n'.join(lines)

