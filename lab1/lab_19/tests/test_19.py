import unittest
from lab1.lab_19.src.task19 import matrix_chain_order, print_optimal_parentheses

class TestMatricesProduct(unittest.TestCase):
    def test_example_1(self):
        p = [10, 50, 90, 20]
        m, s = matrix_chain_order(p)
        result = print_optimal_parentheses(s, 0, len(p) - 2)
        self.assertIn(result, ["((AA)A)", "(A(AA))"])

    def test_example_2(self):
        p = [10, 20, 30, 40, 50]
        m, s = matrix_chain_order(p)
        result = print_optimal_parentheses(s, 0, len(p) - 2)
        self.assertIn(result, ["((A(AA))A)", "(((AA)A)A)"])

if __name__ == "__main__":
    unittest.main()