import unittest
from lab4.lab_7.src.task7 import longest_common_substring

class TestLongestCommonSubstring(unittest.TestCase):

    def test_example_case_1(self):
        p = "cool"
        t = "toolbox"
        start_pos_p, start_pos_t, max_len = longest_common_substring(p, t)
        self.assertEqual(start_pos_p, 1)
        self.assertEqual(start_pos_t, 1)
        self.assertEqual(max_len, 3)

    def test_example_case_2(self):
        p = "aabaa"
        t = "aabaa baabaa"
        start_pos_p, start_pos_t, max_len = longest_common_substring(p, t)
        self.assertEqual(start_pos_p, 0)
        self.assertEqual(start_pos_t, 0)
        self.assertEqual(max_len, 5)

    def test_no_common_substring(self):
        p = "abc"
        t = "xyz"
        start_pos_p, start_pos_t, max_len = longest_common_substring(p, t)
        self.assertEqual(start_pos_p, 0)
        self.assertEqual(start_pos_t, 0)
        self.assertEqual(max_len, 0)

    def test_single_character_match(self):
        p = "a"
        t = "a"
        start_pos_p, start_pos_t, max_len = longest_common_substring(p, t)
        self.assertEqual(start_pos_p, 0)
        self.assertEqual(start_pos_t, 0)
        self.assertEqual(max_len, 1)

if __name__ == "__main__":
    unittest.main()

