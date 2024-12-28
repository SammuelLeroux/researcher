import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distances import distance_hamming
import unittest

class TestDistanceHamming(unittest.TestCase):
    def test_distance_hamming_identique(self):
        self.assertEqual(distance_hamming('test', 'test'), 0)

    def test_hamming_distance_diff(self):
        self.assertEqual(distance_hamming('test', 'tent'), 1)
        self.assertEqual(distance_hamming('JAPON', 'SAVON'), 2)

    def test_hamming_distance_vide(self):
        self.assertEqual(distance_hamming('', ''), None)

    def test_hamming_distance_longeur_diff(self):
        self.assertEqual(distance_hamming('abc', 'a'), None)

if __name__ == '__main__':
    unittest.main()