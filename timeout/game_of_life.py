class Game:
	def __init__(self, size=10):
		self.size = size
		self.grid = [[0]*size for _ in range(size)]


		