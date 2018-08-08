import unittest
from game_of_life import Game

class TestGame(unittest.TestCase):

    def test_size(self):
    	g = Game(n=10)
    	self.assertEqual(g.size, 10)

    	g = Game(n=20)
    	self.assertEqual(g.size, 20)



if __name__ == '__main__':
    unittest.main()