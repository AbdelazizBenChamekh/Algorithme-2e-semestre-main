import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task6 import check_bst

def test_bst_time():
    tree = [
        [10, 1, 2],
        [5, -1, -1],
        [15, -1, -1]
    ]

    tracemalloc.start()
    start_time = time.time()

    result = check_bst(tree)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 20: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_bst_time()

