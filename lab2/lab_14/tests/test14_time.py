import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task14 import AVLTree

def test_avl_insertion_time():
    nodes = [
        (50, 25, 75), (25, 10, 30), (75, 60, 90),
        (10, 5, 15), (30, 27, 35), (60, 55, 70), (90, 85, 100),
        (5, 0, 0), (15, 0, 0), (27, 0, 0), (35, 0, 0),
        (55, 0, 0), (70, 0, 0), (85, 0, 0), (100, 0, 0)
    ]
    
    tracemalloc.start()
    start_time = time.time()

    avl = AVLTree(nodes)
    
    insert_keys = [20, 45, 65, 95, 110, 120, 130, 140, 150]
    for key in insert_keys:
        avl.insert(key)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for AVL multiple insertions: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_avl_insertion_time()


