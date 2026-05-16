from collections import deque
import os


def find_path(n, edges, start, end):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return False


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_path = os.path.join(base_dir, 'txtf', 'output.txt')

    try:
        with open(input_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        n, m = map(int, lines[0].split())
        edges = [tuple(map(int, line.split())) for line in lines[1:m + 1]]
        start, end = map(int, lines[m + 1].split())

        result = find_path(n, edges, start, end)

        with open(output_path, 'w') as f:
            f.write('1' if result else '0')

    except FileNotFoundError:
        print(f"Erreur: Fichier introuvable. Vérifiez que input.txt existe dans le dossier txtf/")
    except Exception as e:
        print(f"Erreur: {str(e)}")


if __name__ == "__main__":
    main()