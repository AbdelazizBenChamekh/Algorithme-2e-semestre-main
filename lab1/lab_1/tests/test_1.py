
import unittest
from lab1.lab_1.src.task1 import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):
    def test_example_1(self):
        n = 3
        W = 50
        items = [(60, 20), (100, 50), (120, 30)]
        result = fractional_knapsack(n, W, items)
        self.assertAlmostEqual(result, 180.0000, places=4)

    def test_example_2(self):
        n = 1
        W = 10
        items = [(500, 30)]
        result = fractional_knapsack(n, W, items)
        self.assertAlmostEqual(result, 166.6667, places=4)

if __name__ == "__main__":
    unittest.main()