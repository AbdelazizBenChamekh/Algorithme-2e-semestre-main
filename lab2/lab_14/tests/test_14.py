import unittest
from lab2.lab_14.src.task14 import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        avl = AVLTree([])
        avl.insert(10)
        expected_tree = {10: (0, 0)}
        self.assertEqual(avl.tree, expected_tree)

    def test_insert_without_rotation(self):
        nodes = [
            (10, 5, 15),
            (5, 0, 0),
            (15, 0, 0)
        ]
        avl = AVLTree(nodes)
        avl.insert(12)
        expected_tree = {
            10: (5, 15),
            5: (0, 0),
            15: (12, 0),
            12: (0, 0)
        }
        self.assertEqual(avl.tree, expected_tree)

    def test_insert_causing_left_rotation(self):
        nodes = [
            (10, 5, 15),
            (5, 0, 0),
            (15, 0, 20),
            (20, 0, 0)
        ]
        avl = AVLTree(nodes)
        avl.insert(25)
        expected_tree = {
            15: (10, 20),
            10: (5, 0),
            5: (0, 0),
            20: (0, 25),
            25: (0, 0)
        }
        self.assertEqual(avl.tree, expected_tree)

    def test_insert_causing_right_rotation(self):
        nodes = [
            (10, 5, 15),
            (5, 2, 7),
            (15, 0, 0),
            (2, 0, 0),
            (7, 0, 0)
        ]
        avl = AVLTree(nodes)
        avl.insert(1)
        expected_tree = {
            5: (2, 10),
            2: (1, 0),
            1: (0, 0),
            10: (7, 15),
            7: (0, 0),
            15: (0, 0)
        }
        self.assertEqual(avl.tree, expected_tree)

if __name__ == "__main__":
    unittest.main()

