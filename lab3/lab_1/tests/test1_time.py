import time
import tracemalloc
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_1.src.task1 import find_path


def test_performance():
    n = 10000
    edges = [(i, i + 1) for i in range(1, n)]
    start, end = 1, n

    tracemalloc.start()
    start_time = time.time()

    result = find_path(n, edges, start, end)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Résultat: {result}")
    print(f"Temps: {end_time - start_time:.4f} sec")
    print(f"Mémoire max: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    test_performance()