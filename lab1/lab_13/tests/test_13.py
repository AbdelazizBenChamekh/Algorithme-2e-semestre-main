import unittest
from lab1.lab_13.src.task13 import can_divide_into_three

class TestSouvenirs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(can_divide_into_three([3, 3, 3, 3]), 0)
        self.assertEqual(can_divide_into_three([40]), 0)
        self.assertEqual(can_divide_into_three([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]), 1)
        self.assertEqual(can_divide_into_three([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]), 1)
        self.assertEqual(can_divide_into_three([1, 1, 1, 1, 1, 1]), 1)

if __name__ == "__main__":
    unittest.main()

