from collections import deque
import os


def calculate_pendants(N, M, grid, queen_pos, L, musketeers):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    qx, qy = queen_pos
    time_grid = [[-1] * M for _ in range(N)]

    queue = deque([(qx, qy)])
    time_grid[qx][qy] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == '0' and time_grid[nx][ny] == -1:
                    time_grid[nx][ny] = time_grid[x][y] + 1
                    queue.append((nx, ny))

    total = 0
    for x, y, p in musketeers:
        if time_grid[x][y] != -1 and time_grid[x][y] <= L:
            total += p
    return total


def main():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(script_dir, 'txtf', 'input.txt')
    output_path = os.path.join(script_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    N, M = map(int, lines[0].split())
    grid = [list(line) for line in lines[1:N + 1]]
    qx, qy, L = map(int, lines[N + 1].split())
    musketeers = []
    for line in lines[N + 2:N + 6]:
        parts = list(map(int, line.split()))
        musketeers.append((parts[0] - 1, parts[1] - 1, parts[2]))  

    result = calculate_pendants(N, M, grid, (qx - 1, qy - 1), L, musketeers)

    with open(output_path, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()