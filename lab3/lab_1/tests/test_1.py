import unittest
import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_1.src.task1 import find_path


class TestLabirynthe(unittest.TestCase):
    def test_path_exists(self):
        self.assertTrue(find_path(4, [(1, 2), (2, 3), (3, 4)], 1, 4))
        self.assertFalse(find_path(4, [(1, 2), (3, 4)], 1, 3))

    def test_file_structure(self):
        """Teste l'intégration avec la structure de fichiers"""
        from lab3.lab_1.src.task1 import main

        test_dir = os.path.dirname(__file__)
        base_dir = os.path.join(test_dir, '..')

        input_path = os.path.join(base_dir, 'txtf', 'input.txt')
        output_path = os.path.join(base_dir, 'txtf', 'output.txt')

        with open(input_path, 'w') as f:
            f.write("4 3\n1 2\n2 3\n3 4\n1 4")

        main()

        with open(output_path, 'r') as f:
            result = f.read().strip()
        self.assertEqual(result, "1")


if __name__ == "__main__":
    unittest.main()