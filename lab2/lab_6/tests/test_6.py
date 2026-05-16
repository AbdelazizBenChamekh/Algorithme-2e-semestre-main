import unittest
from lab2.lab_6.src.task6 import check_bst

class TestBinarySearchTree(unittest.TestCase):
    def test_correct_bst(self):
        tree = [
            [2, 1, 2],
            [1, -1, -1],
            [3, -1, -1]
        ]
        self.assertEqual(check_bst(tree), "CORRECT")

    def test_incorrect_bst(self):
        tree = [
            [3, 1, 2],
            [1, -1, -1],
            [2, -1, -1]
        ]
        self.assertEqual(check_bst(tree), "INCORRECT")

    def test_empty_tree(self):
        tree = []
        self.assertEqual(check_bst(tree), "CORRECT")

    def test_single_node_tree(self):
        tree = [[42, -1, -1]]
        self.assertEqual(check_bst(tree), "CORRECT")

    def test_large_correct_bst(self):
        tree = [
            [10, 1, 2],
            [5, -1, -1],
            [15, -1, -1]
        ]
        self.assertEqual(check_bst(tree), "CORRECT")

    def test_large_incorrect_bst(self):
        tree = [
            [10, 1, 2],
            [15, -1, -1],
            [5, -1, -1]
        ]
        self.assertEqual(check_bst(tree), "INCORRECT")

if __name__ == "__main__":
    unittest.main()
