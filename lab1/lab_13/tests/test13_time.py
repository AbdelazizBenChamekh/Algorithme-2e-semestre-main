import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task13 import can_divide_into_three

def test_time_and_memory():
    values = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]

    tracemalloc.start()
    start_time = time.time()

    result = can_divide_into_three(values)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_time_and_memory()

