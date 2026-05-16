import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_17.src.task17 import find_min_k

class TestKConnexite(unittest.TestCase):
    def test_find_min_k(self):
        self.assertEqual(find_min_k(3, [(1,2),(1,3)]), 1)
        self.assertEqual(find_min_k(4, [(1,2),(2,3),(3,4)]), 3)

if __name__ == "__main__":
    unittest.main()