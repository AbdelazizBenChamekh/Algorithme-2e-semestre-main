import unittest
from lab4.lab_2.src.task2 import count_ways_to_form_palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_example_case_1(self):
        s = "treasure"
        result = count_ways_to_form_palindrome(s)
        self.assertEqual(result, 2)  

    def test_all_characters_same(self):
        s = "aaaaa"
        result = count_ways_to_form_palindrome(s)
        self.assertEqual(result, 3)  

if __name__ == "__main__":
    unittest.main()

