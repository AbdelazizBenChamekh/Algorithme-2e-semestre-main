import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task16 import KthMax

def test_kth_max_time():
    kth_max_ds = KthMax()
    
    tracemalloc.start()
    start_time = time.time()

    for i in range(1, 100001):
        kth_max_ds.add(i)

    for k in range(1, 1001):
        kth_max_ds.kth_max(k)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for K-th maximum operations: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_kth_max_time()

