import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task6 import z_function

def test_z_function_time():
    s = "aaaaAAA" * 1000  

    tracemalloc.start()
    start_time = time.time()

    result = z_function(s)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for Z-function: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_z_function_time()



