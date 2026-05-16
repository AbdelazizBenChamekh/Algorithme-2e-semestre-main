import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task13 import AVLTree

def test_avl_time():
    nodes = [
        (100, 50, 150),
        (50, 25, 75),
        (150, 125, 175),
        (25, 0, 0),
        (75, 0, 0),
        (125, 0, 0),
        (175, 0, 0)
    ]

    tracemalloc.start()
    start_time = time.time()

    avl = AVLTree(nodes)
    rotated_tree = avl.left_rotate()

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for AVL left rotation: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_avl_time()


