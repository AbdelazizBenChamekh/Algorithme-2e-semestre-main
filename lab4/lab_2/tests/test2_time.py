import sys
import os
import time
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task2 import count_ways_to_form_palindrome

def test_palindrome_time():
    s = "you will never find the treasure" * 10  

    tracemalloc.start()
    start_time = time.time()

    result = count_ways_to_form_palindrome(s)

    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time for palindrome search: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")

test_palindrome_time()


