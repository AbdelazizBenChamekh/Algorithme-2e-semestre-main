import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task7 import longest_common_substring

def test_longest_common_substring_time():
    p = "cool" * 100  
    t = "toolbox" * 100  

    tracemalloc.start()
    start_time = time.time()

    result = longest_common_substring(p, t)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for longest common substring: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_longest_common_substring_time()



