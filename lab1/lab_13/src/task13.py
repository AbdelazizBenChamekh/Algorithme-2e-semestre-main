import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_filetask13, write_output_file  

def can_divide_into_three(values):
    total = sum(values)

    if total % 3 != 0:
        return 0

    target = total // 3  
    n = len(values)

    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        val = values[i - 1]
        for j in range(target, -1, -1):
            for k in range(target, -1, -1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= values[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j - values[i - 1]][k]
                if k >= values[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j][k - values[i - 1]]

    return 1 if dp[n][target][target] else 0

n, values = read_input_filetask13(file_path1)
result = can_divide_into_three(values)
write_output_file(file_path2, result)

