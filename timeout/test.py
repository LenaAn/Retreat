import unittest
from game_of_life import Game

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
    	




if __name__ == '__main__':
    unittest.main()