class Game:
	def __init__(self, size=10):
		self.size = size
		self.grid = [[0]*size for _ in range(size)]

	def set_active(self, pattern):
		for i, j in pattern:
			self.grid[i][j] = 1

	def isActive(self, i, j):
		return self.grid[i][j] == 1


		