import unittest
from lab1.lab_20.src.task20 import count_almost_palindromes

class TestAlmostPalindrome(unittest.TestCase):
    def test_example_1(self):
        N = 5
        K = 1
        S = "abcde"
        result = count_almost_palindromes(N, K, S)
        self.assertEqual(result, 12)

    def test_example_2(self):
        N = 3
        K = 3
        S = "aaa"
        result = count_almost_palindromes(N, K, S)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()