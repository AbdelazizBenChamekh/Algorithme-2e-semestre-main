import unittest
import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_13.src.task13 import  count_beds


class TestPlanchesJardin(unittest.TestCase):
    def test_count_beds_sample(self):
        """Test avec l'exemple donné"""
        grid = [
            ['#', '#', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['.', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
            ['.', '#', '#', '#', '.', '.', '.', '.', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.']
        ]
        self.assertEqual(count_beds(5, 10, grid), 3)

    def test_count_beds_edge_cases(self):
        """Cas limites"""
        # Test grille vide
        self.assertEqual(count_beds(0, 0, []), 0)

        # Test sans planches (corrigé)
        grid = [['.' for _ in range(10)] for _ in range(5)]
        self.assertEqual(count_beds(5, 10, grid), 0)

        # Test toutes planches
        grid = [['#' for _ in range(10)] for _ in range(5)]
        self.assertEqual(count_beds(5, 10, grid), 1)

    def test_file_processing(self):
        """Test d'intégration avec fichier"""
        from lab3.lab_13.src.task13 import main

        # Création fichier temporaire
        test_input = """5 10
##......#.
.#..#...#.
.###....#.
..##....#.
........#."""

        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        input_path = os.path.join(script_dir, 'txtf', 'input.txt')
        output_path = os.path.join(script_dir, 'txtf', 'output.txt')

        with open(input_path, 'w') as f:
            f.write(test_input)

        # Exécution
        main()

        # Vérification
        with open(output_path, 'r') as f:
            result = f.read().strip()
        self.assertEqual(result, "3")


if __name__ == "__main__":
    unittest.main()