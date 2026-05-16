import time
import tracemalloc
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_17.src.task17 import find_min_k


def test_performance():
    n = 100  # 100 nœuds
    edges = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j and random.random() < 0.1]

    tracemalloc.start()
    start_time = time.time()

    result = find_min_k(n, edges)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"K minimum: {result}")
    print(f"Temps: {end_time - start_time:.4f} sec")
    print(f"Mémoire max: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    test_performance()