import unittest
from lab2.lab_13.src.task13 import AVLTree

class TestAVLTree(unittest.TestCase):

    def test_no_rotation_needed(self):
        nodes = [
            (10, 5, 0),
            (5, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        self.assertEqual(rotated_tree, avl.tree)

    def test_rotation_on_single_node(self):
        nodes = [
            (10, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        self.assertEqual(rotated_tree, avl.tree)

if __name__ == "__main__":
    unittest.main()


