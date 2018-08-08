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

	def step(self)

