from random import *
import unittest
import minesweeper as m
class RandomTest(unittest.TestCase):

    def test_setupgrid(self):
        self.assertIsInstance(m.setupgrid(9, (4, 0), 10),tuple)

    def test_playagain(self):
        self.assertEqual(m.playagain('Y'),True)
        self.assertTrue(m.playagain('y'))
        self.assertFalse(m.playagain('N'))
        self.assertEqual(m.playagain('dsq'),False)

    def test_parseinput(self):
        res={'cell': (0, 0), 'flag': False, 'message': ''} 
        self.assertIsInstance(m.parseinput('a1', 9, "Type the column followed b...' to the cell (eg. a5f).\\n"),dict)
        self.assertEqual(m.parseinput('a1', 9, "Type the column followed b...' to the cell (eg. a5f).\\n")['flag'], False)
        self.assertEqual(m.parseinput('a1', 9, "Type the column followed b...' to the cell (eg. a5f).\\n")['message'], '')
        self.assertDictEqual(m.parseinput('a1', 9, "Type the column followed b...' to the cell (eg. a5f).\\n"),res)

    def test_getnumbers(self):
        emptygrid = [['0' for i in range(9)] for i in range(9)]
        self.assertIsInstance(m.getnumbers(emptygrid),list)

    def testdata(self):
        self.assertEqual(len(m.getnumbers([['0' for i in range(9)] for i in range(9)])),9)

    def test_getrandomcell(self):
        emptygrid = [['0' for i in range(9)] for i in range(9)]
        self.assertIsInstance(m.getrandomcell(emptygrid),tuple)
        self.assertEqual(len(m.getrandomcell(emptygrid)),2)

    def test_getneighbors(self):
        tu=[(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        emptygrid = [['0' for i in range(9)] for i in range(9)]
        self.assertEqual(m.getneighbors(emptygrid,4,4),tu)
        self.assertIsInstance(m.getneighbors(emptygrid,4,4),list)

    def test_mines(self):
        n = randint(1,10)
        emptygrid = [['0' for i in range(9)] for i in range(9)]
        self.assertEqual(len(m.getmines(emptygrid,(4, 0),n)),n)
        self.assertIsInstance(m.getmines(emptygrid,(4, 0),n),list)
        
        
        
        


unittest.main()
