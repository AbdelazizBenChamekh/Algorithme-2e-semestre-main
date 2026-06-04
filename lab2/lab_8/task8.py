from collections import deque
def tree_height(N, tree):
    if N == 0: return 0
    # tree[i] = (key, left, right), нумерация с 1
    # Корень — вершина 1
    height = 0
    queue = deque([1])
    while queue:
        height += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            key, left, right = tree[node]
            if left  != 0: queue.append(left)
            if right != 0: queue.append(right)
    return height
