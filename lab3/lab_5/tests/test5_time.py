import time
import tracemalloc
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_5.src.task5 import kosaraju


def test_performance():
    # Génération d'un grand graphe
    n = 10000
    edges = [(i, i + 1) for i in range(1, n)] + [(n, 1)]  # Cycle

    tracemalloc.start()
    start_time = time.time()

    result = kosaraju(n, edges)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Résultat: {result}")
    print(f"Temps: {end_time - start_time:.4f} sec")
    print(f"Mémoire max: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    test_performance()