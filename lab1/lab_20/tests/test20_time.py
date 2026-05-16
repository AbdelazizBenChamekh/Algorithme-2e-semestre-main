import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import time
import tracemalloc
from task20 import count_almost_palindromes

def test_almost_palindrome():
    N = 100  
    K = 100  
    S = "a" * N  

    tracemalloc.start()
    start_time = time.time()
    result = count_almost_palindromes(N, K, S)
    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for exercise 20: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_almost_palindrome()
