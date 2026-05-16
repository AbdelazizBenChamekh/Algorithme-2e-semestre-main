import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task18 import min_cost_lunches

def test_cafe_coupons():
    n = 100 
    costs = [i * 3 for i in range(1, n + 1)]  

    tracemalloc.start()
    start_time = time.time()

    result = min_cost_lunches(n, costs)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 18: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_cafe_coupons()
