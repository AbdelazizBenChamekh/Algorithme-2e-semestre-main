import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task1 import naive_substring_search

def test_substring_search_time():
    p = "aba"
    t = "abaCaba" * 1000 

    tracemalloc.start()
    start_time = time.time()

    count, matches = naive_substring_search(p, t)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for substring search: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_substring_search_time()


