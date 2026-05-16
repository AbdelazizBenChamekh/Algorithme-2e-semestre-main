from collections import deque
import os


def count_beds(N, M, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                count += 1
                queue = deque([(i, j)])
                grid[i][j] = '.'

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '#':
                            grid[nx][ny] = '.'
                            queue.append((nx, ny))
    return count


def main():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(script_dir, 'txtf', 'input.txt')
    output_path = os.path.join(script_dir, 'txtf', 'output.txt')

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    N, M = map(int, lines[0].split())
    grid = [list(line) for line in lines[1:N + 1]]

    result = count_beds(N, M, grid)

    with open(output_path, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()