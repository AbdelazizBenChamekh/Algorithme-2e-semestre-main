import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task6 import max_prizes

def test_max_prizes():
    n = 10**9  

    tracemalloc.start()
    start_time = time.time()

    k, prizes = max_prizes(n)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 6: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_max_prizes()
