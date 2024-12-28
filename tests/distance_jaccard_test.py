import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distances import distance_jaccard
import unittest

class TestDistanceJaccard(unittest.TestCase):        
    def test_distance_jaccard(self):
        self.assertEqual(distance_jaccard('PAIR', 'SAPIN'), 1-(1/2))
        self.assertEqual(distance_jaccard('LETTRE', 'TARTE'), 1-(4/7))


if __name__ == '__main__':
    unittest.main()