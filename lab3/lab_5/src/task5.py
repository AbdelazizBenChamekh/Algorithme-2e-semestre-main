from collections import defaultdict, deque
import os


def kosaraju(n, edges):
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)

    # Premier parcours DFS
    visited = [False] * (n + 1)
    order = []

    def dfs(u):
        stack = [u]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                order.append(node)

    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u)

    # Deuxième parcours
    visited = [False] * (n + 1)
    components = 0

    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            while stack:
                node = stack.pop()
                for neighbor in rev_graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            components += 1

    return components


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_path = os.path.join(base_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n, m = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:m + 1]]

    result = kosaraju(n, edges)

    with open(output_path, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()