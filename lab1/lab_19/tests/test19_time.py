import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task19 import matrix_chain_order, print_optimal_parentheses

def test_matrices_product():
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  

    tracemalloc.start()
    start_time = time.time()

    m, s = matrix_chain_order(p)
    result = print_optimal_parentheses(s, 0, len(p) - 2)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 19: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_matrices_product()
