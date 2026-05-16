import unittest
from lab4.lab_1.src.task1 import naive_substring_search

class TestNaiveSubstringSearch(unittest.TestCase):

    def test_found_at_start(self):
        p = "aba"
        t = "abaCaba"
        count, matches = naive_substring_search(p, t)
        self.assertEqual(count, 2)
        self.assertEqual(matches, [1, 5])

    def test_found_in_middle(self):
        p = "aba"
        t = "xabaCaba"
        count, matches = naive_substring_search(p, t)
        self.assertEqual(count, 2)
        self.assertEqual(matches, [2, 6])

    def test_not_found(self):
        p = "xyz"
        t = "abaCaba"
        count, matches = naive_substring_search(p, t)
        self.assertEqual(count, 0)
        self.assertEqual(matches, [])

    def test_pattern_is_t(self):
        p = "aba"
        t = "aba"
        count, matches = naive_substring_search(p, t)
        self.assertEqual(count, 1)
        self.assertEqual(matches, [1])

    def test_empty_string(self):
        p = "aba"
        t = ""
        count, matches = naive_substring_search(p, t)
        self.assertEqual(count, 0)
        self.assertEqual(matches, [])

if __name__ == "__main__":
    unittest.main()
