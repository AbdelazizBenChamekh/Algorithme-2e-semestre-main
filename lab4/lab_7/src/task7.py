import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab4.utils import read_input_file, write_output_file

def longest_common_substring(p, t):
    n = len(p)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_pos_p = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos_p = i  
            else:
                dp[i][j] = 0

    start_pos_p = end_pos_p - max_len  
    start_pos_t = t.find(p[start_pos_p:start_pos_p + max_len])  

    return start_pos_p, start_pos_t, max_len

def process_input_and_output():
    p, t = read_input_file(file_path1)
    start_pos_p, start_pos_t, max_len = longest_common_substring(p, t)
    result = f"{start_pos_p} {start_pos_t} {max_len}"
    write_output_file(file_path2, result)

process_input_and_output()




