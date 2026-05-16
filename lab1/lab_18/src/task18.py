import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_file3, write_output_file3  

def min_cost_lunches(n, costs):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  

    for i in range(n):
        for j in range(n):
            if dp[i][j] != float('inf'):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + costs[i])
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                if costs[i] > 100:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + costs[i])

    return min(dp[n][j] for j in range(n + 1))

data = read_input_file3(file_path1)
n = int(data[0])
costs = list(map(int, data[1:]))

result = min_cost_lunches(n, costs)

write_output_file3(file_path2, str(result))

