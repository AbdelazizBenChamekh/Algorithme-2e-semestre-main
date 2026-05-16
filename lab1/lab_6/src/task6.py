import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_file, write_output_file2  


def max_prizes(n):
    prizes = []
    k = 0
    total = 0
    while total + (k + 1) <= n:
        k += 1
        prizes.append(k)
        total += k
    if total < n:
        prizes[-1] += n - total
    return k, prizes



with open(file_path1, 'r') as file:
    n = int(file.readline().strip())  

k, prizes = max_prizes(n)


output_data = f"{k}\n" + " ".join(map(str, prizes))


write_output_file2(file_path2, output_data)