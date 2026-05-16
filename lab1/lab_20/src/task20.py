import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_file3, write_output_file3 

def count_almost_palindromes(N, K, S):
    count = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            substring = S[i:j]
            changes_needed = 0
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    changes_needed += 1
                left += 1
                right -= 1
            if changes_needed <= K:
                count += 1
    return count

data = read_input_file3(file_path1)

first_line = data[0].split()
if len(first_line) < 2:
    raise ValueError("Invalid input format: Expected two integers in the first line")

N, K = map(int, first_line)
S = data[1].strip()

result = count_almost_palindromes(N, K, S)

write_output_file3(file_path2, str(result))

