import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab1.utils import read_input_file, write_output_file  

def fractional_knapsack(n, W, items):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if W == 0:
            break
        fraction = min(weight, W)
        total_value += fraction * (value / weight)
        W -= fraction
    return total_value


n, W, items = read_input_file(file_path1)


max_value = fractional_knapsack(n, W, items)


write_output_file(file_path2, max_value)