import unittest
from lab1.lab_6.src.task6 import max_prizes

class TestMaxPrizes(unittest.TestCase):
    def test_example_1(self):
        n = 6
        k, prizes = max_prizes(n)
        self.assertEqual(k, 3)
        self.assertEqual(prizes, [1, 2, 3])

    def test_example_2(self):
        n = 8
        k, prizes = max_prizes(n)
        self.assertEqual(k, 3)
        self.assertEqual(prizes, [1, 2, 5])

if __name__ == "__main__":
    unittest.main()