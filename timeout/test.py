import unittest
from game_of_life import Game


PATTERN = [[1, 0], [1, 1], [1, 2]]
NEIGHS = [[3, 3, 3], [2, 2, 2], [3, 3, 3]]

class TestGame(unittest.TestCase):

	def test_size(self):
		g = Game(10)
		self.assertEqual(g.size, 10)
		self.assertEqual(len(g.grid), 10)
		self.assertEqual(len(g.grid[0]), 10)


		g = Game(20)
		self.assertEqual(g.size, 20)
		self.assertEqual(len(g.grid), 20)
		self.assertEqual(len(g.grid[0]), 20)

	def test_set_active(self):
		g = Game(10)
		g.set_active(PATTERN)

		for i in range(10):
			for j in range(10):
				if [i, j] in PATTERN:
					self.assertEqual(g.isActive(i, j), 1)

	def test_grid(self):
		g = Game(10)
		g.set_active(PATTERN)

		for i in range(10):
			for j in range(10):
				if [i, j] in PATTERN:
					self.assertEqual(g.isActive(i, j), 1)
				else:
					self.assertEqual(g.isActive(i, j), 0)

	def test_count_neigh(self):
		g = Game(3)
		g.set_active(PATTERN)
		for i in range(3):
			for j in range(3):
				self.assertEqual(g.count_neigh(i, j), NEIGHS[i][j])




if __name__ == '__main__':
	unittest.main()