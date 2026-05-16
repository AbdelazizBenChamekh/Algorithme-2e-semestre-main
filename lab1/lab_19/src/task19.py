import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_file3, write_output_file3  

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parentheses(s, i, j):
    if i == j:
        return "A"
    else:
        return f"({print_optimal_parentheses(s, i, s[i][j])}{print_optimal_parentheses(s, s[i][j] + 1, j)})"

data = read_input_file3(file_path1)
n = int(data[0])
p = []

for i in range(1, n + 1):
    a, b = map(int, data[i].split())
    p.append(a)
p.append(b)

m, s = matrix_chain_order(p)
optimal_parentheses = print_optimal_parentheses(s, 0, n - 1)

write_output_file3(file_path2, optimal_parentheses)
