import unittest
import os
import sys
from collections import defaultdict, deque

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_5.src.task5 import kosaraju

class TestVilleUnidirectionnelle(unittest.TestCase):
    def test_kosaraju(self):
        self.assertEqual(kosaraju(4, [(1,2),(4,1),(2,3),(3,1)]), 2)
        self.assertEqual(kosaraju(5, [(2,1),(3,2),(3,1),(4,3),(4,1),(5,2),(5,3)]), 5)
        self.assertEqual(kosaraju(3, []), 3)  # Aucune arête

if __name__ == "__main__":
    unittest.main()