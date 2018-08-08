import unittest
from game_of_life import Game_Of_Life

class TestGameOfLife(unittest.TestCase):
    def test_init_size(self):
        g = Game_Of_Life(n = 10)
        self.assertEqual(len(g.board), 10)
        self.assertEqual(len(g.board[0]), 10)

    def test_assignment(self):
        g = Game_Of_Life(n =5)
        g.setAlive(1,1)
        self.assertEqual(g.isAlive(1,1), True)

    def test_calculate_neighbours_count(self):
        g = Game_Of_Life(n =5)
        g.setAlive(1,1)
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if i == 1 and j == 1:
                    pass
                else:
                    self.assertEqual(g.get_neighbours_count(i, j), 1)

        self.assertEqual(g.get_neighbours_count(1, 1), 0)
        self.assertEqual(g.get_neighbours_count(2, 3), 0)

    def test_change_state(self):
        g = Game_Of_Life(n =5)
        g.setAlive(1,1)
        g.setAlive(2,2)
        g.setAlive(0,2)
        g.setAlive(2,0)
        g.nextState()

        self.assertEqual(g.isAlive(1, 1), True)
        self.assertEqual(g.isAlive(0,0), False)        

if __name__ == '__main__':
    unittest.main()