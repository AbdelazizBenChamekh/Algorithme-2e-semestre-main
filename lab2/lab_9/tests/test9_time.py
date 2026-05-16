import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task9 import BST

def test_bst_time():
    nodes = [
        (10, 5, 15),
        (5, 2, 7),
        (15, 12, 20),
        (2, 0, 0),
        (7, 0, 0),
        (12, 0, 0),
        (20, 0, 0)
    ]

    tracemalloc.start()
    start_time = time.time()

    bst = BST(nodes)
    result = bst.delete_subtree(5)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for subtree deletion: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_bst_time()

