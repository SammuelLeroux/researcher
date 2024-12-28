import unittest

from annexes import *

class TestAnnexes(unittest.TestCase):
    def test_distance_hamming_identique(self):
        self.assertEqual(distance_hamming("test", "test"), 0)

    def test_hamming_distance_diff(self):
        self.assertEqual(distance_hamming("test", "tent"), 1)
        self.assertEqual(distance_hamming("JAPON", "SAVON"), 2)

    def test_hamming_distance_vide(self):
        self.assertEqual(distance_hamming("", ""), 0)

if __name__ == "__main__":
    unittest.main()