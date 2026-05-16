import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_15.src.task15 import calculate_pendants

class TestHeros(unittest.TestCase):
    def test_calculate_pendants(self):
        grid = [
            ['1','1','1'],
            ['1','0','1'],
            ['1','1','1']
        ]
        musketeers = [(1,1,5)]
        self.assertEqual(calculate_pendants(3, 3, grid, (1,1), 5, musketeers), 5)

if __name__ == "__main__":
    unittest.main()