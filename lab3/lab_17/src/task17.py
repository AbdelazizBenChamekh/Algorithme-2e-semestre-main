from collections import deque
import os


def find_min_k(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append((v, 0))  
        graph[v].append((u, 1))  

    max_k = 0

    for start in range(1, n + 1):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for (v, cost) in graph[u]:
                if dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    if cost == 1:
                        q.append(v)
                    else:
                        q.appendleft(v)

        current_max = max(dist[1:n + 1])
        if current_max > max_k:
            max_k = current_max

    return max_k


def main():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(script_dir, 'txtf', 'input.txt')
    output_path = os.path.join(script_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n, m = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:m + 1]]

    result = find_min_k(n, edges)

    with open(output_path, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()