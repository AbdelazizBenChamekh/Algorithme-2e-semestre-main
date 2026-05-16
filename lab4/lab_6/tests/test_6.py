import unittest
from lab4.lab_6.src.task6 import z_function

class TestZFunction(unittest.TestCase):

    def test_single_character(self):
        s = "a"
        result = z_function(s)
        self.assertEqual(result, [1]) 

    def test_no_repeating_characters(self):
        s = "abcdefg"
        result = z_function(s)
        self.assertEqual(result, [7, 0, 0, 0, 0, 0, 0]) 

if __name__ == "__main__":
    unittest.main()


