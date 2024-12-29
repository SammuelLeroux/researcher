import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distances import distance_levenshtein
import unittest

class TestDistanceLevenshtein(unittest.TestCase):        
    def test_distance_levenshtein(self):
        self.assertEqual(distance_levenshtein('PAS', 'PLAT'), 2)
        self.assertEqual(distance_levenshtein('VOILE', 'CERISE'), 4)

    def test_distance_levenshtein_vide(self):
        self.assertEqual(distance_levenshtein('PLAT', ''), None)
        self.assertEqual(distance_levenshtein('', 'PLAT'), None)
        self.assertEqual(distance_levenshtein('', ''), None)


if __name__ == '__main__':
    unittest.main()