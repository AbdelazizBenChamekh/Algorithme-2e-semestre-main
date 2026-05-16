import time
import tracemalloc
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab3.lab_13.src.task13 import count_beds


def test_performance():
    """Test de performance avec grande grille"""
    N, M = 200, 200
    grid = []
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append('#' if random.random() > 0.7 else '.')
        grid.append(row)

    tracemalloc.start()
    start_time = time.time()

    result = count_beds(N, M, grid)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Nombre de planches: {result}")
    print(f"Temps d'exécution: {end_time - start_time:.4f} sec")
    print(f"Mémoire maximale utilisée: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    test_performance()