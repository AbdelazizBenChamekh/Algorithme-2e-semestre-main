import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab2.utils import read_input_file, write_output_file

def is_bst(tree, node_idx, min_val, max_val):
    if node_idx == -1:
        return True
    
    key, left, right = tree[node_idx]

    if not (min_val < key < max_val):
        return False

    return (is_bst(tree, left, min_val, key) and
            is_bst(tree, right, key, max_val))

def check_bst(tree):
    if not tree:
        return "CORRECT"
    return "CORRECT" if is_bst(tree, 0, float('-inf'), float('inf')) else "INCORRECT"

tree = read_input_file(file_path1)
result = check_bst(tree)

write_output_file(file_path2, result)
