import unittest
from lab1.lab_15.src.task15 import remove_invalid_brackets

class TestBrackets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(remove_invalid_brackets("([)]"), "[]")
        self.assertEqual(remove_invalid_brackets("{[()]}"), "{[()]}")
        self.assertEqual(remove_invalid_brackets("((())"), "(())")
        self.assertEqual(remove_invalid_brackets(")("), "")
        self.assertEqual(remove_invalid_brackets("[{]}"), "{}")

if __name__ == "__main__":
    unittest.main()
