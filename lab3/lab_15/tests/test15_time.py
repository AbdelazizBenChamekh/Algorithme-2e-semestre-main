import time
import tracemalloc
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_15.src.task15 import calculate_pendants


def test_performance():
    N, M = 20, 20
    grid = [['1'] * M for _ in range(N)]
    # Création d'un chemin central
    for i in range(5, 15):
        for j in range(5, 15):
            grid[i][j] = '0'

    musketeers = [(1, 1, 10), (18, 18, 10), (1, 18, 10), (18, 1, 10)]

    tracemalloc.start()
    start_time = time.time()

    result = calculate_pendants(N, M, grid, (10, 10), 30, musketeers)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Pendants livrés: {result}")
    print(f"Temps: {end_time - start_time:.4f} sec")
    print(f"Mémoire max: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    test_performance()