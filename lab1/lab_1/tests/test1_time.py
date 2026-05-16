import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task1 import fractional_knapsack

def test_fractional_knapsack():
    n = 1000  
    W = 2000  
    items = [(i, i) for i in range(1, n + 1)] 

    tracemalloc.start()
    start_time = time.time()

    result = fractional_knapsack(n, W, items)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 1: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_fractional_knapsack()
