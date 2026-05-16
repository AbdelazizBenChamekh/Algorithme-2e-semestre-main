import unittest
from lab2.lab_9.src.task9 import BST

class TestBST(unittest.TestCase):
    def test_delete_existing_subtree(self):
        nodes = [
            (10, 5, 15),
            (5, 2, 7),
            (15, 12, 20),
            (2, 0, 0),
            (7, 0, 0),
            (12, 0, 0),
            (20, 0, 0)
        ]
        bst = BST(nodes)
        self.assertEqual(bst.delete_subtree(5), 4)  

    def test_delete_nonexistent_node(self):
        nodes = [
            (10, 5, 15),
            (5, 2, 7),
            (15, 12, 20),
            (2, 0, 0),
            (7, 0, 0),
            (12, 0, 0),
            (20, 0, 0)
        ]
        bst = BST(nodes)
        self.assertEqual(bst.delete_subtree(100), 7)  

    def test_empty_tree(self):
        nodes = []
        bst = BST(nodes)
        self.assertEqual(bst.delete_subtree(10), 0)  

if __name__ == "__main__":
    unittest.main()
