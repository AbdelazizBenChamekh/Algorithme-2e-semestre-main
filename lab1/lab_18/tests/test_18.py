import unittest
from lab1.lab_18.src.task18 import min_cost_lunches

class TestCafeCoupons(unittest.TestCase):
    def test_example_1(self):
        n = 5
        costs = [110, 40, 120, 110, 60]
        result = min_cost_lunches(n, costs)
        self.assertEqual(result, 260)

    def test_example_2(self):
        n = 3
        costs = [110, 110, 110]
        result = min_cost_lunches(n, costs)
        self.assertEqual(result, 220)

if __name__ == "__main__":
    unittest.main()