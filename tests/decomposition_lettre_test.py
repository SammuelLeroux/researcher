import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from distances import decomposition_lettre, count_letters
import unittest

class TestDecompositionMots(unittest.TestCase):
    def test_decomposition_mots(self):
        self.assertEqual(decomposition_lettre('PAIR'), ['A', 'I', 'P', 'R'])
        self.assertEqual(decomposition_lettre('SAPIN'), ['A', 'I', 'N', 'P', 'S'])
    
    def test_decomposition_mots_double_lettre(self):
        self.assertEqual(decomposition_lettre('APPELLE', True), ['A', 'E', 'L', 'P'])

    def test_count_letters(self):
        self.assertEqual(count_letters('SAPIN', 'PAIR'), ['A', 'I', 'N', 'P', 'R', 'S'])
        self.assertEqual(len(count_letters('LETTRE', 'TARTE')), 7)
    
    def test_decomposition_mots_vide(self):
        self.assertEqual(decomposition_lettre(''), None)


if __name__ == '__main__':
    unittest.main()